## Fundamental Data Structures for Software Engineers

This repository provides an overview of fundamental data structures every software engineer should be familiar with. These data structures are essential for problem-solving, coding interviews, and efficient system design.

1. **Arrays**  
   Description: A collection of elements stored in contiguous memory locations. They support fast random access but have fixed sizes.  
   Common Operations: Access (O(1)), Insert/Delete (O(n)).  
   Use Cases: Storing a list of items, efficient indexing.

2. **Linked Lists**  
   Description: A linear structure where each element points to the next. Can be singly or doubly linked.  
   Common Operations: Insertion/Deletion (O(1) at head/tail), Traversal (O(n)).  
   Use Cases: Dynamic memory allocation, implementing queues and stacks.

3. **Stacks**  
   Description: A LIFO (Last In, First Out) data structure where elements are added and removed from the same end (the top).  
   Common Operations: Push/Pop (O(1)), Peek (O(1)).  
   Use Cases: Undo functionality, depth-first search (DFS), recursion.

4. **Queues**  
   Description: A FIFO (First In, First Out) data structure where elements are added at the back and removed from the front.  
   Common Operations: Enqueue/Dequeue (O(1)), Peek (O(1)).  
   Use Cases: Breadth-first search (BFS), task scheduling, buffering.

5. **Hash Tables (Hash Maps)**  
   Description: A collection of key-value pairs that allows for fast lookups and insertions using a hash function.  
   Common Operations: Insert/Lookup/Delete (O(1) on average).  
   Use Cases: Caching, frequency counting, fast lookups.

6. **Heaps**  
   Description: A binary tree-based structure that maintains the heap property. Commonly used to implement priority queues.  
   Common Operations: Insertion/Deletion (O(log n)), Peek (O(1)).  
   Use Cases: Priority queues, heap sort, finding the kth largest/smallest element.

7. **Trees**  
   Description: A hierarchical structure with nodes connected by edges. Common types include binary trees, binary search trees (BST), and balanced trees (e.g., AVL, Red-Black).  
   Common Operations: Insertion/Search/Deletion (O(log n) for balanced trees).  
   Use Cases: Hierarchical data, database indexing, search operations.

8. **Graphs**  
   Description: A collection of nodes (vertices) connected by edges. Can be directed, undirected, weighted, or unweighted.  
   Common Operations: Traversal (DFS/BFS), Shortest Path (Dijkstra, Bellman-Ford).  
   Use Cases: Network routing, social network analysis, pathfinding.

9. **Sets**  
   Description: A collection of unique elements with no particular order. Supports fast membership checking.  
   Common Operations: Insert/Lookup/Delete (O(1)).  
   Use Cases: Removing duplicates, set operations (union, intersection).

10. **Tries (Prefix Trees)**  
    Description: A tree-like data structure for storing a dynamic set of strings, allowing for efficient prefix searches.  
    Common Operations: Insert/Search/Delete (O(m), where m is the string length).  
    Use Cases: Autocomplete, dictionary search, prefix matching.

11. **Disjoint Set (Union-Find)**  
    Description: A data structure to keep track of a partition of a set into disjoint subsets, supporting efficient union and find operations.  
    Common Operations: Union/Find (O(α(n)), where α is the inverse Ackermann function).  
    Use Cases: Network connectivity, Kruskal's MST algorithm, connected components.

12. **Bloom Filters**  
    Description: A probabilistic data structure used to test membership, with some chance of false positives but no false negatives.  
    Common Operations: Insert/Check (O(k), where k is the number of hash functions).  
    Use Cases: Membership testing in large datasets, caching.



Built-in Functions in Python:
### map():

Purpose: Applies a given function to each item in an iterable (list, tuple, etc.) and returns a map object (iterator).
Example: Transforming a list of numbers by squaring each number.
python
Copy code
numbers = [1, 2, 3, 4]
result = map(lambda x: x ** 2, numbers)
print(list(result))  # Output: [1, 4, 9, 16]

### filter():

Purpose: Filters elements from an iterable based on a given function that returns True or False. It returns an iterator.
Example: Filtering even numbers from a list.
python
Copy code
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))  # Output: [2, 4]

### reduce() (from functools):

Purpose: Applies a binary function cumulatively to the items of an iterable, reducing it to a single value.
Example: Calculating the product of all elements in a list.
python
Copy code
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24
sorted():

Purpose: Returns a new sorted list from the elements of any iterable (can sort in ascending or descending order).
Example: Sorting a list of numbers.
python
Copy code
numbers = [4, 2, 3, 1]
result = sorted(numbers)
print(result)  # Output: [1, 2, 3, 4]

### zip():

Purpose: Aggregates elements from multiple iterables into tuples. It pairs elements by their positions (i.e., the first element from each iterable, the second element from each iterable, and so on).
Example: Combining two lists into pairs of tuples.
python
Copy code
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 88]
result = list(zip(names, scores))
print(result)  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 88)]

### all() / any():

Purpose:
**all()** checks if all elements in an iterable are True.
**any()** checks if at least one element is True.
Example:
python
Copy code
numbers = [1, 2, 3]
print(all(x > 0 for x in numbers))  # Output: True
print(any(x < 0 for x in numbers))  # Output: False