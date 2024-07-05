import pandas as pd


def preprocess(df):
    df = df.drop(df.columns[0], axis=1)
    for i, row in df.iterrows():
        lat = row[1].split()
        lon = row[2].split()
        lat1 = float(lat[0][0:2]+'.'+lat[1][0:-1])
        lon1 = float(lon[0][0:2]+'.'+lon[1][0:-1])

        df.at[i, 'Latitude'] = lat1
        df.at[i, 'Longitude'] = lon1

    print(df.head())


df = pd.read_csv("BackEnd\\DATA\\latlong_dataset\\Andhrapradesh.csv")

preprocess(df=df)
