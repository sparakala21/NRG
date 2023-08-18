import csv

import sys

if(len(sys.argv)>3):
  print("Usage: python3 csvconverter.py readfile writefile")
  sys.exit


# Open the CSV file
csv_file = open(sys.argv[2], 'w', newline='')

csv_writer = csv.writer(csv_file)
with open(sys.argv[1], 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    csv_writer.writerow([row[1], row[0]])

csv_file.close()