import pandas as pd

# Read the two CSV files into DataFrames
df1 = pd.read_csv('BackEnd\Test\latlong.csv')
df2 = pd.read_csv('BackEnd\Test\castClustGuj.csv')[['Location', 'cluster']]

# Merge the DataFrames based on the common column
merged_df = pd.merge(df1, df2, on='Location', how='inner')

# 'inner' indicates that only rows with common values in both DataFrames will be included in the result.
# If you want to include all rows from both DataFrames, you can use 'outer' instead of 'inner'.

merged_df.to_csv('BackEnd\Test\GujaratCoordAndClsut.csv', index=False)
