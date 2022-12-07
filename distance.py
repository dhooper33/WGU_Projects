import csv
import datetime

#Reading data from CSV files
with open('./delivery_data/WGUPSdistance_data.csv') as distancecsv:
   distance_csv = list(csv.reader(distancecsv, delimiter=','))
with open('./data/WGUPSdestination_name_data.csv') as destinationcsv:
    destination_name_csv = list(csv.reader(destinationcsv, delimiter=','))



    