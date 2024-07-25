# Filter the data for Social Category = Overall
df_filtered = df[df['Social Category'] == 'General']

data = df_filtered[['MappedDNo', 'upPrim_Overall']]

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import seaborn as sns

# Perform hierarchical/agglomerative clustering
linked = linkage(data, method='ward')
