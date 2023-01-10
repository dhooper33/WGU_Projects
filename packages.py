import distance
import package_data_reader
import datetime

#dictate what time the trucks leave the hub
first_truck_leave_time = ['8:00:00']
second_truck_leave_time = ['9:10:00']
final_truck_leave_time = ['11:00:00']


first_delivery = []
first_truck_distances = []
#update the delivery_start time of packages on first_truck
for idx, value in enumerate(package_data_reader.get_first_delivery()):
    package_data_reader.get_first_delivery()[idx][7] = first_truck_leave_time[0]
    first_delivery.append(package_data_reader.get_first_delivery()[idx])

# compares the address of the packages on the first truck against the list of destination and updates 
# the address to its corresponding identifier for evaluation.
# O(N^2)
try:
    first_count = 0
    for k in first_delivery:
        for j in distance.evaluate_address():
            if k[1] == j[2]:
                first_truck_distances.append(j[0])
                first_delivery[first_count][1] = j[0]
        first_count += 1
except IndexError:
    pass
# calls the greedy algorithm tos sort the packages into the optimized order
distance.evaluate_shortest_distance(first_delivery, 1, 0)
first_truck_total_distance = 0

# this for loop excutes distance function in order to find the first trucks distance and updates the delivery status of packages.
# O(N)
first_truck_package_id = 0
for index in range(len(distance.first_truck_optimized_index())):
    try:
        first_truck_total_distance = distance.evaluate_distance(int(distance.first_truck_optimized_index()[index]), int(distance.first_truck_optimized_index()[index + 1]), first_truck_total_distance)
        deliver_package = distance.get_time(distance.evaluate_current_distance(int(distance.first_truck_optimized_index()[index]), int(distance.first_truck_optimized_index()[index + 1])), first_truck_leave_time)
        distance.first_truck_list()[first_truck_package_id][8] = (str(deliver_package))
        package_data_reader.get_hash_map().update(int(distance.first_truck_list()[first_truck_package_id][0]), first_delivery)
        first_truck_package_id += 1
    except IndexError:
        pass


second_delivery = []
second_truck_distances = []
#update the delivery_start time of packages on second_truck
# O(N)
for idx, value in enumerate(package_data_reader.get_second_delivery()):
    package_data_reader.get_second_delivery()[idx][7] = second_truck_leave_time[0]
    second_delivery.append(package_data_reader.get_second_delivery()[idx])
# compares the address of the packages on the second truck against the list of destination and updates 
# the address to its corresponding identifier for evaluation.
# O(N^2)
try:
    second_count = 0
    for k in second_delivery:
        for j in distance.evaluate_address():
            if k[1] == j[2]:
                second_truck_distances.append(j[0])
                second_delivery[second_count][1] = j[0]
        second_count += 1
except IndexError:
    pass
# calls the greedy algorithm tos sort the packages into the optimized order
distance.evaluate_shortest_distance(second_delivery, 2, 0)
second_truck_total_distance = 0

# this for loop excutes distance function in order to find the second trucks distance and updates the delivery status of packages.
# O(N)
second_truck_package_id = 0
for index in range(len(distance.second_truck_optimized_index())):
    try:
        second_truck_total_distance = distance.evaluate_distance(int(distance.second_truck_optimized_index()[index]), int(distance.second_truck_optimized_index()[index + 1]), second_truck_total_distance)
        deliver_package = distance.get_time(distance.evaluate_current_distance(int(distance.second_truck_optimized_index()[index]), int(distance.second_truck_optimized_index()[index + 1])), second_truck_leave_time)
        distance.second_truck_list()[second_truck_package_id][8] = (str(deliver_package))
        package_data_reader.get_hash_map().update(int(distance.second_truck_list()[second_truck_package_id][0]), second_delivery)
        second_truck_package_id += 1
    except IndexError:
        pass

third_delivery = []
third_truck_distances = []
#update the delivery_start time of packages on final_truck
#O(N)
for idx, value in enumerate(package_data_reader.get_third_delivery()):
    package_data_reader.get_third_delivery()[idx][7] = final_truck_leave_time[0]
    third_delivery.append(package_data_reader.get_third_delivery()[idx])
# compares the address of the packages on the third truck against the list of destination and updates 
# the address to its corresponding identifier for evaluation.
# O(N^2)
try:
    third_count = 0
    for k in third_delivery:
        for j in distance.evaluate_address():
            if k[1] == j[2]:
                third_truck_distances.append(j[0])
                third_delivery[third_count][1] = j[0]
        third_count += 1
except IndexError:
    pass

# calls the greedy algorithm tos sort the packages into the optimized order
distance.evaluate_shortest_distance(third_delivery, 3, 0)
third_truck_total_distance = 0

# this for loop excutes distance function in order to find the third trucks distance and updates the delivery status of packages.
# O(N)
third_truck_package_id = 0
for index in range(len(distance.third_truck_index())):
    try:
        # calculate the total distance of the truck
        third_truck_total_distance = distance.evaluate_distance(int(distance.third_truck_index()[index]), int(distance.third_truck_index()[index + 1]), third_truck_total_distance)
        # calculate the distance of each package along the route
        deliver_package = distance.get_time(distance.evaluate_current_distance(int(distance.third_truck_index()[index]), int(distance.third_truck_index()[index + 1])), final_truck_leave_time)
        distance.third_truck_list()[third_truck_package_id][8] = (str(deliver_package))
        package_data_reader.get_hash_map().update(int(distance.third_truck_list()[third_truck_package_id][0]), third_delivery)
        third_truck_package_id += 1
    except IndexError:
        pass


#returns the total distance that all trucks have traveled
def total_distance():
    total_distance = first_truck_total_distance + second_truck_total_distance + third_truck_total_distance
    return total_distance





