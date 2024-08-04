import pandas as pd

# Read the CSV files
df_final_impressions = pd.read_csv(
    'DATA\\RNN Data\\outputData\\final_impressions.csv')
stateDNoMapping_df = pd.read_csv(
    'DATA\\Test\\Abbreviations\\stateDNoMapping.csv')

# Remove "IndiaDistricts" from stateDNoMapping_df
# stateDNoMapping_df = stateDNoMapping_df[stateDNoMapping_df["state"]
#                                         != "IndiaDistricts"]

# Define a function to map DNo to State


def map_dno_to_state(dno, state_df):
    for _, row in state_df.iterrows():
        if row['startingDNo'] <= dno <= row['endingDNo']:
            return row['Location']
    return None


# Apply the mapping function
df_final_impressions['State'] = df_final_impressions['DNo'].apply(
    lambda x: map_dno_to_state(x, stateDNoMapping_df))

# Replace "None" in State column with corresponding district names from "Location" column
df_final_impressions['State'] = df_final_impressions.apply(
    lambda row: row['Location'] if pd.isnull(row['State']) else row['State'],
    axis=1
)

# Convert all state names to uppercase
df_final_impressions['State'] = df_final_impressions['State'].str.upper()

# Drop rows where State is still NaN (if any)
df_final_impressions_filtered = df_final_impressions.dropna(subset=['State'])

# Move the 'State' column to the extreme left
columns = df_final_impressions_filtered.columns.tolist()
columns.insert(0, columns.pop(columns.index('State')))
df_final_impressions_filtered = df_final_impressions_filtered[columns]


# Save the mapped data to a new CSV file
output_file = 'DATA\\RNN Data\\final_impressions_filtered_v2.csv'
df_final_impressions_filtered.to_csv(output_file, index=False)
print(f"Mapped data has been saved to {output_file}")
