import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
import os

# merging at the same time while forming, to create a final combined file


class Clustering:
    # function for combining all the csvs formed
    def combineCSV(self, folderPath):
        par = ['General', 'OBC', 'Overall', 'SC', 'ST']

        combined_output = pd.DataFrame()

        for i in range(0, len(par)):
            combined_data = pd.DataFrame()
            for filename in os.listdir(folderPath):
                if filename.endswith(".csv"):

                    params = filename.split('(')[1].split(')')[0].split('_')
                    print(params)
                    cat, std, gen = params[0], params[1], params[2]
                    if par[i] == cat:
                        file_path = os.path.join(folderPath, filename)

                        # Read the CSV file into a dataframe
                        df = pd.read_csv(file_path)

                        combined_data['Location'] = df['Location']
                        combined_data['Caste'] = df['Caste']
                        combined_data[params[1]+'_'+params[2]] = df['Cluster']

            combined_output = pd.concat(
                [combined_output, combined_data], ignore_index=True)
            combined_output.to_csv(
                f"DATA\\dataframes\\formatted_cluster_data.csv")

    # funtion for forming cluster for each file traversed

    def formClusterCasteWise(self, folderPath):

        for fileName in os.listdir(folderPath):
            if fileName.endswith(".csv"):
                file_path = os.path.join(folderPath, fileName)

                # Read the CSV file into a dataframe
                df = pd.read_csv(
                    f'BackEnd\\main\\Data\\InputData\\FilteredData\\{fileName}')

                # Extracting the column names by removing substrings from file name
                subs = ['filtered_data(',  ')', '.csv']
                colName = fileName[14:len(fileName)-5]
                for i in subs:
                    colName.replace('', i)
                print(type(colName), colName)

                # Extracting the column data
                locations = df['Location']
                caste = df['Social Category']
                data = df[colName].values.reshape(-1, 1)

                # Perform hierarchical clustering
                Z = linkage(data, 'ward')

                # Plot dendrogram
                plt.figure(figsize=(10, 5))
                plt.title(f'Hierarchical Clustering for {fileName} Dendrogram')
                plt.xlabel('Sample Index')
                plt.ylabel('Distance')
                dendrogram(Z, labels=locations.values,
                           leaf_rotation=90., leaf_font_size=8.)
                plt.xticks(rotation=90)
                # plt.show()

                # Save cluster details to a CSV file

                cluster_labels = fcluster(Z, 7, criterion='maxclust')

                # Create a new DataFrame with location and cluster labels
                result_df = pd.DataFrame(
                    {'Location': locations, 'Cluster': cluster_labels, 'Caste': caste})

                # Save the result to a new CSV file
                result_df.to_csv(
                    f'BackEnd\\Test\\OutputData\\filteredOutputs\\clusters\\{fileName}.csv', index=False)

                # Saving the cluster details in another CSV file
                cluster_df = pd.DataFrame(
                    Z, columns=['Cluster 1', 'Cluster 2', 'Distance', 'Number of Points'])
                cluster_df.to_csv(
                    f'BackEnd\\main\\Data\\OutputData\\filteredOutputs\\clusterDetails\\{fileName}_details.csv', index=False)

    def formClusterCSV(self, folderPath):
        try:
            if os.path.isdir(folderPath):
                self.formClusterCasteWise(folderPath)
                self.combineCSV(folderPath)
            else:
                print("Invalid")
        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    folderPath = "BackEnd\\main\\Data\\InputData\\FilteredData"
    clst = Clustering()
    clst.formClusterCSV(folderPath)
