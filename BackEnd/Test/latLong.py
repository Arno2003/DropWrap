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
    print(response)
    data = response.json()
    
    if 'features' in data and len(data['features']) > 0:
        coordinates = data['features'][0]['geometry']['coordinates']
        return coordinates[1], coordinates[0]  # Latitude, Longitude
    else:
        return None

# Read the CSV file
input_file = 'data1.csv'
output_file = 'op.csv'

df = pd.read_csv(input_file)

# Initialize empty lists to store latitude and longitude
latitudes = []
longitudes = []

# Iterate through each row and get location data
for index, row in df.iterrows():
    school_name = row['School Name']
    village_name = row['Village']
    district = row['District Name']
    state_name = 'Gujarat'
    pin_code = row['Pincode']

    # Construct the location string
    location = f"{school_name}, {village_name}, {district}, {state_name}, {pin_code}"

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

# Save the updated DataFrame to a new CSV file
df.to_csv(output_file, index=False)

print(f"Latitude and longitude data saved to {output_file}")
