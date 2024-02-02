# import pandas as pd
# import numpy as np
# from scipy.cluster.hierarchy import dendrogram, linkage
# import matplotlib.pyplot as plt

# # Read data from CSV file
# file_path = 'BackEnd\Test\Gujarat.csv'  # Replace 'your_file.csv' with the actual file path
# df = pd.read_csv(file_path)

# # Extracting relevant columns for clustering
# data_columns = ['prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']
# data = df[data_columns]

# # Performing hierarchical clustering using complete linkage
# linkage_matrix = linkage(data, method='complete')

# # Plotting the dendrogram
# plt.figure(figsize=(15, 8))
# dendrogram(linkage_matrix, labels=df['Location'].astype(str) + '_' + df['Social Category'].astype(str), orientation='top', leaf_font_size=10)
# plt.title('Hierarchical Clustering Dendrogram')
# plt.xlabel('Districts_SocialCategories')
# plt.ylabel('Distance')
# plt.show()


import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# Read data from CSV file
file_path = 'BackEnd\Test\Gujarat.csv'
df = pd.read_csv(file_path)

# Extracting relevant columns for clustering
data_columns = ['prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls', 'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']
data = df[data_columns]

# Reseting index to avoid KeyError in dendrogram
df_reset = df.reset_index(drop=True)
# print(df_reset)

# Performing hierarchical clustering using complete linkage
linkage_matrix = linkage(data, method='complete')
# print(linkage_matrix)

# Plotting the dendrogram
plt.figure(figsize=(15, 8))
dendrogram(linkage_matrix, labels=df_reset['Location'].astype(str) + '_' + df_reset['Social Category'].astype(str), orientation='top', leaf_font_size=10)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Districts_SocialCategories')
plt.ylabel('Distance')
plt.show()
