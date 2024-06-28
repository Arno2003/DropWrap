from pymongo import MongoClient
from dotenv import load_dotenv, dotenv_values
import os 

def Connect():
    try:
        load_dotenv()
        password = os.getenv("MONGO_PASSWORD")
        print("password : ", password)
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
        query = {"Social Category": {"$eq":"General"}}

        # Step 3: Fetch data from MongoDB
        cursor = collection.find()
        print(cursor)
        print("pass3")
        # Step 4: Process the fetched data
        for document in cursor:
            print("document : ", document)
        # step5: Close the connection
        cluster.close()
        
    except Exception as e:
        print(e)
        
Connect()