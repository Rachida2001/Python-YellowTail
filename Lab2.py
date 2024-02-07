import os
import csv

# Create a mapping with dictionary to standardize field names
standardized_header_mapping = {
    'Host Name': ['Host Name', 'hostname', 'Name', 'Host'],
    'IP Address': ['IP Address', 'IP', 'IPAddress'],
    'Department': ['Department', 'Dept'],
    'OS': ['OS', 'Operating System'],
    'Function': ['Function']
}

# Read inventory files from the directory
parent_dir = "Inventories"
consolidated_records = []

for filename in os.listdir(parent_dir):
    with open(os.path.join(parent_dir, filename), 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            modified_record = {}
            for standard_field, variant_fields in standardized_header_mapping.items():
                for variant_field in variant_fields:
                    if variant_field in row:
                        modified_record[standard_field] = row[variant_field]
                        break
            consolidated_records.append(modified_record)

# Write modified and consolidated records into one file
output_file = 'consolidated_inventory.csv'
with open(output_file, 'w', newline='') as csv_file:
    header_names = standardized_header_mapping.keys()
    writer = csv.DictWriter(csv_file, fieldnames=header_names)
    writer.writeheader()
    writer.writerows(consolidated_records)

print(f"Consolidated inventory has been saved to {output_file}")

# Read the content of the consolidated_inventory.csv file into a list of dictionaries
with open('consolidated_inventory.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    consolidated_records = list(csv_reader)

# Sort the list of dictionaries based on the "Department" field
sorted_records = sorted(consolidated_records, key=lambda x: x['Department'])

# Print the header row
if consolidated_records:
    print('\t'.join(consolidated_records[0].keys()))

# Print the sorted content with two tabs as the delimiter
for record in sorted_records:
    print("{:<10}\t{:<10}\t{:<10}\t{:<10}\t{}".format(
        record['Host Name'],
        record['IP Address'],
        record['Department'],
        record['OS'],
        record['Function']
    ))