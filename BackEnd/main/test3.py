import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

data = pd.read_csv('output_data.csv')

# Selecting relevant features for clustering
selected_features = [
    'Name Of District',
    'Boys',
    'Girls',
    'Boys + Girls'
]
data = data[selected_features]
data = data.replace("NR", 0)

# Drop rows with NULL values (NaNs)
data.dropna(inplace=True)

# Extract the 'year' column, convert it to a numerical format
#data['year'] = data['year'].str.extract(r'(\d{4})').astype(int)

# Standardize the numerical features for clustering
scaler = StandardScaler()
numerical_features = data.drop(columns=['Name Of District'])

scaled_features = scaler.fit_transform(numerical_features)

# hierarchical clustering
agg_clustering = AgglomerativeClustering(n_clusters=5, linkage='ward')  # Adjust n_clusters as needed
data['Cluster_Label'] = agg_clustering.fit_predict(scaled_features)

# Dendrogram
lbl = data['Name Of District'].tolist()
dendrogram = sch.dendrogram(sch.linkage(scaled_features, method='ward'), labels=lbl)

# Visualize the dendrogram
plt.title('Dendrogram')
plt.xlabel('Students')
plt.ylabel('Euclidean Distances')
plt.show()

result_data = data[['Name Of District', 'Cluster_Label']]
print(result_data)
result_data.to_csv("cluster.csv")

