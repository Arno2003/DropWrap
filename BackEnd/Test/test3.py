import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

data = pd.read_csv('DOR.csv')

# Selecting relevant features for clustering
selected_features = [
    'State_UT', 'year', 'Primary_Boys', 'Primary_Girls', 'Primary_Total',
    'Upper Primary_Boys', 'Upper Primary_Girls', 'Upper Primary_Total',
    'Secondary _Boys', 'Secondary _Girls', 'Secondary _Total',
    'HrSecondary_Boys', 'HrSecondary_Girls', 'HrSecondary_Total'
]
data = data[selected_features]
data = data.replace("NR", 0)

# Drop rows with NULL values (NaNs)
data.dropna(inplace=True)

# Extract the 'year' column, convert it to a numerical format
data['year'] = data['year'].str.extract(r'(\d{4})').astype(int)

# Standardize the numerical features for clustering
scaler = StandardScaler()
numerical_features = data.drop(columns=['State_UT'])

scaled_features = scaler.fit_transform(numerical_features)

# hierarchical clustering
agg_clustering = AgglomerativeClustering(n_clusters=5, linkage='ward')  # Adjust n_clusters as needed
data['Cluster_Label'] = agg_clustering.fit_predict(scaled_features)

# Dendrogram
dendrogram = sch.dendrogram(sch.linkage(scaled_features, method='ward'))

# Visualize the dendrogram
plt.title('Dendrogram')
plt.xlabel('Students')
plt.ylabel('Euclidean Distances')
plt.show()

result_data = data[['State_UT', 'year', 'Cluster_Label']]
print(result_data)
result_data.to_csv("cluster.csv")

