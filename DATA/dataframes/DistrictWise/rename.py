import os
year = "2021-2022"
folder_path = "DATA/dataframes/DistrictWise/"+year
for filename in os.listdir(folder_path):
    # original_file_name = "Dropout Rate by Gender, Level of School Education and Social Category_State Name _Andaman & Nicobar Islands District - All District_22.xlsx"

    # print(filename)

    # Extract the desired part of the file name
    temp = filename.split('_')[-2]
    new_file_name = temp.split('   ')[0]+".csv"

    # # Rename the file
    os.rename("DATA/dataframes/DistrictWise/"+year+"/" +
              filename, "DATA/dataframes/DistrictWise/"+year+"/"+new_file_name)

    print(f'The file has been renamed to: {new_file_name}')
