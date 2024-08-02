import pandas as pd
import os

dfs = []
files = os.listdir("BackEnd\Test\ModelTesting\outputData\stateWiseData\Merged")
print(*files)

for file in files:
    dfs.append(pd.read_csv("BackEnd\Test\ModelTesting\outputData\stateWiseData\Merged\\" + file))
df = pd.concat(dfs, ignore_index=True)
df.to_csv("BackEnd\Test\ModelTesting\outputData\stateWiseData.csv", index=False)
