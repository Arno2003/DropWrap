from sklearn.cluster import AgglomerativeClustering
import pandas as pd
# import seaborn as sns
import os

def formClusterSeparately():
    try:
        dirLoc = "DATA\\Test\\DistrictWiseData" # i/p file location

        vars = ["prim_Girls", "prim_Boys", "prim_Overall", "upPrim_Girls", "upPrim_Boys", "upPrim_Overall", "snr_Girls", "snr_Boys", "snr_Overall"]
        cats = ["General", "SC", "ST", "OBC", "Overall"]

        if os.path.isdir(dirLoc):
            for fileName in os.listdir(dirLoc):  
                for i in range(len(vars)):
                    var = vars[i]
                    for j in range(len(cats)):
                        cat = cats[j]

                        df = pd.read_csv(dirLoc + "//" + fileName)

                        # colName = var
                        # locations = df['DNo']
                        # caste = df['Social Category']

                        genData = df[df["Social Category"] == cat]
                        print(genData.head())
                        data = genData[["DNo", var]]

                        df = pd.DataFrame(data)
                        # df['serialNumber'] = list(range(1, len(df)+1))
                        # newData = df[[var, "serialNumber"]]

                        # dataLinkage = linkage(newData.values.reshape(-1,1), "ward")

                        # df = pd.DataFrame(newData)
                        clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
                        clusters = clustering.fit_predict(genData)
                        data['Cluster'] = clusters

                        dirPath = "BackEnd\\Test\\ModelTesting\\outputData\\" + fileName.replace(".csv", "")
                        if not os.path.exists(dirPath):
                            os.mkdir(path=dirPath)
                        
                        dirPath += "\\" + cat

                        if not os.path.exists(dirPath):
                            os.mkdir(path=dirPath)

                        filePath = dirPath + "\\"  + var + ".csv"


                        if os.path.exists(filePath):
                            os.remove(filePath)
                            # newData.to_csv(filePath)
                        data.to_csv(filePath)
    except Exception as e:
        print(e)
        
formClusterSeparately()