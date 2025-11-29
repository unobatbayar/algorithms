"""
Prototype Design Pattern

The Prototype pattern creates objects by cloning existing instances rather than
creating new ones from scratch. This is useful when object creation is expensive.

Use cases:
    - When object creation is expensive
    - When you want to avoid subclassing
    - When you need to create objects at runtime
"""


import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    """Abstract prototype class."""
    
    @abstractmethod
    def clone(self):
        """Clone the object."""
        pass


class ConcretePrototype(Prototype):
    """Concrete prototype implementation."""
    
    def __init__(self, value):
        self.value = value
        self.data = []
    
    def clone(self):
        """Create a deep copy of the object."""
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Value: {self.value}, Data: {self.data}"


# Example usage
if __name__ == "__main__":
    # Create original object
    original = ConcretePrototype(10)
    original.data = [1, 2, 3]
    
    print(f"Original: {original}")
    
    # Clone the object
    clone = original.clone()
    clone.value = 20
    clone.data.append(4)
    
    print(f"Clone: {clone}")
    print(f"Original after clone: {original}")  # Original unchanged
    
    # Create another clone
    clone2 = original.clone()
    clone2.value = 30
    print(f"\nClone 2: {clone2}")

