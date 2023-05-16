class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        if self.has_next():
            item = self.collection[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration()

# Example usage

# Create a collection
my_collection = [1, 2, 3, 4, 5]

# Create an iterator for the collection
my_iterator = Iterator(my_collection)

# Iterate over the collection using the iterator
while my_iterator.has_next():
    item = my_iterator.next()
    print(item)
