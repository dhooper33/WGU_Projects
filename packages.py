import distance
import package_data_reader
import datetime

#empty delievery lists created
first_delivery = []
second_delivery = []
third_delivery = []
first_truck_distances = []
second_truck_distances = []
third_truck_distances = []

#dictate what time the trucks leave the hub
first_truck_leave_time = ['8:00:00']
second_truck_leave_time = ['9:10:00']
final_truck_leave_time = ['11:00:00']

#update the delivery_start time of packages on first_truck
for idx, value in enumerate(package_data_reader.get_first_delivery()):
    package_data_reader.get_first_delivery()[idx][9] = first_truck_leave_time[0]
    first_delivery.append(package_data_reader.get_first_delivery()[idx])


# this for loop compares the addresses on truck one to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    first_count = 0
    for k in first_delivery:
        for j in distance.evaluate_address():
            if k[2] == j[2]:
                first_truck_distances.append(j[0])
                first_delivery[first_count][1] = j[0]
        first_count += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
distance.evaluate_shortest_distance(first_delivery, 1, 0)
first_truck_total_distance = 0

# this for loop takes the values in the first truck and runs them through the distance functions in the Distances.py file
# Space-time complexity is O(N)
first_truck_package_id = 0
for index in range(len(distance.first_truck_index())):
    try:
        # calculate the total distance of the truck
        first_truck_total_distance = distance.evaluate_distance(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index + 1]), first_truck_total_distance)
        # calculate the distance of each package along the route
        deliver_package = distance.get_time(distance.evaluate_current_distance(int(distance.first_truck_index()[index]), int(distance.first_truck_index()[index + 1])), first_truck_leave_time)
        distance.first_truck_list()[first_truck_package_id][10] = (str(deliver_package))
        package_data_reader.get_hash_map().update(int(distance.first_truck_list()[first_truck_package_id][0]), first_delivery)
        first_truck_package_id += 1
    except IndexError:
        pass


#update the delivery_start time of packages on second_truck
for idx, value in enumerate(package_data_reader.get_second_delivery()):
    package_data_reader.get_second_delivery()[idx][9] = second_truck_leave_time[0]
    second_delivery.append(package_data_reader.get_second_delivery()[idx])

try:
    second_count = 0
    for k in second_delivery:
        for j in distance.evaluate_address():
            if k[2] == j[2]:
                second_truck_distances.append(j[0])
                second_delivery[second_count][1] = j[0]
        second_count += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
distance.evaluate_shortest_distance(second_delivery, 2, 0)
second_truck_total_distance = 0

# this for loop takes the values in the first truck and runs them through the distance functions in the Distances.py file
# Space-time complexity is O(N)
second_truck_package_id = 0
for index in range(len(distance.second_truck_index())):
    try:
        # calculate the total distance of the truck
        second_truck_total_distance = distance.evaluate_distance(int(distance.second_truck_index()[index]), int(distance.second_truck_index()[index + 1]), second_truck_total_distance)
        # calculate the distance of each package along the route
        deliver_package = distance.get_time(distance.evaluate_current_distance(int(distance.second_truck_index()[index]), int(distance.second_truck_index()[index + 1])), second_truck_leave_time)
        distance.second_truck_list()[second_truck_package_id][10] = (str(deliver_package))
        package_data_reader.get_hash_map().update(int(distance.second_truck_list()[second_truck_package_id][0]), second_delivery)
        second_truck_package_id += 1
    except IndexError:
        pass

for idx, value in enumerate(package_data_reader.get_last_delivery()):
    package_data_reader.get_last_delivery()[idx][9] = final_truck_leave_time[0]
    third_delivery.append(package_data_reader.get_last_delivery()[idx])

try:
    third_count = 0
    for k in third_delivery:
        for j in distance.evaluate_address():
            if k[2] == j[2]:
                third_truck_distances.append(j[0])
                third_delivery[third_count][1] = j[0]
        third_count += 1
except IndexError:
    pass

# calls to the greedy algorithm that sorts the packages in a more efficient order
distance.evaluate_shortest_distance(third_delivery, 3, 0)
third_truck_total_distance = 0

# this for loop takes the values in the first truck and runs them through the distance functions in the Distances.py file
# Space-time complexity is O(N)
third_truck_package_id = 0
for index in range(len(distance.third_truck_index())):
    try:
        # calculate the total distance of the truck
        third_truck_total_distance = distance.evaluate_distance(int(distance.third_truck_index()[index]), int(distance.third_truck_index()[index + 1]), third_truck_total_distance)
        # calculate the distance of each package along the route
        deliver_package = distance.get_time(distance.evaluate_current_distance(int(distance.third_truck_index()[index]), int(distance.third_truck_index()[index + 1])), final_truck_leave_time)
        distance.third_truck_list()[third_truck_package_id][10] = (str(deliver_package))
        package_data_reader.get_hash_map().update(int(distance.third_truck_list()[third_truck_package_id][0]), third_delivery)
        third_truck_package_id += 1
    except IndexError:
        pass

def total_distance():
    total_distance = first_truck_total_distance + second_truck_total_distance + third_truck_total_distance
    return total_distance





