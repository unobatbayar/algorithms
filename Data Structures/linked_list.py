"""
Linked List Data Structure

A linked list is a linear data structure where elements are stored in nodes,
and each node points to the next node. Unlike arrays, linked lists don't have
contiguous memory allocation.

Time Complexity:
    - Access: O(n)
    - Insertion at head: O(1)
    - Insertion at tail: O(1) with tail pointer, O(n) without
    - Deletion: O(1) if node is known, O(n) to find node
    - Search: O(n)

Space Complexity: O(n)
"""


class Node:
    """Node class for linked list."""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if list is empty."""
        return self.head is None
    
    def append(self, data):
        """Add element at the end of the list."""
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """Add element at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_after(self, prev_node, data):
        """Insert element after a given node."""
        if prev_node is None:
            raise ValueError("Previous node cannot be None")
        
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete first occurrence of data."""
        if self.head is None:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
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
    
    def __len__(self):
        """Return size of the list."""
        return self.size
    
    def __str__(self):
        """String representation of the list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "Empty"


# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    
    print("Appending elements:")
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print(f"  {ll}")
    
    print("\nPrepending element:")
    ll.prepend(0)
    print(f"  {ll}")
    
    print(f"\nSearching for 2: Index {ll.search(2)}")
    print(f"Size: {len(ll)}")
    
    print("\nDeleting element 2:")
    ll.delete(2)
    print(f"  {ll}")

