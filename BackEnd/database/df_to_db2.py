import pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
password = os.getenv("MONGO_PASSWORD_NEW")

client = pymongo.MongoClient(
    f"mongodb+srv://hindol_banerjee:{password}@cluster0.u5akrs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# path="BackEnd\\database\\Gujarat"
# dir_list=os.listdir(path)
# print("files in gujarat are")
# print(dir_list)

# for file in dir_list:
#      try:
#         df = pd.read_csv(f"BackEnd\\database\\Gujarat\\{file}")

#         data = df.to_dict(orient="records")

#         db = client['Gujarat']
#         collection=db[file]
#         collection.insert_many(data)
#      except Exception as e:
#          print(e)

''' formatted_cluster_data '''
# df = pd.read_csv("BackEnd\\database\\Gujarat\\formatted_cluster_data.csv")

# data = df.to_dict(orient="records")

# db = client['Gujarat']

# db.formatted_cluster_data.insert_many(data)

''' Latlong '''

df = pd.read_csv("BackEnd\\database\\Gujarat\\latlong.csv")

data = df.to_dict(orient="records")

db = client['Gujarat']

db.latlong.insert_many(data)

''' rates '''

# df = pd.read_csv("BackEnd\\database\\Gujarat\\rates.csv")

# data = df.to_dict(orient="records")

# db = client['Gujarat']

# db.rates.insert_many(data)

''' reasons '''

# df = pd.read_csv("BackEnd\\database\\Gujarat\\reasons.csv")

# data = df.to_dict(orient="records")

# db = client['Gujarat']

# db.reasons.insert_many(data)
