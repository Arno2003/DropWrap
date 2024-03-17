import pandas as pd
import os

# Directory containing your files
directory = 'BackEnd\\Test\\InputData\\FilteredData'

# Initialize an empty DataFrame to store the combined data
data = [['Location', 'Social Category']]
combined_data = pd.DataFrame(data)

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):  # Assuming files are in CSV format
        filepath = os.path.join(directory, filename)
        # Read the file into a DataFrame
        df = pd.read_csv(filepath)
        # print(df.head)
        # Merge with combined_data based on 'Location' and 'Social Category'
        print(df[['Location', 'Social Category']])
        print(combined_data)
        combined_data = combined_data.merge(df, on=['Location', 'Social Category'], how='outer')
        print(combined_data.head)

# Optionally, you can drop duplicates if any
combined_data = combined_data.drop_duplicates()

# Save the combined DataFrame to a new CSV file
combined_data.to_csv('combined_data.csv', index=False)

# Display the combined DataFrame
print(combined_data)
