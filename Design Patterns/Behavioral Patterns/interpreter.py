"""
Interpreter Design Pattern

The Interpreter pattern defines a representation for a language's grammar along
with an interpreter that uses the representation to interpret sentences in the language.

Use cases:
    - Simple language interpreters
    - Expression evaluators
    - Query languages
    - Regular expressions
"""


from abc import ABC, abstractmethod


# Abstract expression
class Expression(ABC):
    """Abstract expression interface."""
    
    @abstractmethod
    def interpret(self, context):
        """Interpret the expression."""
        pass


# Terminal expressions
class Number(Expression):
    """Terminal expression: Number."""
    
    def __init__(self, value):
        self.value = value
    
    def interpret(self, context):
        return self.value


# Non-terminal expressions
class Add(Expression):
    """Non-terminal expression: Addition."""
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


class Subtract(Expression):
    """Non-terminal expression: Subtraction."""
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


class Multiply(Expression):
    """Non-terminal expression: Multiplication."""
    
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
    def interpret(self, context):
        return self.left.interpret(context) * self.right.interpret(context)


# Example usage
if __name__ == "__main__":
    # Expression: (5 + 3) * 2
    expression = Multiply(
        Add(Number(5), Number(3)),
        Number(2)
    )
    
    result = expression.interpret({})
    print(f"(5 + 3) * 2 = {result}")
    
    # Expression: 10 - 4
    expression2 = Subtract(Number(10), Number(4))
    result2 = expression2.interpret({})
    print(f"10 - 4 = {result2}")

