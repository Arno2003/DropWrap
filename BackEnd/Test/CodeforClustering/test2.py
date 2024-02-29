import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# Sample data (replace with your dataset)
data = pd.read_csv("DOR.csv")

# Encode categorical variables (Gender and Caste)
label_encoder = LabelEncoder()
data['Gender'] = label_encoder.fit_transform(data['Gender'])
data['Caste'] = label_encoder.fit_transform(data['Caste'])

# Features for clustering (Age, Gender, Caste)
X = data[['Age', 'Gender', 'Caste']]

# Perform hierarchical clustering
agg_clustering = AgglomerativeClustering(
    n_clusters=3, linkage='ward')  # Adjust n_clusters as needed
data['Cluster_Label'] = agg_clustering.fit_predict(X)

# Dendrogram visualization (optional)
dendrogram = sch.dendrogram(sch.linkage(X, method='ward'))

# Visualize the dendrogram (optional)
plt.title('Dendrogram')
plt.xlabel('Students')
plt.ylabel('Euclidean Distances')
plt.show()

# Print the results
print(data[['Student_ID', 'Age', 'Gender', 'Caste', 'Dropout_Rate', 'Cluster_Label']])
