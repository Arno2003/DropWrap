import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
import os
from Utility import Utility as util

# merging at the same time while forming, to create a final combined file


class Clustering:
    ##########################################################################################################
    ################################# Cluster Formation for row, column cobinations ##########################
    ##########################################################################################################       
    
    def formClusterSeparately(dirLoc):
        try:
            dirLoc = "DATA\\Test\\DistrictWiseData" # i/p file location

            problemList = ["Arunachal Pradesh.csv", "Chandigarh.csv", "Goa.csv",
                           "Ladakh.csv", "Lakshadweep.csv"]

            vars = ["prim_Girls", "prim_Boys", "prim_Overall", "upPrim_Girls", 
                    "upPrim_Boys", "upPrim_Overall", "snr_Girls", "snr_Boys", "snr_Overall"]
            cats = ["General", "SC", "ST", "OBC", "Overall"]

            if os.path.isdir(dirLoc):
                if dirLoc == "DATA\\Test\\StateWiseData":
                    print("StateWiseData")
                    for i in range(len(vars)):
                            var = vars[i]
                            for j in range(len(cats)):
                                cat = cats[j]

                                df = pd.read_csv("DATA\\Test\\stateWiseData\\stateWiseData.csv")

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

                                filePath = dirPath + "\\stateWise.csv"


                                if os.path.exists(filePath):
                                    os.remove(filePath)
                                    # newData.to_csv(filePath)
                                data.to_csv(filePath)
                    
                else:    
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
    
    ############################## for preparing state wise data ###########################################
    def prepareStateData():
        import glob

        # Directory containing your CSV files
        csv_dir = "DATA\\Test\\DistrictWiseData"
        # Get a list of all CSV files in the directory
        csv_files = glob.glob(os.path.join(csv_dir, "*.csv"))

        # Initialize an empty list to store each processed DataFrame
        dataframes = []
        problemList = ["Arunachal Pradesh.csv", "Chandigarh.csv", "Goa.csv",
                           "Ladakh.csv", "Lakshadweep.csv"]
    
        # Check if there are any CSV files found
        if not csv_files:
            print("No CSV files found in the specified directory.")
        else:                 
            # Iterate through each CSV file
            for file in csv_files:
                print(f"Processing file: {file}")

                # Read the CSV file
                try:
                    df = pd.read_csv(file)
                except Exception as e:
                    print(f"Error reading {file}: {e}")
                    continue

                # Get the state name from the file name (assuming the file name is the state name)
                state_name = file.replace("DATA\\Test\\DistrictWiseData\\", "").replace(".csv", "") # Adjust based on your file path format
                print(f"State name: {state_name}")

                # Check if the DataFrame has the expected columns
                if 'Social Category' not in df.columns:
                    print(f"'Social Category' column not found in {file}. Skipping this file.")
                    continue

                # Group by 'Social Category' and calculate the mean of each group
                grouped_df = df.groupby('Social Category').mean().reset_index()

                # Add the state name as a new column
                grouped_df['Location'] = state_name
                
                grouped_df.drop(columns=['DNo'], inplace=True)
                            
                # Append the grouped DataFrame to the list
                dataframes.append(grouped_df)

            # Concatenate all DataFrames in the list into a final DataFrame
            if dataframes:
                final_df = pd.concat(dataframes, ignore_index=True)

                # Rearrange columns to have 'State' and 'Social Category' as the first columns
                cols = ['Location', 'Social Category'] + [col for col in final_df.columns if col not in ['Location', 'Social Category']]
                final_df = final_df[cols]

                # Save the final DataFrame to a new CSV file
                mapped_df = pd.read_csv("DATA\\Test\\Abbreviations\\stateDNoMapping.csv")
                mapped_df['startingDNo'] = mapped_df['startingDNo'].apply(lambda x: int(str(x)[:3]))

                merged_df = pd.merge(final_df, mapped_df[['Location', 'startingDNo']], on='Location', how='left')

                
                final_df["DNo"] = merged_df["startingDNo"]
                
                final_df = final_df[final_df["DNo"].notnull()]

                
                final_df.to_csv('DATA\\Test\\stateWiseData\\stateWiseData.csv', index=False)
                print("Final CSV file with Social Category created successfully.")
            else:
                print("No valid dataframes were created from the CSV files.")


    def formClusterWhole(filePath, fileName):
        df = pd.read_csv(filePath)
        problemList = ["Arunachal Pradesh.csv", "Chandigarh.csv", "Goa.csv",
                           "Ladakh.csv", "Lakshadweep.csv"]

        vars = ["prim_Girls", "prim_Boys", "prim_Overall", "upPrim_Girls", 
                "upPrim_Boys", "upPrim_Overall", "snr_Girls", "snr_Boys", "snr_Overall"]
        
        cats = ["General", "SC", "ST", "OBC", "Overall"]
        
        for var in vars:
            for cat in cats:
                # Filter the data for Social Category = Overall
                df_filtered = df[df['Social Category'] == cat]

                data = df_filtered[['DNo', var]]

                # Perform hierarchical/agglomerative clustering
                linked = linkage(data, method='ward')
                
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


    def formClusterStateWise():
        # Directory containing the CSV files
        directory = 'BackEnd\Test\ModelTesting\outputData\states\Merged'

        # List of CSV files
        # files = ['General_merged.csv', 'OBC_merged.csv', 'Overall_merged.csv', 'SC_merged.csv', 'ST_merged.csv']
        files = os.listdir(directory)
        
        # Initialize an empty DataFrame for the merge
        merged_df = None

        # Iterate over the list of files and merge them on 'DNo'
        for file in files:
            file_path = os.path.join(directory, file)
            df = pd.read_csv(file_path)
            if merged_df is None:
                merged_df = df
            else:
                # merged_df = pd.merge(merged_df, df, on='DNo', how='outer')
                df = df.drop(columns=['DNo'])
                merged_df = pd.concat([merged_df, df], axis=1)

        # Save the merged DataFrame to a new CSV file
        output_file_path = 'BackEnd\Test\ModelTesting\outputData\states.csv'
        # merged_df = merged_df.loc[:, ~merged_df.columns.duplicated()]
        merged_df.to_csv(output_file_path, index=False)

        print("Files merged successfully.")

    ##########################################################################################################
    ################################# Cluster Formation for row, column cobinations ##########################
    ##########################################################################################################
    
    def formCluster(dirLoc):
        # util.serialNoAdd()
        Clustering.formClusterSeparately(dirLoc)
        util.merge()
    
    
    def __init__(self):
        self.util = util()
#########################################################################################################
# End of Clustering.py