import os
import pandas as pd


def preprocessLatLon(df):
    df = df.drop(df.columns[0], axis=1)
    df.rename(columns={'District': 'Location'}, inplace=True)

    for i, row in df.iterrows():
        lat = row[1].split()
        lon = row[2].split()
        lat1 = float(lat[0][0:2]+'.'+lat[1][0:-1])
        lon1 = float(lon[0][0:2]+'.'+lon[1][0:-1])

        df.at[i, 'Location'] = row[0].upper()
        df.at[i, 'Latitude'] = lat1
        df.at[i, 'Longitude'] = lon1

    return df


def mergeDF(latlon, rates, targetPath):
    # for i, rate in rates.iterrows():
    #     for j, latlon in latlon.iterrows():
    #         print(rate['Location'] == latlon['Location'])
    df_merged = pd.merge(latlon, rates, on='Location')
    df_merged.to_csv(targetPath)


latlon = pd.read_csv("BackEnd\\DATA\\latlong_dataset\\Andhra Pradesh.csv")
rates = pd.read_csv(
    "DATA\Test\DistrictWiseData\Andhra Pradesh.csv")

latlon = preprocessLatLon(df=latlon)

directory = "BackEnd\\database\\Andhra Pradesh"
os.makedirs(directory)

targetPath = directory+"\\Andhra Pradesh.csv"
mergeDF(latlon=latlon, rates=rates, targetPath=targetPath)
