import convertapi
from dotenv import load_dotenv
import os
load_dotenv()

convertapi.api_secret = os.getenv("API_SECRET")

folder_path = "DATA/dataframes/DistrictWise/2021-2022"


def convertToSV(folder_path):
    # Ensure the folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return

    # Iterate over all files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # print(f"{file_path}")
            convertapi.convert('csv', {
                'File': file_path
            }, from_format='xls').save_files(folder_path+'/CSVs')

# Specify the folder path


# Call the function to print file locations
convertToSV(folder_path)
