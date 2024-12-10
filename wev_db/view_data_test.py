import weaviate

def view_database_contents():
    # Connect to Weaviate
    client = weaviate.Client("http://localhost:1234")  # Ensure the correct port

    # Ask the user for the class name to inspect
    class_name = input("Enter the class name to view (e.g., WebPage): ").strip()

    try:
        # Query all data in the class with a limit
        response = client.query.get(class_name, ["url", "content"]) \
            .with_limit(100).do()

        # Parse and display results
        results = response.get("data", {}).get("Get", {}).get(class_name, [])
        if results:
            print(f"\nContents of class '{class_name}':\n")
            for i, obj in enumerate(results, 1):
                print(f"Result {i}:")
                print(f"  URL: {obj.get('url')}")
                print(f"  Content: {obj.get('content')[:300]}...\n")  # Print the first 300 characters for readability
                print("-" * 80)
        else:
            print(f"No data found in the class '{class_name}'.")

    except weaviate.exceptions.UnexpectedStatusCodeException as e:
        print(f"Query failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    view_database_contents()
