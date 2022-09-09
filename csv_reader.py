import csv
from HashTable import hash_map

# Read the package data from CSV file
with open('./delivery_data/package_data.csv') as datafile:
        read_csv = csv.reader(datafile, delimiter=',')
        