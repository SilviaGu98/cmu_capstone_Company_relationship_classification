# importing csv module
import csv

# csv file name
filename = "cleaned-csv.csv"

rows = []
# reading csv file
with open(filename, encoding='UTF-8') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # extracting each data row one by one
    for row in csvreader:
        entity_a = row[0]
        entity_b = row[1]
        row.append(row[2].find(entity_a[:7]))
        row.append(row[2].find(entity_b[:7]))
        rows.append(row)

    # get total number of rows
print(rows)
with open('cleaned_data.csv.csv', 'w', encoding='UTF-8', newline='') as f:
    write = csv.writer(f)
    write.writerows(rows)
