import csv
import datetime

#Reading data from CSV files
with open('./delivery_data/WGUPSdistance_data.csv') as distancecsv:
   distance_csv = list(csv.reader(distancecsv, delimiter=','))
with open('./delivery_data/WGUPSdestination_name_data.csv') as destinationcsv:
    destination_name_csv = list(csv.reader(destinationcsv, delimiter=','))


# Calculate the total distance from a list of row/column values -> O(1)
    def evaluate_distance(row_value, column_value, total):
        distance = distance_csv[row_value][column_value]
        if distance == '':
            distance = distance_csv[column_value][row_value]

        total += float(distance)
        return total

# Calculate the current distance from row/column values -> O(1)
    def evaluate_current_distance(row_value, column_value):
        distance = distance_csv[row_value][column_value]
        if distance == '':
            distance = distance_csv[column_value][row_value]
        return float(distance)
    # this is the time that the first truck leaves the hub
    first_time_list = ['8:00:00']
    second_time_list = ['9:10:00']
    third_time_list = ['11:00:00']

    # Calculate total distance for a given truck based on its distance divied by the 18 mph average speed contraint for each truck -> O(n)
    def get_time(distance, truck_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs),
                                        minutes=int(mins), seconds=int(secs))
        return total
    
   # Get package address data -> O(n)
    def evaluate_address():
        return destination_name_csv

        # these lists represent the sorted trucks that are put in order of efficiency in the function below
    first_truck = []
    first_truck_indices = []
    second_truck = []
    second_truck_indices = []
    third_truck = []
    third_truck_indices = []

    # NEED TO UPDATE ALL OF THIS:
    # The following algorithm uses the 'greedy approach'. This is
    # because the algorithm uses a recursive technique to determine the
    # best location to visit next based on the current location. 

    # This algorithm contains 3 parameters:
    # 1. List of packages
    # 2. Truck number
    # 3. Current location of the truck

    # The purpose of the first for loop is to find the shortest distance
    # to the next location. The lowest_value will continually change until
    # a minimum value is found. 

    # The second for loop dictates what happens when the lowest_value has
    # been determined. Conditionally statements check to see which truck
    # the package is associated with. Values are then appended to the 
    # appropriate truck lists. The current package is taken out of the list
    # and the current location moves to the next optimal location
    # determined from the first loop. Lastly, a recursive call is made
    # for the next location and shortened list. Recursive calls will
    # continually be made until the base case is called, which will
    # end the function and return the now empty list. 

    # Base Case: Length of the list is False, or zero. 

    # Space-Time Complexity -> O(n^2)

    def evaluate_shortest_distance(truck_list, truck_num, current_truck_location):
        if not len(truck_list):
            return truck_list

        shortest_distance = 50.0
        location = 0

        for idx in truck_list:
            value = int(idx[1])
            if evaluate_current_distance(current_truck_location, value) <= shortest_distance:
                shortest_distance = evaluate_current_distance(
                    current_truck_location, value)
                location = value

        for idx in truck_list:
            if evaluate_current_distance(current_truck_location, int(idx[1])) == shortest_distance:
                if truck_num == 1:
                    first_truck.append(idx)
                    first_truck_indices.append(idx[1])
                    truck_list.pop(truck_list.index(idx))
                    current_truck_location = location
                    evaluate_shortest_distance(truck_list, 1, current_truck_location)
                elif truck_num == 2:
                    second_truck.append(idx)
                    second_truck_indices.append(idx[1])
                    truck_list.pop(truck_list.index(idx))
                    current_truck_location = location
                    evaluate_shortest_distance(truck_list, 2, current_truck_location)
                elif truck_num == 3:
                    third_truck.append(idx)
                    third_truck_indices.append(idx[1])
                    truck_list.pop(truck_list.index(idx))
                    current_truck_location = location
                    evaluate_shortest_distance(truck_list, 3, current_truck_location)

    # Insert 0 for the first index of each index list
    first_truck_indices.insert(0, '0')
    second_truck_indices.insert(0, '0')
    third_truck_indices.insert(0, '0')

    # The following are all helper functions to return a desired value -> O(1)
    def first_truck_index():
        return first_truck_indices

    def first_truck_list():
        return first_truck

    def second_truck_index():
        return second_truck_indices

    def second_truck_list():
        return second_truck

    def third_truck_index():
        return third_truck_indices

    def third_truck_list():
        return third_truck

