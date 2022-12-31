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
    package_data_reader.get_first_delivery()[idx][9] = first_truck_leave_time
    first_delivery.append(package_data_reader.get_first_delivery()[idx])

# this for loop compares the addresses on truck one to the list of addresses and adds the address index to the list
# Space-time complexity is O(N^2)
try:
    first_variable_count = 0
    for k in first_delivery:
        for j in distance.evaluate_address():
            if k[2] == j[2]:
                first_truck_distances.append(j[0])
                first_delivery[first_variable_count][1] = j[0]
        first_variable_count += 1
except IndexError:
    pass
# calls to the greedy algorithm that sorts the packages in a more efficient order
distance.evaluate_shortest_distance(first_delivery, 1, 0)
first_truck_total_distance = 0
