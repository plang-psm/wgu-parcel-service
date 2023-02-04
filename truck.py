class Truck:
    def __init__(self, capacity, mileage, speed, packages, location, delivery_time, departure_time):
        self.capacity = capacity
        self.mileage = mileage
        self.speed = speed
        self.packages = packages
        self.location = location
        self.delivery_time = departure_time
        self.departure_time = departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.capacity, self.mileage, self.speed, self.packages, self.location, self.delivery_time,
            self.departure_time)
