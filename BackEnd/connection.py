import os
from pymongo import MongoClient
from dotenv import load_dotenv
#from pathlib import Path

load_dotenv()
password = os.getenv("MONGO_PASSWORD_NEW")
#print(f"Password: {password}")
client =MongoClient(
    f"mongodb+srv://hindol_banerjee:{password}@cluster0.u5akrs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


# Specify the database and collection
db = client['Andhra_Pradesh']  
collection = db['cluster']  

# Fetch all documents in the collection
#documents = collection.find()
filter = {'social category': 'SC'}

# Fetch all documents matching the filter
documents = collection.find(filter)


# Iterate over the documents and print them
for document in documents:
    print(document)

# Close the connection
client.close()
