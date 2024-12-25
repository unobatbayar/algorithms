# 1. **Arrays**
# Python's built-in list works as an array

# Example of an array (list in Python)
array = [1, 2, 3, 4, 5]
print(array[0])  # Access (O(1))

# Insertion and deletion (O(n) because lists are dynamic in Python)
array.append(6)  # Insertion
print(array)  # [1, 2, 3, 4, 5, 6]
array.remove(3)  # Deletion of an element
print(array)  # [1, 2, 4, 5, 6]

# 2. **Linked Lists**
# Implementing a singly linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Linked list example
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # 1 -> 2 -> 3 -> None

# 3. **Stacks**
# Implementing a stack using a list

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0

# Stack example
stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek())  # 20
stack.pop()
print(stack.peek())  # 10

# 4. **Queues**
# Implementing a queue using collections.deque (efficient for FIFO)

from collections import deque

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print(queue.popleft())  # 10 (Dequeue)
print(queue)  # deque([20, 30])

# 5. **Hash Tables (Hash Maps)**
# Using a Python dictionary as a hash map

hash_map = {}
hash_map["apple"] = 10
hash_map["banana"] = 20
print(hash_map["apple"])  # 10

# Insertion, lookup, and deletion (all O(1) on average)
hash_map["apple"] = 15  # Update value
del hash_map["banana"]  # Delete key-value pair
print(hash_map)  # {'apple': 15}

# 6. **Heaps**
# Implementing a min-heap using heapq

import heapq

# Min-heap example (heapq always creates a min-heap)
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
print(heapq.heappop(heap))  # 5 (Smallest element)
print(heap)  # [10, 20]

# 7. **Trees**
# Implementing a basic Binary Search Tree (BST)

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = BSTNode(value)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = BSTNode(value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

# BST example
bst = BinarySearchTree()
bst.insert(20)
bst.insert(10)
bst.insert(30)
found_node = bst.search(10)
print(found_node.value if found_node else "Not found")  # 10

# 8. **Graphs**
# Implementing a graph using adjacency list

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

# Graph example
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.print_graph()  # 1: [2, 3], 2: [4], 3: []

# 9. **Sets**
# Using a Python set

s = set()
s.add(10)
s.add(20)
s.add(10)  # Duplicate, will not be added
print(s)  # {10, 20}

# 10. **Tries (Prefix Trees)**
# Implementing a Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

# Trie example
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))  # True
print(trie.search("app"))  # True
print(trie.search("appl"))  # False

# 11. **Disjoint Set (Union-Find)**
# Implementing Union-Find

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

# Union-Find example
uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
print(uf.find(0))  # 0
print(uf.find(2))  # 0 (same set as 0)

# 12. **Bloom Filters**
# Implementing a simple Bloom Filter

class BloomFilter:
    def __init__(self, size, hash_functions):
        self.size = size
        self.bit_array = [False] * size
        self.hash_functions = hash_functions
    
    def add(self, item):
        for hash_func in self.hash_functions:
            index = hash_func(item) % self.size
            self.bit_array[index] = True
    
    def check(self, item):
        return all(self.bit_array[hash_func(item) % self.size] for hash_func in self.hash_functions)

# Bloom Filter example (using simple hash functions)
def hash_func1(item):
    return hash(item)

def hash_func2(item):
    return hash(item) * 2

bloom = BloomFilter(10, [hash_func1, hash_func2])
bloom.add("apple")
print(bloom.check("apple"))  # True
print(bloom.check("banana"))  # False
