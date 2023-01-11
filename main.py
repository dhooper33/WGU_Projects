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
    print(f'Truck 1 traveled a total distanced of: {round(packages.first_truck_total_distance, 1)}')
    print(f'Truck 2 traveled a total distanced of: {round(packages.second_truck_total_distance, 1)}')
    print(f'Truck 3 traveled a total distanced of: {round(packages.third_truck_total_distance, 1)}\n')

main_menu = """
Please select an option below or type 'exit' at any time to leave the system:
    1. Display all packages at a particular time
    2. Display a single package at a particular time
"""
print('-'*90)
print(main_menu)
user_input = input('> ').lower()


while user_input != 'exit':
    #User selecting option 1 to display all packages at a particular time
    #O(N)
    if user_input == '1':
        try:
            user_time_input = input('Enter the time you would like to check in the format HH:MM:SS: ').lower()
            (hrs,mins,secs) = user_time_input.split(":")
            user_time_input_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
        
            # O(N^2)       
            for count in range(1,41):
                try:
                    departure_time = get_hash_map().get(str(count))[7]
                    (hrs,mins,secs) = departure_time.split(":")
                    departure_time_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
                    package_status = get_hash_map().get(str(count))[8]
                    (hrs,mins,secs) = package_status.split(":")
                    package_status_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
                except ValueError:
                    pass

                #determine if packages are still at the hub
                if departure_time_converted >= user_time_input_converted:
                    get_hash_map().get(str(count))[8] = 'At hub'
                    get_hash_map().get(str(count))[7] = 'Package leaves the hub at ' + departure_time

                    #displays the pertinent information of all packages
                    print(
                        f'Package ID -- {get_hash_map().get(str(count))[0]}:\n '
                        f'\tRequired delivery time: {get_hash_map().get(str(count))[2]} \n\t'
                        f'Package Staus: {get_hash_map().get(str(count))[8]}\n '
                        f'\tDelivery Note: {get_hash_map().get(str(count))[7]}'
                        )
                # determine which packages have left the hub but have not been delivered
                elif departure_time_converted <= user_time_input_converted:
                    if user_time_input_converted < package_status_converted:
                        get_hash_map().get(str(count))[8] = 'Package is in tranist'
                        get_hash_map().get(str(count))[7] = 'Package left the hub at ' + departure_time

                        #displays the pertinent information of all packages
                        print(
                            f'Package ID -- {get_hash_map().get(str(count))[0]}:\n '
                            f'\tRequired delivery time: {get_hash_map().get(str(count))[2]} \n\t'
                            f'Package Staus: {get_hash_map().get(str(count))[8]}\n '
                            f'\tDelivery Note: {get_hash_map().get(str(count))[7]}'
                            )
                    # determine which packages have already been delivered
                    else:
                        get_hash_map().get(str(count))[8] = 'Delivered at ' + package_status

                        # Print package's current info
                        print(
                            f'Package ID -- {get_hash_map().get(str(count))[0]}:\n '
                            f'\tRequired delivery time: {get_hash_map().get(str(count))[2]} \n\t'
                            f'Package Staus: {get_hash_map().get(str(count))[8]} '
                            )
            
        # Presents users with options for what they would like to do next
            print('-'*90)
            print("""
Please select an option below to begin or type 'exit' to leave the system:
    1. Search for another time
    2. Return to main menu

*** Invalid selections will automatically return you to the main menu ***
""")
            next_user_selection = input('> ').lower()
            
            if next_user_selection == '1':
                user_input == '1'
            elif next_user_selection == 'exit':
                user_input = next_user_selection
            else:
                print('-'*90)
                print(main_menu)
                user_input = input('> ')
             
        except ValueError:
            if user_time_input == 'exit':
                break
            else:
                print('\nInvalid entry, please try again!\n')
        
    #User selecting option 2 to display a particular packages at a particular time
    #O(n)
    elif user_input == '2':
        try:
            count = input(f'Enter a package ID(1 - {number_of_packages()}): ')
            departure_time = get_hash_map().get(str(count))[7]
            (hrs,mins,secs) = departure_time.split(":")
            departure_time_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
            package_status = get_hash_map().get(str(count))[8]
            (hrs,mins,secs) = package_status.split(":")
            package_status_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
            user_time_input = input('Enter the time you would like to check in the format HH:MM:SS: ')
            (hrs,mins,secs) = user_time_input.split(":")
            user_time_input_converted = datetime.timedelta(hours=int(hrs), minutes=(int(mins)), seconds=(int(secs)))
        
            #determine if package is still at the hub
            if departure_time_converted >= user_time_input_converted:
                    get_hash_map().get(str(count))[8] = 'At hub'
                    get_hash_map().get(str(count))[7] = 'Package leaves the hub at ' + departure_time

                    # Prints all information for the selected package
                    print(
                        '\n***************************************************\n' 
                        f'Package ID: {get_hash_map().get(str(count))[0]}\n'
                        f'Street address: {get_hash_map().get(str(count))[1]}\n'
                        f'Required delivery time: {get_hash_map().get(str(count))[2]}\n'
                        f'Delivery City: {get_hash_map().get(str(count))[3]}\n'
                        f'Delivery Zipcode: {get_hash_map().get(str(count))[4]}\n'
                        f'Package weight: {get_hash_map().get(str(count))[5]}\n'
                        f'Truck status: {get_hash_map().get(str(count))[7]}\n'
                        f'Delivery status: {get_hash_map().get(str(count))[8]}\n'
                        '***************************************************' 
                         )
             # determine which packages have left the hub but have not been delivered
            elif departure_time_converted <= user_time_input_converted:
                if user_time_input_converted < package_status_converted:
                    get_hash_map().get(str(count))[8] = 'Package is in tranist'
                    get_hash_map().get(str(count))[7] = 'Package left the hub at ' + departure_time

                    # Prints all information for the selected package
                    print(
                        '\n***************************************************\n' 
                        f'Package ID: {get_hash_map().get(str(count))[0]}\n'
                        f'Street address: {get_hash_map().get(str(count))[1]}\n'
                        f'Required delivery time: {get_hash_map().get(str(count))[2]}\n'
                        f'Delivery City: {get_hash_map().get(str(count))[3]}\n'
                        f'Delivery Zipcode: {get_hash_map().get(str(count))[4]}\n'
                        f'Package weight: {get_hash_map().get(str(count))[5]}\n'
                        f'Truck status: {get_hash_map().get(str(count))[7]}\n'
                        f'Delivery status: {get_hash_map().get(str(count))[8]}\n'
                        '***************************************************' 
                        )
                #determine if package has already been delivered
                else:
                    get_hash_map().get(str(count))[8] = 'Package was delivered at ' + package_status
                    get_hash_map().get(str(count))[7] = 'Package left the hub at ' + departure_time

                    # Prints all information for the selected package
                    print(
                        '\n***************************************************\n' 
                        f'Package ID: {get_hash_map().get(str(count))[0]}\n'
                        f'Street address: {get_hash_map().get(str(count))[1]}\n'
                        f'Required delivery time: {get_hash_map().get(str(count))[2]}\n'
                        f'Delivery City: {get_hash_map().get(str(count))[3]}\n'
                        f'Delivery Zipcode: {get_hash_map().get(str(count))[4]}\n'
                        f'Package weight: {get_hash_map().get(str(count))[5]}\n'
                        f'Truck status: {get_hash_map().get(str(count))[7]}\n'
                        f'Delivery status: {get_hash_map().get(str(count))[8]}\n'
                        '***************************************************' 
                        )
            
        # Presents users with options for what they would like to do next
            print('-'*90)
            print("""
Please select an option below to begin or type 'exit' to leave the system:
    1. Search for another time
    2. Return to main menu

*** Invalid selections will automatically return you to the main menu ***
""")
            next_user_selection = input('> ').lower()
            
            if next_user_selection == '1':
                user_input == '1'
            elif next_user_selection == 'exit':
                user_input = next_user_selection
            else:
                print('-'*90)
                print(main_menu)
                user_input = input('> ')
        except ValueError:
            if count == 'exit':
                break
            # elif user_time_input == 'exit':
            #     print('\nHave a great day!\n')
            #     break 
            else:
                print('\nInvalid entry, please try again!\n')
        except TypeError:
            print(f'\nPlease select a valid ID between 1 & {number_of_packages()}: ')

        # Print Invalid Entry and quit the program
    else:
        user_input = input('Invalid entry, please try again! > ')
        

print ('\nHave a great day!\n')