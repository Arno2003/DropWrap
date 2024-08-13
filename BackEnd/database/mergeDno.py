import pandas as pd
import os

# base_dir = os.path.dirname(os.path.abspath(__file__))
dno_path = "..\\..\\BackEnd\\database\\stateDNoMapping.csv"
stateCluster_path = "..\\..\\BackEnd\\database\\stateWiseData.csv"

dnoDf = pd.read_csv(dno_path)

# print(dnoDf)
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

# print(dnoDf.head())
# print(clusterDf.head())

merged = pd.merge(dnoDf, clusterDf, on='DNo', how='right')

# print(merged.columns)

merged.drop(columns=['startingDNo', 'endingDNo'], inplace=True)

merged = merged.sort_values(by='Location', ignore_index=True)
# merged.to_csv("BackEnd\database\stateWiseDataMerged.csv")

# print(merged.head())
stateList = []
for ind, row in merged.iterrows():
    if row['Location'] not in stateList:
        stateList.append(row['Location'])


state_cluster = []
for state in stateList:
    stateName = '_'.join(state.split())
    op_dir = f"..\\..\\BackEnd\\database\\States\\{stateName}"
    for ind, row in merged.iterrows():
        if row['Location'] == state:
            state_cluster.append(row)

    if not os.path.isdir(op_dir):
        os.makedirs(op_dir)

    state_cluster_df = pd.DataFrame(state_cluster)
    state_cluster_df.to_csv(op_dir+"\\state_cluster.csv")
    state_cluster = []

print(stateList)
