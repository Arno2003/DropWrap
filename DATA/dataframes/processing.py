import pandas as pd

def clean_data(csv_file_path, cleaned_csv_file_path):
    df = pd.read_csv(csv_file_path)
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].str.rstrip(' \t\n\r')  # Strip trailing spaces and special characters

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(cleaned_csv_file_path, index=False)

if __name__ == "__main__":
    input_csv_path = "DATA/dataframes/DistrictWise/Coordinates/DistrictCd.csv"
    output_csv_path = "DATA/dataframes/DistrictWise/Coordinates/CleanDistrictCd.csv"
    clean_data(input_csv_path, output_csv_path)
