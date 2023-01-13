import csv
import datetime

with open('./delivery_data/WGUPSdistance_data.csv') as distancecsv:
    distance_data_csv = list(csv.reader(distancecsv, delimiter=','))
with open('./delivery_data/WGUPSdestination_name_data.csv') as destinationcsv:
    destination_name_csv = list(csv.reader(destinationcsv, delimiter=','))


# used to find total distance of a truck
# O(1)
    def evaluate_distance(row_value, column_value, total):
        distance = distance_data_csv[row_value][column_value]
        if distance == '':
            distance = distance_data_csv[column_value][row_value]

        total += float(distance)
        return total

# used to find the current distance that a truck has traveled
# O(1)
    def evaluate_current_distance(row_value, column_value):
        distance = distance_data_csv[row_value][column_value]
        if distance == '':
            distance = distance_data_csv[column_value][row_value]
        return float(distance)


    # uses distance of truck divied by the 18 mph average speed contraint to updated trucks travel times
    # O(n)
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
    
   # helpful to call the package address data 
   # O(n)
    def evaluate_address():
        return destination_name_csv

    # these lists will hold the optimized order of package deliveries from the function 
    first_truck_optimized = []
    second_truck_optimized = []
    third_truck_optimized = []

    # these lists will keep track of the distance_data indices for the optimized delivery list.
    first_truck_optimal_indices_list = []
    second_truck_optimal_indices_list = []
    third_truck_optimal_indices_list = []

    # The algorithm below applies a 'greedy approach" by using a recursive technique to utilize the current location to 
    # determine the best location travel to next

    # This algorithm uses the list of packages on a truck, Truck number, and Current location of the truck as parameters

    # the first for loop will go through to find the shortest distance to the next location in the package list.
    # The shortest_distance variable will continually update until the lowest value is found.

    # The second for loop declares what to do after the shortest_distance has been determined. 
    # The conditionally statements check to see which truck the package is on and the values are 
    # then appended to the corresponding truck lists. That package is then removed from the list
    # and the current_truck_location moves to the next optimal location
    # that was determined from the first loop. 
    # 
    # a recursive call is made for the next location and the new list of packages. This will continue until all packages
    # have been delivered.
    # O(n^2)

    def evaluate_shortest_distance(truck_list, truck_num, current_truck_location):
        
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
                    first_truck_optimized.append(idx)
                    first_truck_optimal_indices_list.append(idx[1])
                    truck_list.pop(truck_list.index(idx))
                    current_truck_location = location
                    evaluate_shortest_distance(truck_list, 1, current_truck_location)
                elif truck_num == 2:
                    second_truck_optimized.append(idx)
                    second_truck_optimal_indices_list.append(idx[1])
                    truck_list.pop(truck_list.index(idx))
                    current_truck_location = location
                    evaluate_shortest_distance(truck_list, 2, current_truck_location)
                elif truck_num == 3:
                    third_truck_optimized.append(idx)
                    third_truck_optimal_indices_list.append(idx[1])
                    truck_list.pop(truck_list.index(idx))
                    current_truck_location = location
                    evaluate_shortest_distance(truck_list, 3, current_truck_location)
   
 
    # Insert 0 for the first index of each index list so that all will start at the hub
    first_truck_optimal_indices_list.insert(0, '0')
    second_truck_optimal_indices_list.insert(0, '0')
    third_truck_optimal_indices_list.insert(0, '0')

    # Helpful function to call on for obtaining data  
    # O(1)
    def first_truck_optimized_index():
        return first_truck_optimal_indices_list

    # O(1)
    def first_truck_list():
        return first_truck_optimized

    # O(1)
    def second_truck_optimized_index():
        return second_truck_optimal_indices_list

    # O(1)
    def second_truck_list():
        return second_truck_optimized

    # O(1)
    def third_truck_index():
        return third_truck_optimal_indices_list

    # O(1)
    def third_truck_list():
        return third_truck_optimized



