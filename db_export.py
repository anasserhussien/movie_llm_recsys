from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

load_dotenv()

#load URI from .env
mongo_uri = os.getenv('MONGO_URI')


# Connect to MongoDB
client = MongoClient(mongo_uri)  
db = client['sample_mflix']  
collection = db['movies']

# Fetch all documents from the collection
documents = collection.find()

try :
    with open('movies.json', 'w') as file:
        json.dump(list(documents), file, default=str, indent=4)
        print("Export completed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")