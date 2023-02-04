# Phillip Sanchez ID #001301444

import csv
import datetime

from hashmap import HashMap
from package import Packages
from truck import Truck
from util import distance_between, convert_address, convert_delivery_status, update_truck_and_package, reset_address, \
    update_address


# Time + Space complexity of O(n)
# Method loads the package data, creates an instance of the Packages object and adds them into our hash table.
def load_package_data(data_file, hash_name):
    # Reads the package_data csv file.
    with open(data_file) as pd:
        package_data = csv.reader(pd)
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_zipcode = package[3]
            p_state = package[4]
            p_deadline = package[5]
            p_weight = package[6]
            p_notes = package[7]
            p_status = 'Hub'
            p_time_delivered = ''
            p_start_time = ''

            # Passing the package_data into the Package object.
            p = Packages(p_id, p_address, p_city, p_zipcode, p_state, p_deadline, p_weight, p_notes, p_status,
                         p_time_delivered, p_start_time)
            # Insert the Package instances into the hash table.
            hash_name.insert(p_id, p)


# Define the HashMap.
package_hash = HashMap()
# Load the packages by taking in the package_data csv path and the HashMap we defined as arguments.
load_package_data('data/package_data.csv', package_hash)

# Creating instances of our Truck class and manually load the packages.
# Truck(capacity, mileage, [packages id], location, departure).
truck_1 = Truck(16, 0, 18, [12, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], '4001 South 700 East', '',
                datetime.timedelta(hours=8, minutes=00))
truck_2 = Truck(16, 0, 18, [9, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 18, 36, 38], '4001 South 700 East', '',
                datetime.timedelta(hours=9, minutes=10))
truck_3 = Truck(16, 0, 18, [17, 21, 22, 23, 24, 25, 26, 27, 28, 32, 33, 35, 39], '4001 South 700 East', '',
                datetime.timedelta(hours=10, minutes=30))


# C2 Example of process and flow comments.
# Time + Space complexity of O(n^2)
# Method to deliver the packages using the Nearest Neighbor Algorithm.
def deliver(truck):
    # Create an empty array.
    undelivered_queue = []
    # Iterate through the packages (manually added as an id) and add them to the empty array.
    for pid in truck.packages:
        # Search for the key in the hash table using the lookup method and the package ID. Then assign it to package.
        package = package_hash.lookup(pid)
        # Change the status of the package.
        package.status = 'EN ROUTE'
        # Add the packages into the undelivered array.
        undelivered_queue.append(package)

    # Continue looping until the undelivered queue is 0 (has no packages).
    while len(undelivered_queue) > 0:
        # Start with infinity to find the lowest/min.
        nearest_address = float('inf')
        # Loop through the length of the undelivered queue.
        for i in range(0, len(undelivered_queue)):
            # Assign variables for cleaner code.
            truck_location = truck.location
            package_delivery_location = undelivered_queue[i].address
            package = undelivered_queue[i]
            # Finds the distance between two points by converting the truck and package locations into the address IDs.
            # Once complete, the distance between method will locate the distance between the two points in the hubs
            # csv file.
            distance_conversion = distance_between(convert_address(truck_location),
                                                   convert_address(package_delivery_location))
            # If the distance between two points is less than or equal to the nearest address found:
            if distance_conversion <= nearest_address:
                # Update the nearest address to the new shortest distance.
                nearest_address = distance_conversion
                # Update the package of the shortest distance.
                next_package = package
        # Update the truck and packages data like status, delivery times, locations, etc.
        update_truck_and_package(truck, next_package, nearest_address)
        # Remove the package delivered from the queue.
        undelivered_queue.remove(next_package)


# Deliver the packages.
deliver(truck_1)
deliver(truck_2)
deliver(truck_3)


