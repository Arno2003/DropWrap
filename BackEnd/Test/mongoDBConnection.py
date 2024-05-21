from pymongo import MongoClient

password = "teLPS2jcDkFU7rbl"
# Step 1: Connect to MongoDB
url = "mongodb+srv://dropwrap:{password}@gujarat.jwam9ab.mongodb.net/?retryWrites=true&w=majority&appName=Gujarat"
cluster = MongoClient(url)
db = cluster["DropWrap"]
collection = db["Gujarat"]

# Step 2: Define the query 
# query = {"field_name": "value_to_match"}  

# Step 3: Fetch data from MongoDB
documents = collection.find()

# Step 4: Process the fetched data
for document in documents:
    print(document)

# step5: Close the connection
cluster.close()
