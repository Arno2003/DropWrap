import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

data = pd.read_csv('BackEnd\main\Data\Gujarat.csv')

# Selecting relevant features for clustering
# selected_features = [
#     'Name Of District',
#     'Boys',
#     'Girls',
#     'Boys + Girls'
# ]

feat = [
    "prim_Girls",
    "prim_Boys",
    "prim_Overall",
    "upPrim_Girls",
    "upPrim_Boys",
    "upPrim_Overall",
    "snr_Girls",
    "snr_Boys",
    "snr_Overall"
]
clustNames = []
cast = data["Social Category"]
for i in cast:
    if i not in clustNames:
        clustNames.append(i)
n_clusters = len(clustNames) # this defines the number of clusters required, by counting number
                             # of unique features or paramerts in a column for each location

selected_features = ['Location', 'prim_Girls', 'prim_Boys', 'prim_Overall', 'upPrim_Girls',
                     'upPrim_Boys', 'upPrim_Overall', 'snr_Girls', 'snr_Boys', 'snr_Overall']

data = data[selected_features]
data = data.replace("NR", 0)

# Drop rows with NULL values (NaNs)
data.dropna(inplace=True)

# Extract the 'year' column, convert it to a numerical format
# data['year'] = data['year'].str.extract(r'(\d{4})').astype(int)

# Standardize the numerical features for clustering
scaler = StandardScaler()

numerical_features = data.drop(columns=['Location'])


scaled_features = scaler.fit_transform(numerical_features)

# hierarchical clustering
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')  # Adjust n_clusters as needed,
                                                                                 # here cluster will be adjusted  
                                                                                 # automatically accordin to the 
                                                                                 # number of required clusters
data['Cluster_Label'] = agg_clustering.fit_predict(scaled_features)

# Dendrogram
lbl = data['Location'].tolist()
dendrogram = sch.dendrogram(sch.linkage(scaled_features, method='ward'), labels=lbl)

# Visualize the dendrogram
plt.title('Dendrogram')
plt.xlabel('Students')
plt.ylabel('Euclidean Distances')
plt.show()

result_data = data[['Location', 'Cluster_Label']]
print(result_data)
result_data.to_csv("BackEnd\main\Data\cluster.csv")
