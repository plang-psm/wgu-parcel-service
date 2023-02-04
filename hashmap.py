# WGU Lets go hashing https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71
class HashMap:
    # Time + Space complexity of O(1).
    # Hashmap constructor.
    def __init__(self, initial_capacity=40):
        # Creating a table.
        self.table = []
        # Iterating and appending to the table.
        for i in range(initial_capacity):
            self.table.append([])

    # E. The hash table has an insert function that stores all of the given components
    #   (listed in Part D) using the package ID as the key.
    # Time + Space complexity of O(n).
    # Method that inserts an item into our hash table.
    def insert(self, key, item):
        # Where we are going to place the item.
        index = hash(key) % len(self.table)
        index_list = self.table[index]
        # For the key value in our index list,
        for key_val in index_list:
            # If key value[0] equals the key.
            if key_val[0] == key:
                # Then assign key value[1] to the item and return true.
                key_val[1] = item
                return True
        # Assign the key and item to a key_value variable,
        key_value = [key, item]
        # Append it into our index list and return true.
        index_list.append(key_value)
        return True

    # F. The provided hash table should include a look-up function that can use a package's ID
    #   to retrieve all of the same package’s components from the hash table
    # Time complexity of O(n) + Space complexity of O(1).
    # Method that searches for an item's key and returns its value from our list.
    def lookup(self, key):
        # Where we are going to place the item.
        index = hash(key) % len(self.table)
        index_list = self.table[index]

        # For the key value in our index list,
        for key_val in index_list:
            # If the key value [0] equals to key,
            if key_val[0] == key:
                # Then return key value[1].
                return key_val[1]
        # Return none if none is found.
        return None

    # Time complexity of O(n) + Space complexity of O(1).
    # Method that removes a key and item from out list.
    def remove(self, key):
        index = hash(key) % len(self.table)
        index_list = self.table[index]

        # For the key value in our index list,
        for key_val in index_list:
            # If the key value [0] equals to key,
            if key_val[0] == key:
                # Then remove key value[0] and key value[1].
                index_list.remove([key_val[0], key_val[1]])
