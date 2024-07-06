import os
import csv
import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Geoapify API key
API_KEY = '13c00742ef784344aa1dc02d6b403008'
GEOAPIFY_ENDPOINT = 'https://api.geoapify.com/v1/geocode/autocomplete'

# Function to get latitude and longitude for a given location


def get_lat_lng(location):
    params = {
        'text': location,
        'apiKey': API_KEY,
    }
    response = requests.get(GEOAPIFY_ENDPOINT, params=params)
    data = response.json()
    if 'features' in data and len(data['features']) > 0:
        coordinates = data['features'][0]['geometry']['coordinates']
        return coordinates[1], coordinates[0]  # Latitude, Longitude
    else:
        return None


def convert(input_file, output_file, state):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Initialize empty lists to store latitude and longitude
    latitudes = []
    longitudes = []

    # print(df.head())

    # Iterate through each row and get location data
    for index, row in df.iterrows():
        try:
            # Construct the location string
            location = row['Location'] + f", {state}, India"
            # print(location)

            # Get latitude and longitude using Geoapify API
            coordinates = get_lat_lng(location)
            print(row['Location'], coordinates)
            if coordinates:
                latitudes.append(coordinates[0])
                longitudes.append(coordinates[1])
            else:
                latitudes.append(None)
                longitudes.append(None)
        except:
            print("Exception")
            # Add latitude and longitude columns to the DataFrame
    df['latitude'] = latitudes
    df['longitude'] = longitudes

    # print(df.head())
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Latitude and longitude data saved to {output_file}")


# Specify the path to the folder containing CSV files
folder_path = 'DATA\\Test\\DistrictWiseData'
# output_file = 'DATA\CoordinateScraping\Geocode\latlongNew.csv'
# convert(folder_path, output_file, 'Lakshadweep')

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        state = filename.split('.')[0]
        # print(state)
        # input_file = os.path.join(folder_path, filename)
        input_file = os.path.join(folder_path, filename)
        op_dir = f"BackEnd\\database\\{state}"

        if not os.path.isdir(op_dir):
            os.makedirs(op_dir)

        output_file = op_dir+'\\latlong.csv'
        # print(output_file)
        convert(input_file, output_file, state)

        print(f"#################COMPLETED {state}####################")

# # Open and read the CSV file
# with open(file_path, 'r') as csv_file:
#     reader = csv.reader(csv_file)
#
#     # Process the data as needed
#     for row in reader:
#         print(row)  # Replace this with your desired processing logic
