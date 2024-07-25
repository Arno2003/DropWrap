import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

class ClusterFormation:
    def casteWiseCluster(fp, parameters): # fp -> file path, parameters -> column names 
        df = pd.read_csv(fp)
        
        # parameters = [Social Category - e.g. General, SC,etc ;  Column Name - e.g. primGirls, upperPrimBoys, etc]
        
        # storing parameters
        socialCat = parameters[0]
        colName = parameters[1]
        
        # slicing data based on the Social Category
        slicedData = df[df["Social Category"] == socialCat]
        
        data = slicedData[["Location",colName]]
        1
        # changing location names to serial numbers to give them a numeric value
        df1 = pd.DataFrame(data)
        df1['serialNumber'] = list(range(1, len(df)+1))
        newData = df[[colName, "serialNumber"]]
       
        ####################### plotting the data, forming the dendrogram ####################
         
        # forming the distance matrix array for clustering
        dataLinkage = linkage(newData.values.reshape(-1,1), "ward")
        
        dendrogram(dataLinkage)
        plt.title('Hierarchical Clustering Dendrogram')
        plt.xlabel('Index')
        plt.ylabel('Distance')
        plt.show()
        
        #######################################################################################
        
        
        ########################## forming the clusters, assingning them ######################
        
        df = pd.DataFrame(newData)
        clustering = AgglomerativeClustering(n_clusters=3, linkage='ward')
        clusters = clustering.fit_predict(df)
        newData['Cluster'] = clusters
        
        #######################################################################################
        
        ############################## storing the final output ########################################
        
        newData.to_csv(f"BackEnd\Test\ModelTesting\outputData\{socialCat+"_"+colName}.csv", index=False)
        
        #################################################################################################
        