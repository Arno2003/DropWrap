import pandas as pd

# Specify the Excel file path and the number of rows to skip
excel_file = 'D:\projects\SIH\Smart-India-Hackathon\BackEnd\Test\DropoutRateAndhraPradesh.xlsx'
n_rows_to_skip = 3  # Adjust this value as needed

# Read the Excel file into a DataFrame, skipping the specified rows
df = pd.read_excel(excel_file, skiprows=n_rows_to_skip)

# Specify the desired CSV output file path
csv_file = 'D:\projects\SIH\Smart-India-Hackathon\BackEnd\Test\output_data_2019-20.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file)
