import pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
password = os.getenv("MONGO_PASSWORD_NEW")

client = pymongo.MongoClient(
    f"mongodb+srv://debanwesa_bandhu:{password}@cluster0.u5akrs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
path="BackEnd\\database\\Gujarat"
dir_list=os.listdir(path)
#print("files in gujarat are")
#print(dir_list)

for file in dir_list:

    df = pd.read_csv(f"BackEnd\\database\\Gujarat\\{file}")

    data = df.to_dict(orient="records")

    db = client['Gujarat']
    collection=db[file]
    db.collection.insert_many(data)
