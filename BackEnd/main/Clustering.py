import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
import os
from utility import Utility as util

# merging at the same time while forming, to create a final combined file


class Clustering:      
    ##########################################################################################################
    ################################# Cluster Formation for row, column cobinations ##########################
    ##########################################################################################################       
    
    def formClusterSeparately():
        try:
            dirLoc = "DATA\\Test\\DistrictWiseData" # i/p file location

            problemList = ["Arunachal Pradesh.csv", "Chandigarh.csv", "Goa.csv",
                            "Ladakh.csv", "Lakshadweep.csv"]

            vars = ["prim_Girls", "prim_Boys", "prim_Overall", "upPrim_Girls", 
                    "upPrim_Boys", "upPrim_Overall", "snr_Girls", "snr_Boys", "snr_Overall"]
            cats = ["General", "SC", "ST", "OBC", "Overall"]

            if os.path.isdir(dirLoc):
                for fileName in os.listdir(dirLoc):
                    print("Working with : ", fileName)
                    if fileName not in problemList:
                        for i in range(len(vars)):
                            var = vars[i]
                            for j in range(len(cats)):
                                cat = cats[j]

                                df = pd.read_csv(dirLoc + "//" + fileName)

                                genData = df[df["Social Category"] == cat]
                                # print(genData.head())
                                data = genData[["DNo", var]]

                                df = pd.DataFrame(data)

                                # dataLinkage = linkage(newData.values.reshape(-1,1), "ward")
                                print(fileName)
                                print(data.head())
                                # df = pd.DataFrame(newData)

                                if len(data) > 10:    
                                    noOfClust = 5
                                elif len(data) < 10 and len(data) > 5:
                                    noOfClust = 3
                                else:
                                    noOfClust = 2
                                    
                                clustering = AgglomerativeClustering(n_clusters=noOfClust, linkage='ward')
                                clusters = clustering.fit_predict(data)
                                data[cat + "_" +var + "_" +'Cluster'] = clusters

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
    
    ##########################################################################################################
    ################################# Cluster Formation for row, column cobinations ##########################
    ##########################################################################################################
    
    def formCluster(self):
        util.serialNoAdd()
        self.formClusterSeparately(self)
        util.merge()
    
    def __init__(self):
        self.util = util()
#########################################################################################################

if __name__ == "__main__":
    folderPath = "BackEnd\Main\InputData\FilteredData"
    clst = Clustering()
    clst.formCluster()
