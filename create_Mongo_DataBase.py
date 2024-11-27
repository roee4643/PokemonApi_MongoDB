from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

def create_collection():
    # Connect to MongoDB (update the URI as needed)
    client = MongoClient("mongodb://54.149.108.64:27017/")
    db = client["mydatabase"]  # Use an existing or new database named 'mydatabase'

    # Define the collection name
    collection_name = "Pokemon"

    try:
        # Check if the collection already exists
        if collection_name in db.list_collection_names():
            print("Collection Pokemon already exists.")
        else:
            # Create the collection (implicitly done with first insertion in MongoDB)
            db.create_collection(collection_name)
            print("Collection created:", collection_name)

    except CollectionInvalid as e:
        print(f"Unexpected error: {e}")

# Call the function
create_collection()
