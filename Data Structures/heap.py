"""
Heap Data Structure

A heap is a complete binary tree that satisfies the heap property:
- Max Heap: Parent >= Children
- Min Heap: Parent <= Children

Time Complexity:
    - Insertion: O(log n)
    - Extraction: O(log n)
    - Peek: O(1)
    - Build heap: O(n)

Space Complexity: O(n)

Applications:
    - Priority queues
    - Heap sort
    - Finding kth largest/smallest element
"""


class MinHeap:
    """Min Heap implementation (parent <= children)."""
    
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        """Get parent index."""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Get left child index."""
        return 2 * i + 1
    
    def right_child(self, i):
        """Get right child index."""
        return 2 * i + 2
    
    def swap(self, i, j):
        """Swap elements at indices i and j."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        """Insert value into heap."""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        """Maintain heap property by moving element up."""
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def extract_min(self):
        """Extract and return minimum element."""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, i):
        """Maintain heap property by moving element down."""
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.swap(i, smallest)
            self._heapify_down(smallest)
    
    def peek(self):
        """Get minimum element without removing it."""
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def size(self):
        """Get heap size."""
        return len(self.heap)
    
    def is_empty(self):
        """Check if heap is empty."""
        return len(self.heap) == 0


class MaxHeap:
    """Max Heap implementation (parent >= children)."""
    
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1
    
    def right_child(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)
    
    def extract_max(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        
        if largest != i:
            self.swap(i, largest)
            self._heapify_down(largest)
    
    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0


# Example usage
if __name__ == "__main__":
    print("Min Heap:")
    min_heap = MinHeap()
    values = [3, 1, 6, 5, 2, 4]
    
    for val in values:
        min_heap.insert(val)
        print(f"  Inserted {val}, min: {min_heap.peek()}")
    
    print("\nExtracting from min heap:")
    while not min_heap.is_empty():
        print(f"  Extracted: {min_heap.extract_min()}")
    
    print("\nMax Heap:")
    max_heap = MaxHeap()
    for val in values:
        max_heap.insert(val)
        print(f"  Inserted {val}, max: {max_heap.peek()}")
    
    print("\nExtracting from max heap:")
    while not max_heap.is_empty():
        print(f"  Extracted: {max_heap.extract_max()}")

