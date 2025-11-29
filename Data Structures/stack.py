"""
Stack Data Structure

A stack is a LIFO (Last In, First Out) data structure where elements are
added and removed from the same end (top). Think of it like a stack of plates.

Time Complexity:
    - Push: O(1)
    - Pop: O(1)
    - Peek: O(1)
    - Search: O(n)

Space Complexity: O(n)

Applications:
    - Function call stack
    - Expression evaluation
    - Undo/Redo operations
    - Backtracking algorithms
"""


class Stack:
    """Stack implementation using list."""
    
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add element to the top of the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return element from the top of the stack."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return element at the top without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0
    
    def size(self):
        """Return number of elements in the stack."""
        return len(self.items)
    
    def __str__(self):
        """String representation of the stack."""
        return f"Stack({self.items})"


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    print("Pushing elements:")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"  {stack}")
    print(f"  Size: {stack.size()}")
    print(f"  Top: {stack.peek()}")
    
    print("\nPopping elements:")
    while not stack.is_empty():
        print(f"  Popped: {stack.pop()}")
    
    print(f"  Stack is empty: {stack.is_empty()}")

