import pandas as pd
import os

path = "DATA\\Test\\DistrictWiseData"
problemList = ["Arunachal Pradesh.csv", "Chandigarh.csv", "Goa.csv",
                "Ladakh.csv", "Lakshadweep.csv"]

files = os.listdir(path)
for file in problemList:
    files.remove(file)
    
data = []

for filename in files:
    if filename.endswith('.csv'):
        state_name = filename.replace('.csv', '')

        file_path = os.path.join(path, filename)
        df = pd.read_csv(file_path)

        starting_dno = df['DNo'].iloc[0]
        ending_dno = df['DNo'].iloc[-1]

        data.append([state_name, starting_dno, ending_dno])
        
abbreDF = pd.DataFrame(data, columns=['state', 'startingDNo', 'endingDNo'])

abbreDF.to_csv('DATA\\Test\\Abbreviations\\stateDNoMapping.csv', index=False)  

        