"""
Doubly Linked List Data Structure

A doubly linked list is a linked list where each node has pointers to both
the next and previous nodes. This allows traversal in both directions.

Time Complexity:
    - Access: O(n)
    - Insertion at head/tail: O(1)
    - Deletion: O(1) if node is known, O(n) to find node
    - Search: O(n)

Space Complexity: O(n)
"""


class Node:
    """Node class for doubly linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Doubly linked list implementation."""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty."""
        return self.head is None
    
    def append(self, data):
        """Add element at the end of the list."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """Add element at the beginning of the list."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def delete(self, data):
        """Delete first occurrence of data."""
        current = self.head
        
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
                return True
            
            current = current.next
        
        return False
    
    def search(self, data):
        """Search for data in the list."""
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def traverse_forward(self):
        """Traverse list from head to tail."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty"
    
    def traverse_backward(self):
        """Traverse list from tail to head."""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        return " <- ".join(elements) if elements else "Empty"
    
    def __len__(self):
        """Return size of the list."""
        return self.size
    
    def __str__(self):
        """String representation (forward traversal)."""
        return self.traverse_forward()


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    print("Appending elements:")
    dll.append(1)
    dll.append(2)
    dll.append(3)
    print(f"  Forward: {dll}")
    print(f"  Backward: {dll.traverse_backward()}")
    
    print("\nPrepending element:")
    dll.prepend(0)
    print(f"  {dll}")
    
    print(f"\nSearching for 2: Index {dll.search(2)}")
    print(f"Size: {len(dll)}")
    
    print("\nDeleting element 2:")
    dll.delete(2)
    print(f"  {dll}")

