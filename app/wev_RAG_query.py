import weaviate

CLASS_NAME = "WebPage"


"""
>>>

"""
def query_weaviate(query):
    # Connect to Weaviate
    client = weaviate.Client("http://localhost:1234")  # Ensure the correct port

    # Ask the user for the class name and query text
    query_text = query

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
                return obj.get('content')
        else:
            print("\nNo results found for your query.")
    except weaviate.exceptions.UnexpectedStatusCodeException as e:
        print(f"Query failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
