class Packages:
    def __init__(self, p_id, address, city, zipcode, state, deadline, weight, notes, status, time_delivered,
                 start_time):
        self.p_id = p_id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.time_delivered = time_delivered
        self.start_time = start_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.p_id, self.address, self.city, self.zipcode, self.state, self.deadline,
            self.weight, self.notes, self.status, self.time_delivered, self.start_time)