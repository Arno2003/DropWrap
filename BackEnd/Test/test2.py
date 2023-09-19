import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# Sample data (replace with your dataset)
data = pd.DataFrame({
    'Student_ID': range(1, 21),
    'Age': [18, 19, 20, 21, 22, 20, 19, 21, 22, 18, 20, 21, 22, 18, 19, 20, 21, 22, 19, 20],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'Caste': ['General', 'SC', 'ST', 'General', 'OBC', 'General', 'SC', 'ST', 'General', 'OBC', 'General', 'SC', 'ST', 'General', 'OBC', 'General', 'SC', 'ST', 'General', 'OBC'],
    'Dropout_Rate': [0.05, 0.1, 0.15, 0.2, 0.25, 0.12, 0.18, 0.21, 0.08, 0.13, 0.22, 0.28, 0.19, 0.09, 0.16, 0.24, 0.26, 0.11, 0.17, 0.23]
})

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
