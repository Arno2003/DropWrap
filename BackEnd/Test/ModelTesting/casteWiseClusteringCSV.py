from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import seaborn as sns
import os

try:
    dirLoc = "DATA\\Test\\DistrictWiseData"

    vars = ["prim_Girls", "prim_Boys", "prim_Overall", "upPrim_Girls", "upPrim_Boys", "upPrim_Overall", "snr_Girls", "snr_Boys", "snr_Overall"]
    cats = ["General", "SC", "ST", "OBC", "Overall"]

    if os.path.isdir(dirLoc):
        for fileName in os.listdir(dirLoc):  
            state = fileName
            for i in range(len(vars)):
                var = vars[i]
                for j in range(len(cats)):
                    cat = cats[j]

                    file = state
                    df = pd.read_csv(file)

                    colName = var
                    locations = df['Location']
                    caste = df['Social Category']

                    genData = df[df["Social Category"] == cat]
                    data = genData[["Location", var]]

                    df = pd.DataFrame(data)
                    df['serialNumber'] = list(range(1, len(df)+1))
                    newData = df[[var, "serialNumber"]]

                    # dataLinkage = linkage(newData.values.reshape(-1,1), "ward")

                    df = pd.DataFrame(newData)
                    clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
                    clusters = clustering.fit_predict(df)
                    newData['Cluster'] = clusters

                    dirPath = "D:\\projects\\DropWrap\\BackEnd\\Test\\ModelTesting\\outputData\\" + state + "\\" + cat

                    if  not os.path.exists(dirPath):
                        os.mkdir(path=dirPath)

                    filePath = dirPath + "\\"  + "\\" + var + ".csv"


                    if os.path.exists(filePath):
                        os.remove(filePath)
                        # newData.to_csv(filePath)
                    newData.to_csv(filePath)
except Exception as e:
    print(e)