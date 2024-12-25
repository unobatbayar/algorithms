# map()
# Purpose: Applies a given function to each item in an iterable and returns a map object (iterator).
numbers = [1, 2, 3, 4]
result = map(lambda x: x ** 2, numbers)
print(list(result))  # Output: [1, 4, 9, 16]

# filter()
# Purpose: Filters elements from an iterable based on a given function that returns True or False. It returns an iterator.
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))  # Output: [2, 4]

# reduce() (from functools)
# Purpose: Applies a binary function cumulatively to the items of an iterable, reducing it to a single value.
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24

# sorted()
# Purpose: Returns a new sorted list from the elements of any iterable (can sort in ascending or descending order).
numbers = [4, 2, 3, 1]
result = sorted(numbers)
print(result)  # Output: [1, 2, 3, 4]

# zip()
# Purpose: Aggregates elements from multiple iterables into tuples. It pairs elements by their positions.
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 88]
result = list(zip(names, scores))
print(result)  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 88)]

# all() / any()
# Purpose: all() checks if all elements in an iterable are True, any() checks if at least one element is True.
numbers = [1, 2, 3]
print(all(x > 0 for x in numbers))  # Output: True
print(any(x < 0 for x in numbers))  # Output: False
