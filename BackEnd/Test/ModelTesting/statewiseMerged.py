import os
import pandas as pd

def merge_files_in_folder(folder_path, output_file):
    header_written = False
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    lines = infile.readlines()
                    if not header_written:
                        outfile.write(lines[0])  # Write header from the first file
                        header_written = True
                    outfile.writelines(lines[1:])  # Write the rest of the file

# Define the base directory path
base_dir = r"BackEnd\Test\ModelTesting\outputData\Andhra Pradesh"

# Initialize a dictionary to hold dataframes indexed by DNo
dno_data = {}

# Loop through each subdirectory in the base directory
for sub_dir in os.listdir(base_dir):
    sub_dir_path = os.path.join(base_dir, sub_dir)
    
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
                
                # Add the 'caste' column with the subdirectory name
                df['caste'] = sub_dir
                
                # Filter columns ending with 'Cluster' and keep 'DNo' and 'caste'
                cluster_columns = [col for col in df.columns if col.endswith('Cluster')]
                columns_to_keep = ['DNo', 'caste'] + cluster_columns
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
output_dir = r"BackEnd\Test\ModelTesting\outputData\Andhra Pradesh\Merged"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

for sub_dir, data in dno_data.items():
    # Check if there is any data to process
    if data:
        # Convert the dictionary to a dataframe
        merged_df = pd.DataFrame.from_dict(data, orient='index')

        # Reset the index to ensure DNo is a column
        merged_df.reset_index(drop=True, inplace=True)

        # Drop the prefix based on sub_dir from each column name (if it's a string)
        prefix_to_remove = f"{sub_dir}_"
        merged_df.columns = [col.replace(prefix_to_remove, '') if isinstance(col, str) else col for col in merged_df.columns]

        # Save the merged dataframe to a new CSV file in the output directory
        output_file = os.path.join(output_dir, f"{sub_dir}_merged.csv")
        merged_df.to_csv(output_file, index=False)

        print(f"Files in {sub_dir} merged into {output_file}")
        print("Success")
    else:
        print(f"No valid data found in {sub_dir}. Skipping.")

# Merge all files in the merged directory into a single output file
output_file_all = os.path.join(output_dir, 'output_file.csv')
merge_files_in_folder(output_dir, output_file_all)
print("Success: All merged files combined into output_file.csv")