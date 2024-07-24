import pandas as pd
import os

folder_path = "DATA\\Test\\DistrictWiseData"

res = []

for file in os.listdir(folder_path):
    file_path = folder_path+"\\"+file
    # print(file_path)
    df = pd.read_csv(file_path)
    df['State'] = os.path.splitext(file)[0]
    res.append(df)

merged_df = pd.concat(res, ignore_index=True)

# Save the merged dataframe to a new CSV file
merged_file_path = os.path.join('DATA\\Test', 'merged_output.csv')
merged_df.to_csv(merged_file_path, index=False)
