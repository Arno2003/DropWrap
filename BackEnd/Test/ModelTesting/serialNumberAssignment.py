import os
import pandas as pd

def addKeys():
    # Specify the directory containing the CSV files
    directory_path = 'DATA\\Test\\Districtwise_filtered_data' # i/p path
    outPath = "DATA\\Test\\DistrictWiseData" # o/p path
    
    # List all files in the directory
    all_files = os.listdir(directory_path)

    # Filter out non-CSV files
    csv_files = [f for f in all_files if f.endswith('.csv')]

    serialNo = 100**len(str(len(all_files))) # for assigning serial numbers to states

    # Loop through each CSV file and read it using pandas
    for file in csv_files:
        file_path = os.path.join(directory_path, file)
        df = pd.read_csv(file_path)
        
        print(f'Read {file} successfully:')
        

        
        df.insert(0, "DNo", range(serialNo+1, serialNo+len(df)+1))
        df.to_csv(outPath+"\\"+f'{file.replace("_modified", "")}.csv', index=False)
        
        serialNo += 100
        
addKeys()
