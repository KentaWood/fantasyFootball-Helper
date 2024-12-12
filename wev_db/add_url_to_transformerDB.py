import os
import sys
import requests
from bs4 import BeautifulSoup
import weaviate

def fetch_and_add_urls_to_weaviate_from_file(file_path, client, class_name):
    # Ensure the file exists
    if not os.path.isfile(file_path):
        print(f"Error: The file '{file_path}' does not exist.")
        return

    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()  # Read all lines from the file
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return

    # Process each URL
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespace or newlines
        if not url:
            continue  # Skip empty lines

        try:
            # Step 1: Fetch the webpage
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Successfully fetched: {url}")
            else:
                print(f"Failed to fetch {url}: {response.status_code}")
                continue

            # Step 2: Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")

            # Step 3: Extract and clean the text
            page_text = soup.get_text(strip=True)
            if not page_text:
                print(f"No content found for {url}. Skipping.")
                continue

            # Step 4: Add data to Weaviate
            data_object = {
                "url": url,
                "content": page_text,
            }
            client.data_object.create(data_object, class_name=class_name)
            print(f"Data added for URL: {url}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
        except weaviate.exceptions.WeaviateException as we:
            print(f"Error adding data to Weaviate for {url}: {we}")

def fetch_and_add_urls_to_weaviate_from_directory(directory, client, class_name):
    # Iterate through all files in the given directory (non-recursive)
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)  # Full path of the file

        # Ensure it's a file (not a directory)
        if not os.path.isfile(file_path):
            continue

        fetch_and_add_urls_to_weaviate_from_file(file_path, client, class_name)

if __name__ == "__main__":
    # Check if the correct arguments are passed
    if len(sys.argv) < 3:
        print("Usage: python fetch_urls.py --file <file_path> or --directory <directory_path>")
        sys.exit(1)

    mode = sys.argv[1]
    path = sys.argv[2]

    # Connect to Weaviate
    client = weaviate.Client("http://localhost:1234")  # Ensure the correct port is used

    # Define the class name
    class_name = "WebPage"

    # Check if the class exists
    if not client.schema.exists(class_name):
        print(f"Error: Schema '{class_name}' does not exist. Please create it first.")
        sys.exit(1)

    if mode == "--file":
        fetch_and_add_urls_to_weaviate_from_file(path, client, class_name)
    elif mode == "--directory":
        fetch_and_add_urls_to_weaviate_from_directory(path, client, class_name)
    else:
        print("Error: Invalid mode. Use --file for a single file or --directory for a directory.")
        sys.exit(1)
