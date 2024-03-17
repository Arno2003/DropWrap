import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt
import os

# merging at the same time while forming, to create a final combined file




# funtion for forming cluster for each file traversed  
def formClusterCasteWise(folderPath):
    for fileName in os.listdir(folderPath):
        if fileName.endswith(".csv"):
            file_path = os.path.join(folderPath, fileName)
        
            # Read the CSV file into a dataframe        
            df = pd.read_csv(f'BackEnd\\Test\\InputData\\FilteredData\\{fileName}')
            
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
            dendrogram(Z, labels=locations.values, leaf_rotation=90., leaf_font_size=8.)
            plt.xticks(rotation=90)
            # plt.show()

            # Save cluster details to a CSV file

            cluster_labels = fcluster(Z, 7, criterion='maxclust')

            # Create a new DataFrame with location and cluster labels
            result_df = pd.DataFrame({'Location': locations, 'Cluster': cluster_labels, 'Caste': caste})

            # Save the result to a new CSV file
            result_df.to_csv(f'BackEnd\\Test\\OutputData\\filteredOutputs\\clusters\\{fileName}.csv', index=False)


            cluster_df = pd.DataFrame(Z, columns=['Cluster 1', 'Cluster 2', 'Distance', 'Number of Points'])
            cluster_df.to_csv(f'BackEnd\\Test\\OutputData\\filteredOutputs\\clusterDetails\\{fileName}_details.csv', index=False)

if __name__ == "__main__":
    folderPath = "BackEnd\Test\InputData\FilteredData"
    formClusterCasteWise(folderPath)