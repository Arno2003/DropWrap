import pandas as pd
import os

input_dir = "BackEnd\\database\\States"


def computeStateData(df):
    df = df.drop(columns=['latitude', 'longitude'])
    df = df.rename(columns={'state_latitude': 'latitude',
                   'state_longitude': 'longitude'})

    grouped_df = df.groupby('Social Category').mean().reset_index()
    return grouped_df


for state_name in os.listdir(input_dir):
    input_path = input_dir+"\\"+state_name+"\\latlong.csv"
    output_path = input_dir+"\\"+state_name+"\\state_latlong.csv"
    df = pd.read_csv(input_path)

    final_df = computeStateData(df)
    final_df.to_csv(output_path)
    # print(input_path)


# test_path = "BackEnd\\database\\States\\Andhra_Pradesh\\latlong.csv"
# df = pd.read_csv(test_path)
#
