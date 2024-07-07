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
    print(df)

    # Initialize empty lists to store latitude and longitude
    latitudes = []
    longitudes = []

    # Iterate through each row and get location data
    for index, row in df.iterrows():
        # Construct the location string
        location = row['Location'] + f", {state}"

        # Get latitude and longitude using Geoapify API
        coordinates = get_lat_lng(location)

        if coordinates:
            latitudes.append(coordinates[0])
            longitudes.append(coordinates[1])
        else:
            latitudes.append(None)
            longitudes.append(None)

    # Add latitude and longitude columns to the DataFrame
    df['latitude'] = latitudes
    df['longitude'] = longitudes
    for index, rows in df.iterrows():
        if index != 'latitude' or index != 'longitude':
            df.pop(index)
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    print(f"Latitude and longitude data saved to {output_file}")


# Specify the path to the folder containing CSV files
folder_path = 'DATA/dataframes/DistrictWise/2020-2021'

# Iterate through all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        state = filename
        input_file = os.path.join(folder_path, filename)
        output_file = 'BackEnd\Test\latlong.csv'
        convert(input_file, output_file, state)

        # # Open and read the CSV file
        # with open(file_path, 'r') as csv_file:
        #     reader = csv.reader(csv_file)
        #
        #     # Process the data as needed
        #     for row in reader:
        #         print(row)  # Replace this with your desired processing logic
