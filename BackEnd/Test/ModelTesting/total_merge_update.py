import os
import pandas as pd

# Base directory containing state directories
base_dir = "BackEnd\\Test\\ModelTesting\\outputData"

# List to store DataFrames
dataframes = []

# Iterate through each state directory
for state_dir in os.listdir(base_dir):
    state_path = os.path.join(base_dir, state_dir)
    if os.path.isdir(state_path):
        # Iterate through each category directory within the state directory
        for categoryDir in ["General", "SC", "ST", "Overall", "OBC"]:
            subPath = os.path.join(state_path, categoryDir)
            if os.path.isdir(subPath):
                # Iterate through each CSV file in the category directory
                for csv_file in os.listdir(subPath):
                    if csv_file.endswith('.csv'):
                        file_path = os.path.join(subPath, csv_file)
                        
                        # Read the CSV file into a DataFrame
                        df = pd.read_csv(file_path)
                        df['Category'] = categoryDir
                        
                        # Append the DataFrame to the list
                        dataframes.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(dataframes, ignore_index=True)

# Saving the merged DataFrame
merged_df.to_csv('merged_output.csv', index=False)

print("Merged file saved as 'merged_output.csv'")
