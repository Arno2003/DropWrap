import pandas as pd
from itertools import combinations
import os

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('BackEnd\Test\InputData\Gujarat1.csv')
output_dir = 'BackEnd\Test\InputData\FilteredData'


list1 = ['prim_Boys','prim_Girls','prim_Overall','upPrim_Boys','upPrim_Girls','upPrim_Overall','snr_Boys','snr_Girls','snr_Overall']
list2 = ['General', 'SC', 'ST','OBC','Overall']

# Loop through all combinations
for x in list1:
    for y in list2:
        # Filter the data based on the conditions
        filtered_data = data[(data["Social Category"] == y) & (data[x].notnull())]
        filtered_data = filtered_data.rename(columns={x: f"{y}_{x}"})[["Location", f"{y}_{x}", "Social Category"]]

        # Save the filtered data to a new CSV file
        filename = f"filtered_data({y}_{x}).csv"
        filepath = os.path.join(output_dir, filename)
        filtered_data.to_csv(filename, index=False)
       # print(f"Saved: {filename}")

print("Success")