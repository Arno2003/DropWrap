import csv

# Input CSV file name
input_file = './geo.csv'

# Output CSV file name
output_file = 'output.csv'

# Open the input and output files
with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        # Check if any value in the row is not blank
        if any(row):
            # If at least one value is not blank, write the row to the output file
            writer.writerow(row)

print(f"Blank rows removed. Output saved to {output_file}")
