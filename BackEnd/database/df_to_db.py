import pymongo
import os
from pymongo import MongoClient
import pandas as pd

password = "teLPS2jcDkFU7rbl"


def connect_to_mongo(db_name, collection_name, df):
    url = f"mongodb+srv://dropwrap:{password}@gujarat.jwam9ab.mongodb.net/?retryWrites=true&w=majority&appName=Gujarat"
    cluster = MongoClient(url)
    db = cluster[db_name]
    collection = db[collection_name]

    data = df.to_dict(orient="records")
    print(data)
    # post = {"name": "Hindol", "score": 5}
    # collection.insert_one(post)


andra = pd.read_csv('BackEnd\database\Andhra Pradesh.csv')
# print(andra)
connect_to_mongo("test", "test", andra)
