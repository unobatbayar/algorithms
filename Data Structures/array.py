"""
Dynamic Array Data Structure

A dynamic array is a resizable array that automatically grows when needed.
Python's list is implemented as a dynamic array.

Time Complexity:
    - Access: O(1)
    - Append: O(1) amortized
    - Insert: O(n)
    - Delete: O(n)
    - Search: O(n)

Space Complexity: O(n)
"""


class DynamicArray:
    """Dynamic array implementation."""
    
    def __init__(self, capacity=2):
        """
        Initialize dynamic array.
        
        Args:
            capacity: Initial capacity
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
    
    def _resize(self, new_capacity):
        """Resize the array to new capacity."""
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity
    
    def append(self, value):
        """Add element at the end."""
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)
        
        self.data[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """Insert value at index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        
        self.data[index] = value
        self.size += 1
    
    def delete(self, index):
        """Delete element at index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]
        
        self.size -= 1
        
        # Shrink if too much unused space
        if self.size < self.capacity // 4 and self.capacity > 2:
            self._resize(self.capacity // 2)
    
    def get(self, index):
        """Get element at index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.data[index]
    
    def set(self, index, value):
        """Set element at index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.data[index] = value
    
    def __len__(self):
        """Return size of array."""
        return self.size
    
    def __getitem__(self, index):
        """Support indexing."""
        return self.get(index)
    
    def __setitem__(self, index, value):
        """Support assignment."""
        self.set(index, value)
    
    def __str__(self):
        """String representation."""
        return str([self.data[i] for i in range(self.size)])


# Example usage
if __name__ == "__main__":
    arr = DynamicArray()
    
    print("Appending elements:")
    for i in range(5):
        arr.append(i)
        print(f"  {arr}, capacity: {arr.capacity}")
    
    print(f"\nAccessing element at index 2: {arr[2]}")
    
    print("\nInserting 10 at index 1:")
    arr.insert(1, 10)
    print(f"  {arr}")
    
    print("\nDeleting element at index 2:")
    arr.delete(2)
    print(f"  {arr}, capacity: {arr.capacity}")

