from pymongo import MongoClient
from dotenv import load_dotenv, dotenv_values
import os 

def Connect():
    try:
        password = os.getenv("PASSWORD")
        # Step 1: Connect to MongoDB
        url = f"mongodb+srv://dropwrap:{password}@gujarat.jwam9ab.mongodb.net/?retryWrites=true&w=majority&appName=Gujarat"
        cluster = MongoClient(url)
        print("pass1")
        # print(cluster)
        db = cluster["DropWrap"]
        print()
        print(db)
        print()
        collection = db["Gujarat"]
        print("pass2")

        # Step 2: Define the query 
        # query = {"field_name": "value_to_match"}  

        # Step 3: Fetch data from MongoDB
        # cursor = collection.find()
        print("pass3")
        document = list(collection.find())
        print(*document)
        print("pass4")
        # Step 4: Process the fetched data
        # for document in documents:
        #     print(document)

        # step5: Close the connection
        cluster.close()
    except Exception as e:
        print(e)
        
Connect()