import pymongo
import pandas as pd
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
password = os.getenv("MONGO_PASSWORD_NEW")

client = pymongo.MongoClient(
    f"mongodb+srv://hindol_banerjee:{password}@cluster0.u5akrs9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client2 = pymongo.MongoClient(
    f"mongodb+srv://hindol_banerjee:{password}@cluster1.jf2mcdo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1")

path = "BackEnd\\database\\States"

problemList = ["Arunachal_Pradesh",
               "Chandigarh", "Goa", "Ladakh", "Lakshadweep"]
list_state = os.listdir(path)
print(list_state)

count = 0
for file in list_state:
    if file not in problemList:
        latlong_path = path+"\\"+file+"\\latlong.csv"
        cluster_path = path+"\\"+file+"\\cluster.csv"
        state_cluster_path = path+"\\"+file+"\\state_cluster.csv"
        df1 = pd.read_csv(latlong_path)
        df2 = pd.read_csv(cluster_path)
        df3 = pd.read_csv(state_cluster_path)

        # client.drop_database(file)
        # client2.drop_database(file)

        if count < 15:
            db = client[file]

            data = df1.to_dict(orient="records")
            db.latlong.insert_many(data)

            data = df2.to_dict(orient="records")
            db.cluster.insert_many(data)

            data = df3.to_dict(orient="records")
            db.state_cluster.insert_many(data)

        else:
            db = client2[file]

            data = df1.to_dict(orient="records")
            db.latlong.insert_many(data)

            data = df2.to_dict(orient="records")
            db.cluster.insert_many(data)

            data = df3.to_dict(orient="records")
            db.state_cluster.insert_many(data)

        count += 1
