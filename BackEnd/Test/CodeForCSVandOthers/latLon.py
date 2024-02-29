import pandas as pd
import requests

# Replace with your Geoapify API key
API_KEY = '13c00742ef784344aa1dc02d6b403008'

# Function to geocode a location using Geoapify API


def geocode_location(location):
    base_url = 'https://api.geoapify.com/v1/geocode/search'
    params = {
        'text': location,
        'apiKey': API_KEY,
    }
    print("***")
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if 'features' in data and data['features']:
            coordinates = data['features'][0]['geometry']['coordinates']
            print("++++",coordinates)
            return {
                'Latitude': coordinates[1],
                'Longitude': coordinates[0]
            }
        else:
            return {
                'Latitude': None,
                'Longitude': None
            }
    except Exception as e:
        print(f"Error geocoding {location}: {str(e)}")
        return {
            'Latitude': None,
            'Longitude': None
        }


# Read the CSV file with locations
input_file = 'locations.csv'
output_file = 'op.csv'

try:
    df = pd.read_csv(input_file)
    df[['Latitude', 'Longitude']] = df['Location'].apply(geocode_location).apply(pd.Series)
    df.to_csv(output_file, index=False)
    
    print(f"Geocoded data saved to {output_file}")
except Exception as e:
    print(f"Error reading or processing the CSV file: {str(e)}")
