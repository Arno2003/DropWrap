import pandas as pd
import os
import csv

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
    unnamed_rows = df[df.apply(lambda row: any(str(val).startswith('Unnamed:') for val in row), axis=1)]
    # Drop the identified rows
    df = df.drop(unnamed_rows.index)
    return df

def process_file(filepath):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filepath, skiprows=range(4), skipfooter=2, engine='python', quoting=csv.QUOTE_NONE, encoding='utf-8')

    # Remove rows and columns
    df = remove_rows_and_columns(df)

    # Replace column names
    df = replace_column_names(df)

    # Create the modified file name
    base_filename = os.path.basename(filepath)
    new_filename = f"{os.path.splitext(base_filename)[0]}_modified.csv"
    output_filepath = os.path.join('DATA/Test/Districtwise_filtered_data', new_filename)

    # Save the modified DataFrame back to a CSV file
    df.to_csv(output_filepath, index=False)

    print(f"Success!!! Modified DataFrame saved to {output_filepath}.")

def main():
    input_folder = 'DATA/dataframes/DistrictWise/2021-2022'
    output_folder = 'DATA/Test/Districtwise_filtered_data'

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Process each CSV file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            filepath = os.path.join(input_folder, filename)
            process_file(filepath)

if __name__ == "__main__":
    main()
