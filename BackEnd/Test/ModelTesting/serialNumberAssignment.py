import os
import pandas as pd

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
    df.to_csv(outPath+"\\SerialNoListDistricts", index=False)
    
addKeys()
assignKeys()
abbreviationsDist()
abbreviationsState()