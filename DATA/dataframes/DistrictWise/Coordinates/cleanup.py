import pandas as pd
folder_path = "DATA/dataframes/DistrictWise/Coordinates"

df = pd.read_csv(folder_path+"/DistrictCd.csv")

print(df['District'].head(50))
df['District'] = df['District'].str.replace(' \*', '')
print(df['District'].head(50))
