import pandas as pd
import os
import csv

def replace_column_names(df):
    # Specify column replacements for Girls, Boys, and Overall
    all_column_replacements = {
        'Girls': {'Girls': 'prim_Girls', 'Girls.1': 'upPrim_Girls', 'Girls.2': 'snr_Girls'},
        'Boys': {'Boys': 'prim_Boys', 'Boys.1': 'upPrim_Boys', 'Boys.2': 'snr_Boys'},
        'Overall': {'Overall': 'prim_Overall', 'Overall.1': 'upPrim_Overall', 'Overall.2': 'snr_Overall'}
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
    cols_to_drop = df.filter(regex='^Unnamed:').columns

    # Drop the identified columns
    df.drop(columns=cols_to_drop, inplace=True)
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
