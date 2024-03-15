import os
import pandas as pd
import csv

# Path to the folder containing CSV files
folder_path = "BackEnd\\Test\\OutputData\\filteredOutputs\\clusters"

# Initialize an empty dataframe to store combined data
combined_data = pd.DataFrame()

colNames = []

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        
        # Read the CSV file into a dataframe
        df = pd.read_csv(file_path)
        print()
        print(df.head)
        # Append the dataframe to combined_data
        combined_data = combined_data.append(df, ignore_index=True)
        
        # csv_reader = csv.DictReader(file_path)
        # # colNames.append(csv_reader[1])   # for storing the column names in a file
        # print(list(csv_reader)[1])
        
# Replacing empty location values with 'Unknown'
combined_data['Location'].fillna('Unknown', inplace=True)

# Grouping by Location and Caste and aggregating with NaN mean
combined_data_grouped = combined_data.groupby(['Location', 'Caste']).agg(lambda x: x.mean() if x.dtype=='float64' else ', '.join(x))

# Reordering columns to match the desired format
print(combined_data.head)
# combined_data_grouped = combined_data_grouped[['prim_Boys','prim_Girls','Overall_prim_Boys','upPrim_Boys','upPrim_Girls','upPrim_Overall','snr_Boys','snr_Girls','snr_Overall']]

# Writing the combined data to a new CSV file
combined_data_grouped.to_csv("combined_data.csv")

# Display the combined data
print(combined_data_grouped)
