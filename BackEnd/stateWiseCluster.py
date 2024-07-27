# import pandas as pd

# # Read the CSV files
# df_data = pd.read_csv('DATA\\Test\\stateWiseData\\stateWiseData.csv')  # Replace with your file path
# df_states = pd.read_csv('DATA\\Test\\Abbreviations\\stateDNoMapping.csv')  # Replace with your file path

# # Define a function to map DNo to startingDNo//100 * 100
# def map_dno(dno):
#     for _, row in df_states.iterrows():
#         if row['startingDNo'] <= dno <= row['endingDNo']:
#             return row['startingDNo'] // 100 * 100
#     return None  # In case no match is found

# # Apply the function to the DNo column
# df_data['MappedDNo'] = df_data['DNo'].apply(map_dno)

# # Save the updated DataFrame to a new CSV file
# df_data.to_csv('DATA\\Test\\stateWiseData\\states.csv', index=False)  # Replace with your desired output file path



# # import os
# # import pandas as pd
# # from sklearn.cluster import AgglomerativeClustering

# # dirLoc = "DATA\\Test\\DistrictWiseData" # i/p file location

# # vars = ["prim_Girls", "prim_Boys", "prim_Overall", "upPrim_Girls", 
# #     "upPrim_Boys", "upPrim_Overall", "snr_Girls", "snr_Boys", "snr_Overall"]
# # cats = ["General", "SC", "ST", "OBC", "Overall"]

# # if os.path.isdir(dirLoc):
# #     fileName = "DATA\\Test\\stateWiseData\\stateWiseData.csv"
# #     print("Working with : ", fileName)
# #     # if fileName not in problemList:

# #     for i in range(len(vars)):
# #         var = vars[i]
# #         for j in range(len(cats)):
# #             cat = cats[j]

# #             df = pd.read_csv(fileName)

# #             genData = df[df["Social Category"] == cat]
# #             # print(genData.head())
# #             data = genData[["DNo", var]]

# #             df = pd.DataFrame(data)

# #             # dataLinkage = linkage(newData.values.reshape(-1,1), "ward")
# #             print(fileName)
# #             print(data.head())
# #             # df = pd.DataFrame(newData)

# #             if len(data) > 10:    
# #                 noOfClust = 5
# #             elif len(data) < 10 and len(data) > 5:
# #                 noOfClust = 3
# #             else:
# #                 noOfClust = 2
                
# #             clustering = AgglomerativeClustering(n_clusters=noOfClust, linkage='ward')
# #             clusters = clustering.fit_predict(data)
# #             data[cat + "_" +var + "_" +'Cluster'] = clusters

# #             dirPath = "BackEnd\\Test\\ModelTesting\\outputData" + fileName.replace(".csv", "")
# #             if not os.path.exists(dirPath):
# #                 os.mkdir(path=dirPath)
            
# #             dirPath += "\\" + cat

# #             if not os.path.exists(dirPath):
# #                 os.mkdir(path=dirPath)

# #             filePath = dirPath + "\\"  + var + ".csv"

# #             if os.path.exists(filePath):
# #                 os.remove(filePath)
# #                 # newData.to_csv(filePath)
# #             data.to_csv(filePath)

# # Load the data
# file_path = 'DATA\Test\stateWiseData\states.csv'
# df = pd.read_csv(file_path)

# # Filter the data for Social Category = Overall
# df_filtered = df[df['Social Category'] == 'General']

# data = df_filtered[['MappedDNo', 'upPrim_Overall']]

# import matplotlib.pyplot as plt
# from scipy.cluster.hierarchy import dendrogram, linkage
# import seaborn as sns

# # Perform hierarchical/agglomerative clustering
# linked = linkage(data, method='ward')

# locations = df_filtered['State'].values

# # Plot the dendrogram
# plt.figure(figsize=(12, 8))

# # Create a dendrogram with labels
# dendrogram(
#     linked,
#     orientation='top',
#     distance_sort='descending',
#     show_leaf_counts=True,
#     labels=locations  # Add labels to the dendrogram
# )

# # Rotate x-axis labels if necessary
# plt.xticks(rotation=90, fontsize=8)

# plt.title('Dendrogram')
# plt.xlabel('Location')
# plt.ylabel('Distance')
# plt.savefig('dendrogram_States.png', dpi=600)  # Save with DPI
# plt.show()

# import os
# import pandas as pd

# # Define the main folder and subfolders
# main_folder = 'BackEnd\Test\ModelTesting\outputData\states'
# subfolders = ['General', 'OBC', 'Overall', 'SC', 'ST']

# # Initialize an empty DataFrame for the final result
# final_df = pd.DataFrame()

# # Iterate through each subfolder
# for subfolder in subfolders:
#     subfolder_path = os.path.join(main_folder, subfolder)
#     # Initialize an empty DataFrame for the subfolder
#     subfolder_df = pd.DataFrame()
    
#     # Iterate through each CSV file in the subfolder
#     for filename in os.listdir(subfolder_path):
#         if filename.endswith('.csv'):
#             file_path = os.path.join(subfolder_path, filename)
#             # Read the CSV file
#             df = pd.read_csv(file_path)
#             # Keep only the common columns and concatenate the unique columns
#             common_columns = df[['DNo']]
#             unique_columns = df.drop(columns=['DNo'])
#             concatenated_df = pd.concat([common_columns, unique_columns], axis=1)
#             # Append the concatenated DataFrame to the subfolder DataFrame
#             subfolder_df = pd.concat([subfolder_df, concatenated_df], ignore_index=True)
    
#     # Add the 'Social Category' column to the subfolder DataFrame
#     subfolder_df['Social Category'] = subfolder
#     # Append the subfolder DataFrame to the final DataFrame
#     final_df = pd.concat([final_df, subfolder_df], ignore_index=True)

# # Save the final concatenated DataFrame to a new CSV file
# final_df.to_csv('BackEnd\Test\ModelTesting\outputData\states.csv', index=False)

# print("Concatenation complete. The final file 'states.csv' has been created.")


import os
import pandas as pd

# Define the main folder and subfolders
main_folder = 'BackEnd\Test\ModelTesting\outputData\states'
subfolders = ['General', 'OBC', 'Overall', 'SC', 'ST']

# Initialize an empty DataFrame for the final result
final_df = pd.DataFrame()

# Function to filter columns
def filter_columns(df):
    # Keep only 'DNo' and columns ending with '_Cluster'
    columns_to_keep = ['DNo'] + [col for col in df.columns if col.endswith('_Cluster')]
    return df[columns_to_keep]

# Iterate through each subfolder
for subfolder in subfolders:
    subfolder_path = os.path.join(main_folder, subfolder)
    subfolder_df = pd.DataFrame()
    
    # Iterate through each CSV file in the subfolder
    for filename in os.listdir(subfolder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(subfolder_path, filename)
            # Read the CSV file
            df = pd.read_csv(file_path)
            # Filter the columns
            df = filter_columns(df)
            # Append the filtered DataFrame to the subfolder DataFrame
            subfolder_df = pd.concat([subfolder_df, df], ignore_index=True)
    
    # Add the 'Social Category' column to the subfolder DataFrame
    subfolder_df['Social Category'] = subfolder
    # Append the subfolder DataFrame to the final DataFrame
    final_df = pd.concat([final_df, subfolder_df], ignore_index=True)

# Save the final concatenated DataFrame to a new CSV file
final_df.to_csv('BackEnd\Test\ModelTesting\outputData\states.csv', index=False)

print("Concatenation complete. The final file 'sides.csv' has been created.")

