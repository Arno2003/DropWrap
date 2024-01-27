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

# Read the CSV file
input_file = 'BackEnd\Test\Gujarat.csv'
output_file = 'BackEnd\Test\latlong.csv'

df = pd.read_csv(input_file)
print(df)

# Initialize empty lists to store latitude and longitude
latitudes = []
longitudes = []

# Iterate through each row and get location data
for index, row in df.iterrows():
    # Construct the location string
    location = row['Location'] + ", Gujarat"

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
