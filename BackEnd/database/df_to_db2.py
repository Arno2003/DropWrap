import pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
password = os.getenv("MONGO_PASSWORD_NEW")

client = pymongo.MongoClient(
    f"mongodb+srv://hindol_banerjee:{password}@cluster0.u5akrs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
path = "BackEnd\\database\\States"

problemList = ["Arunachal_Pradesh",
               "Chandigarh", "Goa", "Ladakh", "Lakshadweep"]
list_state = os.listdir(path)
print(list_state)
for file in list_state:
    if file not in problemList:
        latlong_path = path+"\\"+file+"\\latlong.csv"
        cluster_path = path+"\\"+file+"\\cluster.csv"
        print(latlong_path, cluster_path)
        df1 = pd.read_csv(latlong_path)
        df2 = pd.read_csv(cluster_path)

        data = df1.to_dict(orient="records")
        db = client[file]
        db.latlong.insert_many(data)

        data = df2.to_dict(orient="records")
        db = client[file]
        db.cluster.insert_many(data)
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

# df = pd.read_csv("BackEnd\\database\\Gujarat\\formatted_cluster_data.csv")

# data = df.to_dict(orient="records")

# db = client['Gujarat']

# db.formatted_cluster_data.insert_many(data)

# df = pd.read_csv("BackEnd\\database\\Gujarat\\latlong.csv")

# data = df.to_dict(orient="records")

# db = client['Gujarat']

# db.latlong.insert_many(data)

# df = pd.read_csv("BackEnd\\database\\Gujarat\\rates.csv")

# data = df.to_dict(orient="records")

# db = client['Gujarat']

# db.rates.insert_many(data)

# df = pd.read_csv("BackEnd\\database\\Gujarat\\reasons.csv")

# data = df.to_dict(orient="records")

# db = client['Gujarat']

# db.reasons.insert_many(data)
