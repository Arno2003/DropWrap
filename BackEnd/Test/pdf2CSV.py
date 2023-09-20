import tabula
import pandas as pd

pdf_file_path = "educationalstatisticsbook2019-20.pdf"
page_number = 27  # Change this to your desired page number
csv_file_path = "output_data.csv"

# Extract tabular data using Tabula
tables = tabula.read_pdf(pdf_file_path, pages=page_number)

if not tables:
    print("No tables found on the specified page.")
else:
    # Assuming you want to work with the first table on the page
    first_table = tables[0]
    df = pd.DataFrame(first_table)

    # Export DataFrame to CSV
    df.to_csv(csv_file_path, index=False)
