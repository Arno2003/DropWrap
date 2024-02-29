import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('BackEnd\\Test\\InputData\\FilteredData\\filtered_data(General_prim_Boys).csv')

# Extracting the column names
locations = df['Location']
data = df['General_prim_Boys'].values.reshape(-1, 1)

# Perform hierarchical clustering
Z = linkage(data, 'ward')
# Plot dendrogram
plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
dendrogram(Z, labels=locations.values, leaf_rotation=90., leaf_font_size=8.)
plt.xticks(rotation=90)
plt.show()

# Save cluster details to a CSV file

cluster_labels = fcluster(Z, 7, criterion='maxclust')

# Create a new DataFrame with location and cluster labels
result_df = pd.DataFrame({'Location': locations, 'Cluster': cluster_labels})

# Save the result to a new CSV file
result_df.to_csv('BackEnd\Test\OutputDAta\gen_prim_boys_clust.csv', index=False)


cluster_df = pd.DataFrame(Z, columns=['Cluster 1', 'Cluster 2', 'Distance', 'Number of Points'])
cluster_df.to_csv('BackEnd\Test\OutputDAta\gen_prim_boys_cluster_details.csv', index=False)
