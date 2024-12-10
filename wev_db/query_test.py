import weaviate

CLASS_NAME = "WebPage"

def query_weaviate():
    # Connect to Weaviate
    client = weaviate.Client("http://localhost:1234")  # Ensure the correct port

    # Ask the user for the class name and query text
    query_text = input("Enter your search query: ").strip()

    try:
        # Perform the query
        response = client.query.get(CLASS_NAME, ["url", "content"]) \
            .with_near_text({"concepts": [query_text]}) \
            .with_limit(2) \
            .do()

        # Extract and print the result
        result = response.get("data", {}).get("Get", {}).get(CLASS_NAME, [])
        if result:
            for obj in result:
                print("\nQuery Result:")
                print(f"URL: {obj.get('url')}")
                print(f"Content: {obj.get('content')}\n")
        else:
            print("\nNo results found for your query.")
    except weaviate.exceptions.UnexpectedStatusCodeException as e:
        print(f"Query failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    query_weaviate()
