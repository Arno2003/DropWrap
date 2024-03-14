import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt
import csv

def clust(data, feat, fileNo):
    # setting parameters for dendrogram in matplotlib
    plt.rcParams['figure.figsize'] = [24, 16]

    clustNames = []
    cast = data["Social Category"]
    for i in cast:
        if i not in clustNames:
            clustNames.append(i)
    n_clusters = len(clustNames) # this defines the number of clusters required, by counting number
                                # of unique features or paramerts in a column for each location

    selected_features = ['Location', feat]

    data = data[selected_features]
    data = data.replace("NR", 0)

    # Drop rows with NULL values (NaNs)
    data.dropna(inplace=True)

    # Standardize the numerical features for clustering
    scaler = StandardScaler()

    numerical_features = data.drop(columns=['Location'])


    scaled_features = scaler.fit_transform(numerical_features)

    # hierarchical clustering
    agg_clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')  # Adjust n_clusters as needed,
                                                                                    # here cluster will be adjusted  
                                                                                    # automatically accordin to the 
                                                                                    # number of required clusters
    label = feat + '_Cluster_Label'
    data[label] = agg_clustering.fit_predict(scaled_features)

    # Dendrogram
    lbl = data['Location'].tolist()
    dendrogram = sch.dendrogram(sch.linkage(scaled_features, method='ward'), labels=lbl)


    # Save the dendrogram as a PNG file with higher resolution
    plt.savefig(f'BackEnd\main\Images\GujaratCastWiseDendrogram({fileNo}).jpeg', dpi=600)


    # Visualize the dendrogram
    plt.title('Dendrogram')
    plt.xlabel('Students')
    plt.ylabel('Euclidean Distances')
    # plt.show()
    # plt.savefig("BackEnd\main\Images\GujaratCastWiseDendrogram.jpeg")

    result_data = data[['Location', label]]
    return result_data
    
if __name__ == "__main__":
    totalData = pd.read_csv("BackEnd\Test\InputData\Gujarat.csv")
    features = []
    with open("BackEnd\Test\InputData\Gujarat.csv") as csv_file:
 
        # reading the csv file using DictReader
        csv_reader = csv.DictReader(csv_file)
    
        # converting the file to dictionary
        # by first converting to list
        # and then converting the list to dict
        dict_from_csv = dict(list(csv_reader)[0])
    
        # making a list from the keys of the dict
        features = list(dict_from_csv.keys())
    features = features[2:]
    #print(features)
    
    fileNo = 0
    dataFrames = []
    for feat in features:
        print(feat)
        data = totalData[['Location', 'Social Category', feat]]
        temp = clust(data, feat, fileNo)
        # print(temp)
        dataFrames.append(temp)
        fileNo += 1
    
    noOfDF = len(dataFrames)
    df2 = totalData[['Location']]
    for i in range(1, noOfDF):
        df2[[dataFrames[i][0]]] = dataFrames[i]
    df2.to_csv("BackEnd\Test\OutputData\temp.csv")
    # print(df1)