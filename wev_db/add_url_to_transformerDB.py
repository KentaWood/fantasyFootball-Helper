import os
import sys
import requests
from bs4 import BeautifulSoup
import weaviate


def fetch_and_add_urls_to_weaviate(directory):
    # Connect to Weaviate
    client = weaviate.Client("http://localhost:1234")  # Ensure the correct port is used

    # Define the class name
    class_name = "WebPage"

    # Check if the class exists
    if not client.schema.exists(class_name):
        print(f"Error: Schema '{class_name}' does not exist. Please create it first.")
        return

    # Iterate through all files in the given directory (non-recursive)
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)  # Full path of the file

        # Ensure it's a file (not a directory)
        if not os.path.isfile(file_path):
            continue

        # Open each file containing URLs
        try:
            with open(file_path, 'r') as file:
                urls = file.readlines()  # Read all lines from the file
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            continue

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


if __name__ == "__main__":
    # Get the directory from command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python fetch_urls.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)

    # Call the function to fetch and add data
    fetch_and_add_urls_to_weaviate(directory)
