import os
import pandas as pd
year = "2021-2022"
folder_path = "DATA/dataframes/DistrictWise/"+year
for filename in os.listdir(folder_path):
    temp = filename.split('_')[-2]

    new_file_name = temp.split('   ')[0]+".xlsx"

    os.rename("DATA/dataframes/DistrictWise/"+year+"/" +
              filename, "DATA/dataframes/DistrictWise/"+year+"/"+new_file_name)

    print(f'The file has been renamed to: {new_file_name}')
