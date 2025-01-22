## Fundamental Algorithms for Software Engineers

As a software engineer, it's crucial to have a strong understanding of fundamental algorithms. Here's a list of essential algorithms that every software engineer should be familiar with:

## 1. Sorting Algorithms

Sorting is a fundamental operation in computer science that arranges elements in a specific order. Understanding sorting algorithms helps in both optimization and problem-solving.

- **Bubble Sort**: A simple, inefficient sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. ![](https://img.shields.io/static/v1?label=&message=learned&color=blue)
- **Selection Sort**: An algorithm that repeatedly selects the smallest (or largest) element from the unsorted portion and swaps it into the correct position.
- **Insertion Sort**: Builds the final sorted array one item at a time by inserting each new element into its correct position.
- **Merge Sort**: A divide-and-conquer algorithm that divides the array into two halves, recursively sorts each half, and then merges the sorted halves.
- **Quick Sort**: Another divide-and-conquer algorithm that partitions the array around a pivot and recursively sorts the sub-arrays.
- **Heap Sort**: Utilizes a binary heap to sort elements. It’s efficient but not stable.
- **Counting Sort**: A non-comparative integer sorting algorithm that counts occurrences of each element.
- **Radix Sort**: A non-comparative sorting algorithm that sorts numbers digit by digit starting from the least significant digit.
- **Bucket Sort**: Divides the range of input elements into several "buckets" and sorts each bucket individually.

## 2. Searching Algorithms

Searching is used to find specific elements in data structures. These algorithms are foundational for tasks like data retrieval.

- **Linear Search**: A simple search algorithm that checks every element in the list one by one.
- **Binary Search**: A more efficient search algorithm for sorted arrays. It repeatedly divides the search interval in half.
- **Breadth-First Search (BFS)**: A graph traversal algorithm that explores nodes level by level. ![](https://img.shields.io/static/v1?label=&message=learning&color=green)

- **Depth-First Search (DFS)**: A graph traversal algorithm that explores as far as possible along each branch before backtracking.
- **Jump Search**: An optimization of linear search for sorted arrays. It jumps ahead by a fixed number of elements and then performs a linear search within the block.
- **Exponential Search**: A search algorithm that works for sorted arrays and has a time complexity of O(log n).

## 3. Dynamic Programming

Dynamic programming (DP) is a method for solving problems by breaking them down into simpler subproblems. It avoids redundant calculations by storing the results of subproblems.

- **Fibonacci Sequence (Recursive & Memoized)**: Classic example of using dynamic programming to avoid redundant recursive calls.
- **Knapsack Problem**: Involves selecting a subset of items with given weights and values to maximize the total value without exceeding the weight capacity.
- **Longest Common Subsequence (LCS)**: Finds the longest subsequence common to two sequences.
- **Longest Increasing Subsequence (LIS)**: Finds the longest subsequence of a sequence that is strictly increasing.
- **Matrix Chain Multiplication**: Optimizes the order of matrix multiplications to minimize the number of scalar multiplications.
- **Edit Distance (Levenshtein Distance)**: Measures the difference between two strings in terms of the minimum number of operations (insertions, deletions, or substitutions) required to transform one string into the other.

## 4. Greedy Algorithms

Greedy algorithms make a series of choices by choosing the best option at each step, with the hope of finding the optimal solution.

- **Activity Selection Problem**: Select the maximum number of activities that can be performed by a single person given their start and finish times.
- **Fractional Knapsack Problem**: A variant of the knapsack problem where you can take fractions of items (instead of whole items).
- **Huffman Coding**: A lossless data compression algorithm that assigns variable-length codes to input characters, with shorter codes assigned to more frequent characters.
- **Prim’s and Kruskal’s Algorithms (Minimum Spanning Tree)**: Used to find the minimum spanning tree of a graph, which connects all the vertices with the minimum possible total edge weight.
- **Dijkstra’s Algorithm**: Used for finding the shortest path between nodes in a graph with non-negative edge weights.

## 5. Divide and Conquer

Divide and conquer is an algorithmic paradigm that breaks a problem into smaller subproblems, solves them recursively, and combines their results.

- **Merge Sort**: A divide-and-conquer algorithm for sorting, which recursively divides the array and then merges the sorted arrays.
- **Quick Sort**: Another divide-and-conquer sorting algorithm that partitions the array and sorts each partition recursively.
- **Binary Search**: A classic divide-and-conquer search algorithm that operates on a sorted list by repeatedly dividing the search space in half.

## 6. Graph Algorithms

Graphs are fundamental data structures in computer science. Several algorithms are designed to traverse and optimize graphs.

- **Breadth-First Search (BFS)**: Traverses a graph level by level, starting from a root node.
- **Depth-First Search (DFS)**: Traverses a graph by going as deep as possible along each branch before backtracking.
- **Dijkstra’s Algorithm**: Finds the shortest path in a graph with non-negative weights from a starting node to all other nodes.
- **Bellman-Ford Algorithm**: Finds the shortest path in a graph, similar to Dijkstra, but can handle negative weights.
- **Floyd-Warshall Algorithm**: A dynamic programming algorithm for finding shortest paths between all pairs of vertices in a graph.
- **Topological Sort**: A linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every directed edge, vertex u comes before vertex v.
- **Kruskal’s and Prim’s Algorithms (MST)**: Used to find the Minimum Spanning Tree in a weighted graph.
- **A\* Search Algorithm**: A graph traversal and pathfinding algorithm that finds the shortest path between nodes, using heuristics to improve performance.

## 7. Backtracking Algorithms

Backtracking is used to solve problems by trying to build a solution incrementally, and abandoning a solution as soon as it is determined to be invalid.

- **N-Queens Problem**: Place N queens on an N×N chessboard such that no two queens threaten each other.
- **Sudoku Solver**: Uses backtracking to try different placements of numbers in a grid until a solution is found.
- **Subset Sum Problem**: Finds a subset of numbers that add up to a given sum.

## 8. Miscellaneous Algorithms

These are additional fundamental algorithms that don't fit neatly into the categories above but are important for software engineering.

- **Euclid’s Algorithm (GCD)**: Finds the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
- **Sieve of Eratosthenes**: Finds all prime numbers up to a given limit using a sieve technique.
- **Ternary Search**: A divide-and-conquer search algorithm that works on unimodal functions or ordered arrays.
- **KMP (Knuth-Morris-Pratt) String Matching Algorithm**: Efficient string matching algorithm for finding occurrences of a substring in a string.
- **Rabin-Karp String Matching Algorithm**: A string searching algorithm that uses hashing to find patterns in a text.
- **Bit Manipulation Algorithms**: Algorithms that use bitwise operators to solve problems, like checking if a number is a power of 2 or finding the Hamming weight (number of 1’s in the binary representation).

## Big O notation

- ![Learn Big O notation in 6 minutes](https://raw.githubusercontent.com/unobatbayar/algorithms/refs/heads/master/public/big_o.png)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [(Learn Big O notation in 6 minutes)](https://www.youtube.com/watch?v=XMUe3zFhM5c)

## See also

- [Bit Manipulation (AND, OR, XOR, Shifts)](https://realpython.com/python-bitwise-operators/)
- [Algorithms study cheatsheets](https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/)
