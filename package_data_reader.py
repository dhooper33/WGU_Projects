import csv
import hash_table

# Read CSV files
with open('./delivery_data/WGUPSpackage_data.csv') as packagefile:
    package_data = csv.reader(packagefile, delimiter=',')

    #Create delivery trucks
    first_delivery_truck = []
    second_delivery_truck = []
    third_delivery_truck = []

    #create hash map instance for the package data
    package_map = hash_table.hash_map()
    
    #associate data in column to a variable
    for column in package_data:
        package_id = column[0]
        delivery_address = column[1]
        delivery_deadline = column[5]
        delivery_city = column[2]
        delivery_state = column [3]
        delivery_zip = column[4]
        package_weight = column[6]
        delivery_requirements = column[7]
        #extra items to add to each entry for package tracking
        departure_time = ''
        delivery_status = 'At Hub'

        #place all column data into one value list to use as part of the key/value pair for the hash table
        value = [package_id, #value[0]
                delivery_address, #value[1]
                delivery_deadline, #value[2]
                delivery_city, #value[3]
                delivery_zip, #value[4]
                package_weight, #value[5]
                delivery_requirements, #value[6]
                departure_time, #value[7]
                delivery_status, #value[8]
                delivery_state]

        #Creating conditional statments to sort trucks and determine which packages should go on each truck
        #based on delivery deadlines and requirements

        #ensures that packages that have a set delivery time are on the first truck along with any 
        #packages that have to be delivered together
        if value[2] != 'EOD':
            if 'Must' in value[6] or 'None' in value[6]:
                first_delivery_truck.append(value)

        #ensures the package 19 is on the first truck with the packages it must be delivered with
        if value[0] == "19" :
            first_delivery_truck.append(value)

        #ensures that packages that can only be on truck 2 and any delayed packages are
        #on the second delivery truck
        if 'Can only be' in value[6] or 'Delayed' in value[6]:
            second_delivery_truck.append(value)
        
       # Update incorrect package information
        if 'Wrong address listed' in value[6]:
            value[1] = '410 S State St'
            value[4] = '84111'
            third_delivery_truck.append(value)

        # Check remaining packages are loaded while trying to split the load between the second and third delivery trucks
        if value not in first_delivery_truck and value not in second_delivery_truck and value not in third_delivery_truck:
            second_delivery_truck.append(value) if len(second_delivery_truck) < len(third_delivery_truck) else third_delivery_truck.append(value)
        
        # Insert key and value into the hash table
        package_map.add(package_id, value)

    # returns the packages on the first delivery truck
    # O(1)
    def get_first_delivery():
        return first_delivery_truck

    # returns the packages on the second delivery truck
    # O(1)
    def get_second_delivery():
        return second_delivery_truck

    # returns the packages on the third delivery truck
    # O(1)
    def get_third_delivery():
        return third_delivery_truck

    # return full list of packages
    # O(1)
    def get_hash_map():
        return package_map

    #Determines the total numebr of packages being delivered
    #O(N)
    def number_of_packages():
        total_packages = len(first_delivery_truck) + len(second_delivery_truck) + len(third_delivery_truck)
        return (total_packages)

