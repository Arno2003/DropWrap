import os
import pandas as pd

# Define the base directory path
base_dir = r"BackEnd\Test\ModelTesting\outputData\Andhra Pradesh"

# Loop through each subdirectory in the base directory
for sub_dir in os.listdir(base_dir):
    sub_dir_path = os.path.join(base_dir, sub_dir)
    
    # Check if it is a directory
    if os.path.isdir(sub_dir_path):
        # Initialize a dictionary to hold dataframes indexed by DNo
        dno_data = {}

        # Loop through each file in the subdirectory
        for file_name in os.listdir(sub_dir_path):
            if file_name.endswith(".csv"):
                file_path = os.path.join(sub_dir_path, file_name)
                
                # Read the CSV file into a dataframe
                df = pd.read_csv(file_path)
                
                # Add the 'caste' column with the subdirectory name
                df['caste'] = sub_dir
                
                # Filter columns ending with 'Cluster' and keep 'DNo' and 'caste'
                cluster_columns = [col for col in df.columns if col.endswith('Cluster')]
                columns_to_keep = ['DNo', 'caste'] + cluster_columns
                df = df[columns_to_keep]
                
                # Merge data for each DNo
                for _, row in df.iterrows():
                    dno = row['DNo']
                    if dno not in dno_data:
                        dno_data[dno] = row
                    else:
                        # Combine the rows with existing data
                        for col in cluster_columns:
                            if col in row and not pd.isna(row[col]):
                                dno_data[dno][col] = row[col]

        # Convert the dictionary to a dataframe
        merged_df = pd.DataFrame.from_dict(dno_data, orient='index')

        # Reset the index to ensure DNo is a column
        merged_df.reset_index(drop=True, inplace=True)

        # Drop the prefix based on sub_dir from each column name
        prefix_to_remove = f"{sub_dir}_"
        merged_df.columns = merged_df.columns.str.replace(prefix_to_remove, '', regex=False)

        # Save the merged dataframe to a new CSV file
        output_file = os.path.join(sub_dir_path, f"{sub_dir}_merged.csv")
        merged_df.to_csv(output_file, index=False)

        print(f"Files in {sub_dir} merged into {output_file}")
        print("Success")
