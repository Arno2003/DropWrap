import pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
password = os.getenv("NEW_MONGO_PASSWORD")

client = pymongo.MongoClient(
    f"mongodb+srv://dropwrap:{password}@gujarat.jwam9ab.mongodb.net/?retryWrites=true&w=majority&appName=Gujarat")

df = pd.read_csv("BackEnd\\database\\reasons.csv")

# print(df.head())

data = df.to_dict(orient="records")

db = client['Reasons']

db.Reasons.insert_many(data)
