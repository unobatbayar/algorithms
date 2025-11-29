"""
Visitor Design Pattern

The Visitor pattern represents an operation to be performed on elements of
an object structure. It lets you define a new operation without changing the
classes of the elements on which it operates.

Use cases:
    - Operations on object structures
    - Adding new operations without modifying classes
    - Separating algorithms from object structure
"""


from abc import ABC, abstractmethod


# Element interface
class Element(ABC):
    """Abstract element interface."""
    
    @abstractmethod
    def accept(self, visitor):
        """Accept a visitor."""
        pass


# Concrete elements
class ConcreteElementA(Element):
    """Concrete element A."""
    
    def accept(self, visitor):
        visitor.visit_element_a(self)
    
    def operation_a(self):
        return "Operation A"


class ConcreteElementB(Element):
    """Concrete element B."""
    
    def accept(self, visitor):
        visitor.visit_element_b(self)
    
    def operation_b(self):
        return "Operation B"


# Visitor interface
class Visitor(ABC):
    """Abstract visitor interface."""
    
    @abstractmethod
    def visit_element_a(self, element):
        """Visit element A."""
        pass
    
    @abstractmethod
    def visit_element_b(self, element):
        """Visit element B."""
        pass


# Concrete visitors
class ConcreteVisitor1(Visitor):
    """Concrete visitor 1."""
    
    def visit_element_a(self, element):
        print(f"Visitor1: {element.operation_a()}")
    
    def visit_element_b(self, element):
        print(f"Visitor1: {element.operation_b()}")


class ConcreteVisitor2(Visitor):
    """Concrete visitor 2."""
    
    def visit_element_a(self, element):
        print(f"Visitor2: {element.operation_a()}")
    
    def visit_element_b(self, element):
        print(f"Visitor2: {element.operation_b()}")


# Example usage
if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]
    
    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()
    
    print("Using Visitor1:")
    for element in elements:
        element.accept(visitor1)
    
    print("\nUsing Visitor2:")
    for element in elements:
        element.accept(visitor2)

