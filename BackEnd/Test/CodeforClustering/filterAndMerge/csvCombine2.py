import pandas as pd
import os
import csv

folderPath = "BackEnd\\Test\\OutputData\\filteredOutputs\\clusters"

par = ['General', 'OBC', 'Overall', 'SC', 'ST']

combined_output = pd.DataFrame()


def stdNum(std):
    if std == 'prim':
        return ''
    if std == 'upPrim':
        return '.1'
    if std == 'snr':
        return '.2'


for i in range(0, len(par)):
    combined_data = pd.DataFrame()
    for filename in os.listdir(folderPath):
        if filename.endswith(".csv"):

            params = filename.split('(')[1].split(')')[0].split('_')

            cat, std, gen = params[0], params[1], params[2]
            if par[i] == cat:
                file_path = os.path.join(folderPath, filename)

                # Read the CSV file into a dataframe
                df = pd.read_csv(file_path)

                combined_data['Location'] = df['Location']
                combined_data['Caste'] = df['Caste']
                combined_data[gen.capitalize()+stdNum(std)] = df['Cluster']
                # print(gen.capitalize()+stdNum(std))
                # print(std)

    combined_output = pd.concat(
        [combined_output, combined_data], ignore_index=True)
    combined_output.to_csv(f"DATA\\dataframes\\formatted_cluster_data.csv")
