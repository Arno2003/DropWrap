import tabula
import pandas as pd
import csv

pdf_file = "info.pdf"

# Extract tabular data from the PDF
df = tabula.read_pdf(pdf_file, pages='all')

# Concatenate DataFrames if there are multiple tables or pages
if isinstance(df, list):
    df = pd.concat(df)

# Saving the DataFrame as a CSV file
df.to_csv('data.csv', index=False)
f = open("data.csv", "r")
data = csv.reader(f)
df = pd.read_csv("data.csv")

x = df[["Sr. No", "District Name", "Taluka", "cluname", "Village Name", "schcd", "School Name", "School Category"]]
x.to_csv("sorted.csv")

z = df[["School Name"]]
z.to_csv("schools.csv")

f1 = open("data1.csv", "r")
dt = csv.reader(f1)
d = pd.read_csv("data1.csv")

temp = df["School Name"] + ", " + df["Village Name"] + ", "  + df["District Name"] + ", PIN Code=" + d['Pincode'] + " Gujarat"

y = pd.DataFrame({"Location" : temp})
y.to_csv("locations.csv")

# get the pincode from the infos.pdf file and concat it with the data.csv file contents