# G. Interface.
class Main:
    print('WELCOME TO THE WGU PACKAGING SYSTEM')
    # Loop until user selects an option.
    isExit = True
    while isExit:
        print('-------------------------------------------------------')
        print('                     OPTIONS')
        print('-------------------------------------------------------')
        # Displays the truck delivery miles and times.
        print('1, GET TRIP INFORMATION.')
        # Displays the status of one package based on the time and package id the user inputs.
        print('2, CHECK THE STATUS OF A GIVEN PACKAGE AT A GIVEN TIME.')
        # Displays the status of all packages based on the time the user inputs.
        print('3, CHECK THE STATUS OF ALL PACKAGES AT A GIVEN TIME.')
        # Exits the system.
        print('4, EXIT THE SYSTEM.')
        print('-------------------------------------------------------')
        option = input('           CHOOSE AM OPTION (1,2,3 OR 4):')
        print('-------------------------------------------------------')
        if option == '1':
            print('-------------------------------------------------------')
            print('                   TRUCK DATA')
            print('-------------------------------------------------------')
            print('TRUCK 1: ')
            print('       MILEAGE: ' + str(truck_1.mileage))
            print('       TIME:    ' + str(truck_1.delivery_time - truck_1.departure_time))
            print('TRUCK 2: ')
            print('       MILEAGE: ' + str(truck_2.mileage))
            print('       TIME:    ' + str(truck_2.delivery_time - truck_2.departure_time))
            print('TRUCK 3: ')
            print('       MILEAGE: ' + str(truck_3.mileage))
            print('       TIME:    ' + str(truck_3.delivery_time - truck_3.departure_time))
            print('-------------------------------------------------------')
            print('TOTAL MILEAGE:         ' + str(round(truck_1.mileage + truck_2.mileage + truck_3.mileage, 2)))
            print('TOTAL DELIVERY TIME:   ' + str((truck_1.delivery_time - truck_1.departure_time)
                                                  + (truck_2.delivery_time - truck_2.departure_time)
                                                  + (truck_3.delivery_time - truck_3.departure_time)))
        elif option == '2':
            try:
                # Stores the users input of id and time to search for.
                user_package = int(input('ENTER A VALID PACKAGE ID# (1-40): '))
                user_time = input('ENTER A TIME in 24HR FORMAT. (HH:MM:SS):')
                # If the user enters a number out of the range from 1-41, an error will occur.
                if 0 >= user_package or user_package >= 41:
                    print('**** INVALID VALUE. ENTER A PACKAGE ID (1-40) AND TIME IN HH:MM:SS FORMAT. ****')
                else:
                    # Converts the users time from datetime to deltatime to minutes to later compare vs the users input.
                    # Will help with conversion
                    user_time_datetime = datetime.datetime.strptime(user_time, '%H:%M:%S')
                    user_time_delta = datetime.timedelta(hours=user_time_datetime.hour,
                                                         minutes=user_time_datetime.minute,
                                                         seconds=user_time_datetime.second)
                    user_time_minutes = int(user_time_delta / datetime.timedelta(minutes=1))
                    print('-------------------------------------------------------')
                    print(f'         YOU ENTERED ID: {user_package} TIME:{user_time_delta}')
                    print('-------------------------------------------------------')
                    try:
                        # Searches for the package using the HashMap lookup method and the package id.
                        package_gui = package_hash.lookup(user_package)

                        # Resets and updates package 9s wrong address.
                        reset_address(package_gui, 9)
                        update_address(user_time_delta, package_gui)

                        # Convert time delivered from string to datetime, to deltatime to minutes so we can compare.
                        time_delivered = package_gui.time_delivered
                        t = datetime.datetime.strptime(time_delivered, '%H:%M:%S')
                        time_delivered_delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                        time_delivered_minutes = int(time_delivered_delta / datetime.timedelta(minutes=1))

                        # Convert start time into minutes.
                        start_time = package_gui.start_time
                        start_time_minutes = int(package_gui.start_time / datetime.timedelta(minutes=1))

                        # Change the delivery status based on users input using convert_delivery_status method.
                        convert_delivery_status(start_time_minutes, user_time_minutes, time_delivered_minutes,
                                                package_gui)
                        # Print the results.
                        print(
                            str(f'ID: {package_gui.p_id} | WEIGHT: {package_gui.weight} | DEADLINE: {package_gui.deadline} | EXPECTED DELIVERY:'
                                f'{package_gui.time_delivered} | STATUS: {package_gui.status}'))
                        print(
                            str(f'START TIME: {package_gui.start_time} | ADDRESS: {package_gui.address, package_gui.city, package_gui.zipcode, package_gui.state} '))
                    except ValueError:
                        print('')
                        print('**** SYSTEM ERROR ****')
                        print('')
            except ValueError:
                print('')
                print('**** INVALID VALUE. ENTER A PACKAGE ID (1-40) AND TIME IN HH:MM:SS FORMAT. ****')
                print('')

        elif option == '3':

            try:
                # Stores the users input of the time to search for.
                user_time = input('ENTER A TIME in 24HR FORMAT. (HH:MM:SS)')
                # Converts the users time from datetime to deltatime to minutes to later compare vs the users input.
                # Will help with conversion
                user_time_datetime = datetime.datetime.strptime(user_time, '%H:%M:%S')
                user_time_delta = datetime.timedelta(hours=user_time_datetime.hour, minutes=user_time_datetime.minute,
                                                     seconds=user_time_datetime.second)
                user_time_minutes = int(user_time_delta / datetime.timedelta(minutes=1))
                print('-------------------------------------------------------')
                print(f'               TIME ENTERED: {user_time_delta}')
                print('-------------------------------------------------------')

                # Time complexity of O(n) -- For loop O(n)
                for i in range(1, len(package_hash.table) + 1):
                    try:
                        # Searches for the package using the HashMap lookup method and the package id.
                        package_gui = package_hash.lookup(i)

                        # Resets and updates package 9s wrong address.
                        reset_address(package_gui, 9)
                        update_address(user_time_delta, package_gui)

                        # Convert time delivered from string to datetime, to deltatime to minutes so we can compare.
                        time_delivered = package_gui.time_delivered
                        t = datetime.datetime.strptime(time_delivered, '%H:%M:%S')
                        time_delivered_delta = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
                        time_delivered_minutes = int(time_delivered_delta / datetime.timedelta(minutes=1))

                        # Convert start time into minutes.
                        start_time = package_gui.start_time
                        start_time_minutes = int(package_gui.start_time / datetime.timedelta(minutes=1))

                        # Change the delivery status based on users input using convert_delivery_status method.
                        convert_delivery_status(start_time_minutes, user_time_minutes, time_delivered_minutes,
                                                package_gui)
                        # Print the results.
                        print(
                            str(f'ID: {package_gui.p_id} | WEIGHT: {package_gui.weight} | DEADLINE: {package_gui.deadline} | EXPECTED DELIVERY: '
                                f'{package_gui.time_delivered} | STATUS: {package_gui.status}'))
                        print(
                            str(f'START TIME: {package_gui.start_time} | ADDRESS: {package_gui.address, package_gui.city, package_gui.zipcode, package_gui.state} '))
                    except ValueError:
                        print('')
                        print('**** SYSTEM ERROR ****')
                        print('')
            except ValueError:
                print('')
                print('**** INVALID VALUE. ENTER IN HH:MM:SS FORMAT. ****')
                print('')
        elif option == '4':
            # Print GOODBYE and exit the program
            print('GOODBYE')
            isExit = False
        else:
            print('INVALID OPTION. TRY AGAIN.')
