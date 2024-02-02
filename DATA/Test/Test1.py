import pandas as pd

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
    df = pd.read_csv("DATA\Test\ANI.csv", skiprows=range(4),skipfooter=2, engine='python')
    return df

def main():
    # Read the CSV file into a DataFrame
    df = pd.read_csv("DATA\Test\ANI.csv")

    # Display the original DataFrame
    print("Original DataFrame:")
    print(df)
    
    # Remove rows and columns
    df = remove_rows_and_columns(df)

    # Replace column names
    df = replace_column_names(df)

    
    # Display the modified DataFrame
    print("\nDataFrame after modifications:")
    print(df)

    # Save the modified DataFrame back to a CSV file
    df.to_csv('modified_file.csv', index=False)

    print("\nSuccess!!! Modified DataFrame saved to modified_file.csv.")

if __name__ == "__main__":
    main()
