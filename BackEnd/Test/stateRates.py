import os
import pandas as pd

path = "DATA\\Test\\DistrictWiseData"


problemList = ["Arunachal Pradesh.csv", "Chandigarh.csv", "Goa.csv",
                "Ladakh.csv", "Lakshadweep.csv"]

files = os.listdir(path)
for file in problemList:
    files.remove(file)

csvFile = pd.read_csv(path + "//" +files[0])
df = pd.DataFrame(csvFile)

files.remove(files[0])

for file in files:
    if file.endswith('.csv'):
       tempdf = pd.read_csv(path + "\\" + file)
       df = pd.concat([df, tempdf], axis=0)

print(df.head())
df.to_csv("DATA\\Test\\DistrictWiseData\\IndiaDistricts.csv", index=False)