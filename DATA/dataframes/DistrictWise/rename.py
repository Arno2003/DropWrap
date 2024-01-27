import os
import pandas as pd
year = "2021-2022"
folder_path = "DATA/dataframes/DistrictWise/"+year
# for filename in os.listdir(folder_path):
#     temp = filename.split('_')[-2]

#     new_file_name = temp.split('   ')[0]+".xlsx"

#     # # Rename the file
#     os.rename("DATA/dataframes/DistrictWise/"+year+"/" +
#               filename, "DATA/dataframes/DistrictWise/"+year+"/"+new_file_name)

#     print(f'The file has been renamed to: {new_file_name}')

for filename in os.listdir(folder_path):
    df = pd.read_excel(folder_path+"/Gujarat.xlsx")
    print(df)
    # df.to_csv("DATA/dataframes/DistrictWise/"+year+"/Gujarat")
