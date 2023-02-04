import csv
import datetime


# Time + Space complexity of O(1)
# Method to find the distance between two points from the distance between csv file.
def distance_between(x, y):
    # Reads the distance_between csv file.
    with open('data/distance_between.csv') as db:
        distance_between_data = list(csv.reader(db, delimiter=","))
    # Set distance equal to the distance between two points.
    distance = distance_between_data[y][x]
    # If empty:
    if distance == '':
        # Swap the points to read the position [y][x] as [x][y].
        distance = distance_between_data[x][y]
    # Return the distance as a float.
    return float(distance)


# Time complexity of O(n) + Space complexity of O(1).
# Method to convert an address to its id in the hubs csv file.
def convert_address(address):
    # Read the distance_between hubs file.
    with open('data/hubs.csv') as hub:
        hub_data = list(csv.reader(hub, delimiter=","))
    # Loop through the data.
    for hubs in hub_data:
        # If the address is in row 2 of the hubs file.
        if address in hubs[2]:
            # Return id as an int.
            return int(hubs[0])


# Time + Space complexity of O(1)
# Method to change the delivery status based off the time the user inputs.
def convert_delivery_status(start_time, user_time, time_delivered, package):
    # Start time is less than or equal to user's input time:
    if start_time <= user_time:
        # If time delivered is less than or equal to user's input time:
        if time_delivered <= user_time:
            # Set status to DELIVERED
            package.status = 'DELIVERED'
        # If time delivered is less than or equal to start time:
        elif time_delivered >= start_time:
            # Set status to EN ROUTE
            package.status = 'EN ROUTE'
    else:
        # Set status to HUB
        package.status = 'HUB'


# Time + Space complexity of O(1).
# Method to update the truck's location, miles, delivery time and the package's status.
def update_truck_and_package(truck, package, address):
    truck.location = package.address
    truck.mileage += address
    time_change = datetime.timedelta(hours=address / truck.speed)
    truck.delivery_time += time_change
    package.time_delivered = str(truck.delivery_time)
    package.status = 'DELIVERED AT:'
    package.start_time = truck.departure_time


# Time + Space complexity of O(1)
# Resets the address back to the incorrect address if the time is before 10:20 in the GUI.
def reset_address(package, p_id):
    # If the package is equal to package 9:
    if package.p_id == p_id:
        # Reset the address to the wrong address.
        package.address = '300 State St'
        package.city = 'Salt Lake City'
        package.state = 'UT'
        package.zipcode = '84103'


# Time + Space complexity of O(1)
# Updates the address to the correct address after being notified (10:20) in the GUI.
def update_address(user_time, package):
    # If the user's input time is 10:20 or after, update the address.
    if user_time >= datetime.timedelta(hours=10, minutes=20, seconds=00):
        package.address = '410 S State St.'
        package.city = 'Salt Lake City'
        package.state = 'UT'
        package.zipcode = '84111'
