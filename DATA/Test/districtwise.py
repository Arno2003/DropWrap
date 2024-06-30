import pandas as pd
import os

def replace_column_names(df):
    # Specify column replacements for Girls, Boys, and Overall
    all_column_replacements = {
        'Girls': {'Girls': 'Girls(Primary Dropout)', 'Girls.1': 'Girls(Upper Primary Dropout)', 'Girls.2': 'Girls(Secondary Dropout)'},
        'Boys': {'Boys': 'Boys(Primary Dropout)', 'Boys.1': 'Boys(Upper Primary Dropout)', 'Boys.2': 'Boys(Secondary Dropout)'},
        'Overall': {'Overall': 'Overall(Primary Dropout)', 'Overall.1': 'Overall(Upper Primary Dropout)', 'Overall.2': 'Overall(Secondary Dropout)'}
    }

    # Use a loop to replace the specified column names for each category
    for category, column_replacements in all_column_replacements.items():
        df = df.rename(columns=column_replacements)

    return df

def remove_rows_and_columns(df):
    # Drop the first 3 rows and last 2 rows
    df = df.iloc[3:-2].copy()
    
    # Remove unnamed columns
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    return df

def process_file(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Remove rows and columns
    df = remove_rows_and_columns(df)

    # Replace column names
    df = replace_column_names(df)

    # Save the modified DataFrame back to a CSV file
    df.to_csv(file_path, index=False)
    
    print(f"Success!!! Modified DataFrame saved to {file_path}")

def main():
    folder_path =r"DATA\dataframes\DistrictWise\2021-2022"
    
    # List all CSV files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        print(f"Processing file: {file_path}")
        process_file(file_path)

if __name__ == "__main__":
    main()
