import csv
import hash_table

# Read CSV files
with open('./delivery_data/WGUPSpackage_data.csv') as packagefile:
    package_data = csv.reader(packagefile, delimiter=',')

    package_map = hash_table.HashMap()  # Create an instance of HashMap class
    first_truck = []  # first truck delivery
    second_truck = [] # second truck delivery
    last_truck = [] # final truck delivery

    # Insert values from csv file into key/value pairs of the hash table -> O(n)
    for row in package_data:
        package_id = row[0]
        package_address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery_requirement = row[5]
        package_weight = row[6]
        special_note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        value = [package_id, address_location, package_address, city, state, zip, delivery_requirement, package_weight, 
            special_note, delivery_start, delivery_status]

        #Conditional statements to determine which truck a package should be located and 
        #put these packages into a nested list for quick indexing

        # First truck's first delivery
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_truck.append(value)

        #ensures the package 19 is on the first truck with the packages it must be delivered with
        if value[0] == "19" :
            first_truck.append(value)

        # Second truck's delivery
        if 'Can only be' in value[8] or 'Delayed' in value[8]:
            second_truck.append(value)
        
       # Correct incorrect package detail 
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            last_truck.append(value)

        # Check remaining packages
        if value not in first_truck and value not in second_truck and value not in last_truck:
            second_truck.append(value) if len(second_truck) < len(last_truck) else last_truck.append(value)

        # Insert value into the hash table
        package_map.add(package_id, value)

    # Get packages on the first delivery -> O(1)
    def get_first_delivery():
        return first_truck

    # Get packages on the second delivery -> O(1)
    def get_second_delivery():
        return second_truck

    # Get packages on the final delivery -> O(1)
    def get_last_delivery():
        return last_truck

    # Get full list of packages -> O(1)
    def get_hash_map():
        return package_map

    def number_of_packages():
        total_packages = len(first_truck) + len(second_truck) + len(last_truck)
        return (total_packages)

    