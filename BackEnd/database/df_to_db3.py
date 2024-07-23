import pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
password = os.getenv("MONGO_PASSWORD_NEW")

client = pymongo.MongoClient(
    f"mongodb+srv://hindol_banerjee:{password}@cluster0.u5akrs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

path = "BackEnd\\database\\final_impressions.csv"

df = pd.read_csv(path)

db = client['Other']

data = df.to_dict(orient="records")
db.reasons.insert_many(data)
