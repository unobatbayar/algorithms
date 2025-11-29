"""
Queue Data Structure

A queue is a FIFO (First In, First Out) data structure where elements are
added at the rear and removed from the front. Think of it like a line of people.

Time Complexity:
    - Enqueue: O(1)
    - Dequeue: O(1)
    - Front: O(1)
    - Search: O(n)

Space Complexity: O(n)

Applications:
    - Task scheduling
    - Breadth-First Search (BFS)
    - Print queue management
    - Message queues
"""


from collections import deque


class Queue:
    """Queue implementation using deque for efficiency."""
    
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """Add element to the rear of the queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()
    
    def front(self):
        """Return element at the front without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]
    
    def rear(self):
        """Return element at the rear without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of elements in the queue."""
        return len(self.items)
    
    def __str__(self):
        """String representation of the queue."""
        return f"Queue({list(self.items)})"


# Example usage
if __name__ == "__main__":
    queue = Queue()
    
    print("Enqueuing elements:")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"  {queue}")
    print(f"  Size: {queue.size()}")
    print(f"  Front: {queue.front()}")
    print(f"  Rear: {queue.rear()}")
    
    print("\nDequeuing elements:")
    while not queue.is_empty():
        print(f"  Dequeued: {queue.dequeue()}")
    
    print(f"  Queue is empty: {queue.is_empty()}")

