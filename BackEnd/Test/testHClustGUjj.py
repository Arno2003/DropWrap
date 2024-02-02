import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Read data from CSV file
file_path = 'castClustGuj.csv'  # Replace 'your_file.csv' with the actual file path
df = pd.read_csv(file_path)

# Extracting relevant columns for clustering
data_columns = ['prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']
data = df[data_columns]

# Performing hierarchical clustering using complete linkage
linkage_matrix = linkage(data, method='complete')

# Plotting the dendrogram
plt.figure(figsize=(15, 8))
dendrogram(linkage_matrix, labels=df['Location'].astype(str) + '_' + df['Social Category'].astype(str), orientation='top', leaf_font_size=10)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Districts_SocialCategories')
plt.ylabel('Distance')
plt.show()