#Devon Hooper Student ID #: 000875101

from package_data_reader import get_hash_map
from package_data_reader import number_of_packages
import packages
import datetime

class Main:
    print("*" * 25)
    print("Welcome to the WGUPS Package delivery system!")
    print("*" * 25)
    print(f'All trucks routes were completed in {packages.total_distance():.2f} miles.\n')

print("""
Please select an option below to begin or type 'exit' at any time to leave the system:
    1. Display all packages at a particular time
    2. Display a single package at a particular time
""")
user_input = input('> ')


while user_input != 'exit':
    #User selecting option 1 to display all packages at a particular time
    #has a comoplexity of O(n)
    if user_input == '1':
        try:
            user_time_input = input('Enter the time you would like to check in the format HH:MM:SS: ')
            (hrs,mins,secs) = user_time_input.split(":")
            user_time_input_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
        
            # O(N^2)       
            for count in range(1,41):
                try:
                    departure_time = get_hash_map().get(str(count))[9]
                    package_status = get_hash_map().get(str(count))[10]
                    (hrs,mins,secs) = departure_time.split(":")
                    departure_time_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
                    (hrs,mins,secs) = package_status.split(":")
                    package_status_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
                except ValueError:
                    pass

                #determine if package is still at the hub
                if departure_time_converted >= user_time_input_converted:
                    get_hash_map().get(str(count))[10] = 'At hub'
                    get_hash_map().get(str(count))[9] = 'Package leaves the hub at ' + departure_time

                    #display all packages current info
                    print(
                        f'Package ID: {get_hash_map().get(str(count))[0]}, '
                        f'Package Staus: {get_hash_map().get(str(count))[10]}'
                    )
                # Determine which packages have left but have not been delivered
                elif departure_time_converted <= user_time_input_converted:
                    if user_time_input_converted < package_status_converted:
                        get_hash_map().get(str(count))[10] = 'Package is in tranist'
                        get_hash_map().get(str(count))[9] = 'Package left the hub at ' + departure_time

                        # Print package's current info
                        print(
                            f'Package ID: {get_hash_map().get(str(count))[0]}, '
                            f'Delivery status: {get_hash_map().get(str(count))[10]}'
                            )
                    # Determine which packages have already been delivered
                    else:
                        get_hash_map().get(str(count))[10] = 'Delivered at ' + package_status
                        get_hash_map().get(str(count))[9] = 'Left at the hub at ' + departure_time

                        # Print package's current info
                        print(
                            f'Package ID: {get_hash_map().get(str(count))[0]}, '
                            f'Delivery status: {get_hash_map().get(str(count))[10]}'
                            )
        except IndexError:
            print(IndexError)
            exit()
        except ValueError:
            print('Invalid entry, please try again!')
            exit()

    #User selecting option 2 to display a particular packages at a particular time
    #has a comoplexity of O(n)
    elif user_input == '2':
        try:
            count = input(f'Enter a package ID(1 - {number_of_packages()}): ')
            departure_time = get_hash_map().get(str(count))[9]
            package_status = get_hash_map().get(str(count))[10]
            user_time_input = input('Enter the time you would like to check in the format HH:MM:SS: ')
            (hrs,mins,secs) = departure_time.split(":")
            departure_time_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
            (hrs,mins,secs) = package_status.split(":")
            package_status_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
            (hrs,mins,secs) = user_time_input.split(":")
            user_time_input_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
        
            #determine if package is still at the hub
            if departure_time_converted >= user_time_input_converted:
                    get_hash_map().get(str(count))[10] = 'At hub'
                    get_hash_map().get(str(count))[9] = 'Package leaves the hub at ' + departure_time

                    # Print package's current info
                    print(
                        f'Package ID: {get_hash_map().get(str(count))[0]}\n'
                        f'Street address: {get_hash_map().get(str(count))[2]}\n'
                        f'Required delivery time: {get_hash_map().get(str(count))[6]}\n'
                        f'Package weight: {get_hash_map().get(str(count))[7]}\n'
                        f'Truck status: {get_hash_map().get(str(count))[9]}\n'
                        f'Delivery status: {get_hash_map().get(str(count))[10]}\n'
                    )
            #Determine if the package has left but not been delivered
            elif departure_time_converted <= user_time_input_converted:
                if user_time_input_converted < package_status_converted:
                    get_hash_map().get(str(count))[10] = 'Package is in tranist'
                    get_hash_map().get(str(count))[9] = 'Package left the hub at ' + departure_time

                    print(
                        f'Package ID: {get_hash_map().get(str(count))[0]}\n'
                        f'Street address: {get_hash_map().get(str(count))[2]}\n'
                        f'Required delivery time: {get_hash_map().get(str(count))[6]}\n'
                        f'Delivery City: {get_hash_map().get(str(count))[3]}\n'
                        f'Delivery Zipcode: {get_hash_map().get(str(count))[5]}\n'
                        f'Package weight: {get_hash_map().get(str(count))[7]}\n'                        
                        f'Truck status: {get_hash_map().get(str(count))[9]}\n'
                        f'Delivery status: {get_hash_map().get(str(count))[10]}\n'
                        )
                #determine if package has already been delivered
                else:
                    get_hash_map().get(str(count))[10] = 'Package was delivered at ' + package_status
                    get_hash_map().get(str(count))[9] = 'Package left the hub at ' + departure_time

                    print(
                        f'Package ID: {get_hash_map().get(str(count))[0]}\n'
                        f'Street address: {get_hash_map().get(str(count))[2]}\n'
                        f'Required delivery time: {get_hash_map().get(str(count))[6]}\n'
                        f'Delivery City: {get_hash_map().get(str(count))[3]}\n'
                        f'Delivery Zipcode: {get_hash_map().get(str(count))[5]}\n'
                        f'Package weight: {get_hash_map().get(str(count))[7]}\n'                        
                        f'Truck status: {get_hash_map().get(str(count))[9]}\n'
                        f'Delivery status: {get_hash_map().get(str(count))[10]}\n'
                        )
        except ValueError:
                print('Invalid entry')
                exit()

        # Case 'exit'
        # This exits the program
    elif user_input == 'quit':
        exit()

        # Case Error
        # Print Invalid Entry and quit the program
    else:
        print('Invalid entry, please try again!')
        exit()