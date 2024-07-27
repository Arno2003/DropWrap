import pandas as pd
import os

class Utility:    
    #############################################################################################
    ######################## Adding key values (DNo) to all districts ###########################
    #############################################################################################
    def addKeys():
        # Specify the directory containing the CSV files
        directory_path = 'DATA\\Test\\Districtwise_filtered_data' # i/p path 
        # directory_path1 = "DATA\\Test\\Abbreviations" # i/p path 
        
        # outPath = "DATA\\Test\\DistrictWiseData" # o/p path 
        outPath = "DATA\\Test\\Abbreviations\\Districts" # o/p path 
        
        # List all files in the directory
        all_files = os.listdir(directory_path)

        # Filter out non-CSV files
        csv_files = [f for f in all_files if f.endswith('.csv')]

        serialNo = 100**len(str(len(all_files))) # for assigning serial numbers to states

        # Loop through each CSV file and read it using pandas
        for file in csv_files:
            file_path = os.path.join(directory_path, file)
            df = pd.read_csv(file_path)
            df1 = df.copy()
            
            print(f'Read {file} successfully:')
            df['DNo'] = df.groupby('Location').ngroup() + 1 + serialNo 
            # df.insert(0, "DNo", range(serialNo+1, serialNo+len(df)+1))
            df = df[["DNo", "Location"]]
            print(df.head)
            serialNo += 100
            
            serial_number_column = df.pop('DNo')
            df.insert(0, 'DNo', serial_number_column)
            df = df.drop_duplicates()
            df.to_csv(outPath+"\\"+f'{file.replace("_modified", "")}', index=False)


    #############################################################################################
    ######################## Assigning key values (DNo) to all districts ########################
    #############################################################################################


    def assignKeys():
        directory_path = 'DATA\\Test\\Districtwise_filtered_data' # i/p path all files 
        directory_path1 = "DATA\\Test\\Abbreviations\\Districts" # i/p path DNo
        outPath = "DATA\\Test\\DistrictWiseData" # o/p path 
        
        # List all files in the directory
        all_files = os.listdir(directory_path)

        # Filter out non-CSV files
        csv_files = [f for f in all_files if f.endswith('.csv')]
        
        # Loop through each CSV file and read it using pandas
        for file in csv_files:
            file_path = os.path.join(directory_path, file)
            file_path1 = os.path.join(directory_path1, file.replace("_modified", ""))
            df = pd.read_csv(file_path)
            df1 = pd.read_csv(file_path1)
                
            print(df.head)
            print(df1.head)
            
            # print(f'Read {file} successfully:')
            mergedDF = pd.merge(df, df1, on='Location')
            print(mergedDF)
            mergedDF = mergedDF.drop_duplicates()
            mergedDF.to_csv(outPath+"\\"+f'{file.replace("_modified", "")}', index=False)



    #############################################################################################
    ######################## Combining Abbreviations of all districts ###########################
    #############################################################################################      
    def abbreviationsDist():
        # Specify the directory containing the CSV files
        directory_path = 'DATA\\Test\\DistrictWiseData' # i/p path
        outPath = "DATA\\Test\\Abbreviations" # o/p path
        
        # List all files in the directory
        all_files = os.listdir(directory_path)

        # Filter out non-CSV files
        dataframes = []
        
        # Loop through each CSV file and read it using pandas
        for file in all_files:
            file_path = os.path.join(directory_path, file)
            df = pd.read_csv(file_path)
            dataframes.append(df)

        # Concatenate all dataframes into a single dataframe
        combined_df = pd.concat(dataframes, ignore_index=True)
        df = combined_df.copy()[["DNo", "Location"]]

        # Save the combined dataframe to a new CSV file
        df = df.drop_duplicates()
        df.to_csv(outPath+"\\SerialNoListDistricts", index=False)



    #############################################################################################
    ######################## Adding key values (DNo) to all STATES ##############################
    #############################################################################################

    def abbreviationsState():
        # Specify the directory containing the CSV files
        directory_path = 'DATA\\Test\\DistrictWiseData' # i/p path
        outPath = "DATA\\Test\\Abbreviations" # o/p path
        
        # List all files in the directory
        all_files = os.listdir(directory_path)

        # Filter out non-CSV files
        dataframes = []
        
        # Loop through each CSV file and read it using pandas
        for file in all_files:
            file_path = os.path.join(directory_path, file)
            df = pd.read_csv(file_path)
            dataframes.append(df)

        # Concatenate all dataframes into a single dataframe
        combined_df = pd.concat(dataframes, ignore_index=True)
        df = combined_df.copy()[["DNo", "Location"]]

        # Save the combined dataframe to a new CSV file
        df = df.drop_duplicates()
        df.to_csv(outPath+"\\SerialNoListDistricts.csv", index=False)
        
    ############################# main calling function for srl no. assignment ##########################
    
    def serialNoAdd():
        Utility.addKeys()
        Utility.assignKeys()
        Utility.abbreviationsDist()
        Utility.abbreviationsState()

    #####################################################################################################


    #############################################################################################
    ######################## for merging cluster.csv file data ##################################
    #############################################################################################
    def process_subfolder(base_dir, subfolder_name):
        subfolder_path = os.path.join(base_dir, subfolder_name)
        
        # Initialize a dictionary to hold dataframes indexed by DNo
        dno_data = {}

        # Loop through each subdirectory in the base directory
        for sub_dir in os.listdir(subfolder_path):
            sub_dir_path = os.path.join(subfolder_path, sub_dir)
            
            # Check if it is a directory
            if os.path.isdir(sub_dir_path):
                # Initialize a dictionary to hold dataframes indexed by DNo for each subdirectory
                dno_data[sub_dir] = {}

                # Loop through each file in the subdirectory
                for file_name in os.listdir(sub_dir_path):
                    file_path = os.path.join(sub_dir_path, file_name)
                    
                    # Check if the file is a CSV file and not empty
                    if file_name.endswith(".csv") and os.path.getsize(file_path) > 0:
                        # Read the CSV file into a dataframe
                        df = pd.read_csv(file_path)
                        
                        # Add the 'Social Category' column with the subdirectory name
                        df['Social Category'] = sub_dir
                        
                        # Filter columns ending with 'Cluster' and keep 'DNo' and 'Social Category'
                        cluster_columns = [col for col in df.columns if col.endswith('Cluster')]
                        columns_to_keep = ['DNo', 'Social Category'] + cluster_columns
                        df = df[columns_to_keep]
                        
                        # Merge data for each DNo
                        for _, row in df.iterrows():
                            dno = row['DNo']
                            if dno not in dno_data[sub_dir]:
                                dno_data[sub_dir][dno] = row
                            else:
                                # Combine the rows with existing data
                                for col in cluster_columns:
                                    if col in row and not pd.isna(row[col]):
                                        dno_data[sub_dir][dno][col] = row[col]

        # Iterate over each subdirectory's data and save each merged DataFrame separately
        output_dir = os.path.join(subfolder_path, "Merged")

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        dfList = [] # for storing data frames to be merged
        for sub_dir, data in dno_data.items():
            # Check if there is any data to process
            if sub_dir != "Merged":
                if data:
                    # Convert the dictionary to a dataframe
                    merged_df = pd.DataFrame.from_dict(data, orient='index')

                    # Reset the index to ensure DNo is a column
                    merged_df.reset_index(drop=True, inplace=True)

                    # Drop the prefix based on sub_dir from each column name (if it's a string)
                    prefix_to_remove = f"{sub_dir}_"
                    merged_df.columns = [col.replace(prefix_to_remove, '') if isinstance(col, str) else col for col in merged_df.columns]
                    
                    merged_df.columns = [col.replace('_Cluster', '') for col in merged_df.columns]

                    # Save the merged dataframe to a new CSV file in the output directory
                    output_file = os.path.join(output_dir, f"{sub_dir}_merged.csv")
                    merged_df.to_csv(output_file, index=False)
                    
                    dfList.append(merged_df)

                    print(f"Files in {sub_dir} merged into {output_file}")
                else:
                    print(f"No valid data found in {sub_dir}. Skipping.")

        # output directory for storing cluster data
        # output_file_all = f"BackEnd\database\{subfolder_name}\cluster.csv"
        output_file_all = f"BackEnd\\Test\\ModelTesting\\outputData\\{subfolder_name}.csv"
        
        # merging all the clusters into a single file
        df = pd.concat(dfList)
        
        extraCols = ['prim', 'snr', 'upPrim']
        for col in extraCols:
            df.drop(col, axis=1, inplace=True)
        
        df.to_csv(output_file_all)
        print(f"Success: All merged files combined into {output_file_all}")

        
    def mergeFiles(dirPath):
        for subfolder in os.listdir(dirPath):
            subfolder_path = os.path.join(dirPath, subfolder)
            
            # Check if it is a directory
            if os.path.isdir(subfolder_path):
                Utility.process_subfolder(dirPath, subfolder)
    
    def mergeFilesWhole():
        dirPath = "BackEnd\\Test\\ModelTesting\\outputData\\IndiaDistricts"
        for subfolder in os.listdir(dirPath):
            subfolder_path = os.path.join(dirPath, subfolder)
            
            # Check if it is a directory
            if os.path.isdir(subfolder_path):
                Utility.process_subfolder(dirPath, subfolder)
    
    #################################### main calling function ##########################################
    def merge(dirPath="BackEnd\\Test\\ModelTesting\\outputData"):
        # dirPath = "BackEnd\\Test\\ModelTesting\\outputData"
        Utility.mergeFiles(dirPath)
    
    def mergeStateFiles():
        Utility.mergeFiles("BackEnd\Test\ModelTesting\outputData\states")
        
        

    