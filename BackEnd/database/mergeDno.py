import pandas as pd
import os

dno_path = "DATA\\Test\\Abbreviations\\stateDNoMapping.csv"
stateCluster_path = "BackEnd\\database\\stateWiseData.csv"

dnoDf = pd.read_csv(dno_path)
ls = []
for item in dnoDf['startingDNo']:
    ls.append(item//100)
dnoDf['DNo'] = ls

# print(ls)
clusterDf = pd.read_csv(stateCluster_path)
ls = []
for item in clusterDf['DNo']:
    ls.append(int(item))
clusterDf['DNo'] = ls

print(dnoDf.head())
print(clusterDf.head())

merged = pd.merge(dnoDf, clusterDf, on='DNo', how='right')
merged.drop(columns=['startingDNo', 'endingDNo', 'Unnamed: 0'], inplace=True)

merged.to_csv("BackEnd\database\stateWiseDataMerged.csv")

print(merged.head())
