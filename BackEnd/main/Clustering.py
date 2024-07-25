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
                    # if fileName not in problemList:
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
                                
                                
                                # # Dendrogram
                                # plt.figure(figsize=(50, 20))  # Adjust figsize to improve readability, might need tweaking
                                # plt.title("Dendrogram for " + var)
                                # dend = dendrogram(linkage(data.values, method="ward"), leaf_rotation=90)  # Rotate labels for better readability
                                # plt.xlabel("Districts")
                                # plt.ylabel("Distance")
                                # plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
                                # plt.savefig(dirPath + "\\" + var + "_Dendrogram.png", dpi=600)
                                # plt.close() 
        except Exception as e:
            print(e)
    
    ##########################################################################################################
    ################################# Cluster Formation for row, column cobinations ##########################
    ##########################################################################################################
    
    def formCluster():
        util.serialNoAdd()
        Clustering.formClusterSeparately()
        util.merge()
        
    def prepareStateData():
        import pandas as pd
        import glob

        # Directory containing your CSV files
        csv_dir = "DATA\\Test\\DistrictWiseData\\*.csv"

        # Get a list of all CSV files in the directory
        csv_files = glob.glob(csv_dir)

        # Initialize an empty DataFrame to store the final results
        final_df = pd.DataFrame()

        # Iterate through each CSV file
        for file in csv_files:
            # Read the CSV file
            df = pd.read_csv(file)
            
            # Calculate the mean of each column
            mean_df = df.mean().to_frame().T
            
            # Get the state name from the file name (assuming the file name is the state name)
            state_name = file.replace("DATA\\Test\\DistrictWiseData\\", "").replace(".csv", "") # Adjust based on your file path format
            
            # Add the state name as a new column
            mean_df['Location'] = state_name
            
            # Append the mean DataFrame to the final DataFrame
            final_df = pd.concat([final_df, mean_df], ignore_index=True)

        # Rearrange columns to have 'State' as the first column
        cols = final_df.columns.tolist()
        cols = [cols[-1]] + cols[:-1]
        final_df = final_df[cols]

        # Save the final DataFrame to a new CSV file
        final_df.to_csv('DATA\\Test\\stateWiseData\\stateWiseData.csv', index=False)

        # print("Final CSV file created successfully.")

    def formClusterStateWise():
        Clustering.prepareStateData()
        util.merge()
    
    def formClusterWhole():
        try:
            dirLoc = "DATA\\Test\\DistrictWiseData" # i/p file location

            vars = ["prim_Girls", "prim_Boys", "prim_Overall", "upPrim_Girls", 
                    "upPrim_Boys", "upPrim_Overall", "snr_Girls", "snr_Boys", "snr_Overall"]
            cats = ["General", "SC", "ST", "OBC", "Overall"]

            if os.path.isdir(dirLoc):
                for fileName in os.listdir(dirLoc):
                    print("Working with : ", fileName)
                    # if fileName not in problemList:
                    if fileName == "IndiaDistricts.csv":
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
                                
                                
                                # # Dendrogram
                                # plt.figure(figsize=(50, 20))  # Adjust figsize to improve readability, might need tweaking
                                # plt.title("Dendrogram for " + var)
                                # dend = dendrogram(linkage(data.values, method="ward"), leaf_rotation=90)  # Rotate labels for better readability
                                # plt.xlabel("Districts")
                                # plt.ylabel("Distance")
                                # plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
                                # plt.savefig(dirPath + "\\" + var + "_Dendrogram.png", dpi=600)
                                # plt.close() 
        except Exception as e:
            print(e)
    
    def __init__(self):
        self.util = util()
#########################################################################################################

if __name__ == "__main__":
    folderPath = "BackEnd\Main\InputData\FilteredData"
    clst = Clustering()
    clst.formCluster()
    clst.formClusterWhole()
