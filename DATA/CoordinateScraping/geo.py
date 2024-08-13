import os
import csv
import requests
import pandas as pd

# Replace 'YOUR_API_KEY' with your actual Geoapify API key
API_KEY = '13c00742ef784344aa1dc02d6b403008'
GEOAPIFY_ENDPOINT = 'https://api.geoapify.com/v1/geocode/autocomplete'

input_dir = "..\\..\\BackEnd\\database\\States"

# Function to get latitude and longitude for a given location
problemList = ["Arunachal_Pradesh",
               "Chandigarh", "Goa", "Ladakh", "Lakshadweep"]


def computeStateData(df, state_name):
    df = df.drop(columns=['latitude', 'longitude'])
    df = df.rename(columns={'state_latitude': 'latitude',
                   'state_longitude': 'longitude'})

    grouped_df = df.groupby('Social Category').mean().reset_index()
    grouped_df['Location'] = state_name
    return grouped_df


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

    latitudesSt = []
    longitudesSt = []

    # print(df.head())

    # Iterate through each row and get location data
    for index, row in df.iterrows():
        try:
            # Construct the location string
            location = row['Location'] + f", {state}, India"

            # Get latitude and longitude using Geoapify API
            coordinates = get_lat_lng(location)
            stCoordinates = get_lat_lng(f"{state}, India")
            print(row['Location'], coordinates)
            if coordinates:
                latitudes.append(coordinates[0])
                longitudes.append(coordinates[1])

                latitudesSt.append(stCoordinates[0])
                longitudesSt.append(stCoordinates[1])
            else:
                latitudes.append(None)
                longitudes.append(None)

                latitudesSt.append(None)
                longitudesSt.append(None)
        except:
            print("Exception")
            latitudes.append(None)
            longitudes.append(None)
            latitudesSt.append(None)
            longitudesSt.append(None)

    # Check lengths of the lists and DataFrame
    if len(latitudes) != len(df):
        print(
            f"Length mismatch: DataFrame({len(df)}), Latitudes({len(latitudes)})")
        # Adjust lengths if needed
        min_length = min(len(df), len(latitudes))
        df = df.iloc[:min_length]
        latitudes = latitudes[:min_length]
        longitudes = longitudes[:min_length]
        latitudesSt = latitudesSt[:min_length]
        longitudesSt = longitudesSt[:min_length]

    # Add latitude and longitude columns to the DataFrame
    df['latitude'] = latitudes
    df['longitude'] = longitudes

    df['state_latitude'] = latitudesSt
    df['state_longitude'] = longitudesSt

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
        if state not in ['IndiaDistricts', 'stateWiseData']:
            input_file = os.path.join(folder_path, filename)
            input_file = os.path.join(folder_path, filename)

            stateName = "_".join(state.split())

            if stateName not in problemList:
                op_dir = f"..\\..\\BackEnd\\database\\States\\{stateName}"

                if not os.path.isdir(op_dir):
                    os.makedirs(op_dir)

                output_file = op_dir+'\\latlong.csv'
                print(output_file)
                convert(input_file, output_file, state)

                print(
                    f"#################COMPLETED {state}####################")


for state_name in os.listdir(input_dir):
    input_path = input_dir+"\\"+state_name+"\\latlong.csv"
    output_path = input_dir+"\\"+state_name+"\\state_latlong.csv"
    df = pd.read_csv(input_path)

    final_df = computeStateData(df, ' '.join(state_name.split('_')))
    print(final_df.head())
    final_df.to_csv(output_path)
