import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def KMclust(df, filePath):
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
    cast = df["Social Category"]
    for i in cast:
        if i not in clustNames:
            clustNames.append(i)

    df.dropna(inplace=True)
    # Select relevant columns for clustering
    features = df[feat]

    # Standardize the features for better performance of clustering algorithm
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Combine location and social category columns for clustering
    df['combined_key'] = df['Location'] + '_' + df['Social Category']

    # Initialize and fit KMeans clustering model
    print(clustNames)
    n_clusters = len(clustNames)  # Adjust the number of clusters as needed
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(features_scaled)

    # Displaying the resulting DataFrame
    df.to_csv(filePath)
    # print(df)
    # Plot each cluster separately
    for cluster_label in range(n_clusters):
        cluster_data = df[df['cluster'] == cluster_label]
        plt.scatter(
                    cluster_data["prim_Girls"],
                    cluster_data["prim_Boys"],
                    label=f'{clustNames[cluster_label]}'
                )

    # Labeling axes and adding legend
    plt.xlabel('Boys')
    plt.ylabel('Girls')
    plt.title('Clusters based on primary Boys and Girls')
    plt.legend()
    plt.show()

    for cluster_label in range(n_clusters):
        cluster_data = df[df['cluster'] == cluster_label]
        plt.scatter(
                    cluster_data["upPrim_Girls"],
                    cluster_data["upPrim_Boys"],
                    label=f'{clustNames[cluster_label]}'
                )

    # Labeling axes and adding legend
    plt.xlabel('Boys')
    plt.ylabel('Girls')
    plt.title('Clusters based on upper primary Boys and Girls')
    plt.legend()
    plt.show()

    for cluster_label in range(n_clusters):
        cluster_data = df[df['cluster'] == cluster_label]
        plt.scatter(
                    cluster_data["snr_Girls"],
                    cluster_data["snr_Boys"],
                    label=f'{clustNames[cluster_label]}'
                )

    # Labeling axes and adding legend
    plt.xlabel('Boys')
    plt.ylabel('Girls')
    plt.title('Clusters based on senior Boys and Girls')
    plt.legend()
    plt.show()

def Hclust(df, destPath, n):
    X = df[['DropoutRate']]
    # Hierarchical clustering
    ward_linkage = linkage(X, method='ward')
    cluster_labels = AgglomerativeClustering(n_clusters=n, linkage='ward').fit_predict(X)

    # Add cluster labels to the dataframe
    df['Cluster'] = cluster_labels

    # Print the caste-wise clusters
    print(df[['Caste', 'Cluster']])

    # Dendrogram visualization
    plt.figure(figsize=(12, 6))
    dendrogram(ward_linkage, labels=df['Caste'].tolist(), orientation='top', distance_sort='descending', show_leaf_counts=True)
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('Caste')
    plt.ylabel('Distance')
    plt.show()


if __name__ == "__main__":
    dataForKM = pd.read_csv("BackEnd\Test\Gujarat.csv")
    opFilePathKM = "BackEnd\Test\castClustGuj.csv"
    KMclust(dataForKM, opFilePathKM)
    dataForHC = pd.read_csv("BackEnd/Test/CastWiseGuj.csv")
    opFilePAthHC = "BackEnd/Test/HClustCastWiseGuj.csv"
    # Hclust(dataForHC, opFilePAthHC)
