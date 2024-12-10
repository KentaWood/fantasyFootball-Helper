import weaviate

# Connect to the Weaviate instance
client = weaviate.Client("http://localhost:1234")

# Define the schema
class_name = "WebPage"
if not client.schema.exists(class_name):
    schema = {
        "class": class_name,
        "description": "A class to store webpages",
        "properties": [
            {"name": "url", "dataType": ["string"]},
            {"name": "content", "dataType": ["text"]},
        ],
        "vectorizer": "text2vec-transformers",  # Automatically vectorize "content"
    }
    client.schema.create_class(schema)
    print(f"Schema '{class_name}' created!")

