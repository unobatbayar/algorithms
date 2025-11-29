"""
Iterator Design Pattern

The Iterator pattern provides a way to access elements of an aggregate object
sequentially without exposing its underlying representation.

Use cases:
    - Traversing collections
    - Hiding implementation details of collection
    - Supporting multiple traversal methods
"""


from abc import ABC, abstractmethod


# Iterator interface
class Iterator(ABC):
    """Abstract iterator interface."""
    
    @abstractmethod
    def has_next(self):
        """Check if there are more elements."""
        pass
    
    @abstractmethod
    def next(self):
        """Get next element."""
        pass


# Aggregate interface
class Aggregate(ABC):
    """Abstract aggregate interface."""
    
    @abstractmethod
    def create_iterator(self):
        """Create an iterator."""
        pass


# Concrete aggregate
class NumberCollection(Aggregate):
    """Concrete aggregate: Collection of numbers."""
    
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        """Add a number to collection."""
        self.numbers.append(number)
    
    def create_iterator(self):
        """Create iterator for this collection."""
        return NumberIterator(self.numbers)


# Concrete iterator
class NumberIterator(Iterator):
    """Concrete iterator for NumberCollection."""
    
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    
    def has_next(self):
        """Check if there are more elements."""
        return self.index < len(self.numbers)
    
    def next(self):
        """Get next element."""
        if self.has_next():
            value = self.numbers[self.index]
            self.index += 1
            return value
        raise StopIteration


# Example usage
if __name__ == "__main__":
    collection = NumberCollection()
    collection.add(1)
    collection.add(2)
    collection.add(3)
    collection.add(4)
    collection.add(5)
    
    iterator = collection.create_iterator()
    
    print("Iterating through collection:")
    while iterator.has_next():
        print(iterator.next())
    
    # Python's built-in iteration (using __iter__ and __next__)
    print("\nUsing Python's built-in iteration:")
    for num in collection.numbers:
        print(num)
