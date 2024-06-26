import pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
password = os.getenv("MONGO_PASSWORD")

client = pymongo.MongoClient(
    f"mongodb+srv://dropwrap:{password}@gujarat.jwam9ab.mongodb.net/?retryWrites=true&w=majority&appName=Gujarat")

df = pd.read_csv("BackEnd\\database\\formatted_cluster_data.csv")

# print(df.head())

data = df.to_dict(orient="records")

db = client['Cluster_No']

db.Cluster_nos.insert_many(data)
