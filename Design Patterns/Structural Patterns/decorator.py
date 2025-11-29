"""
Decorator Design Pattern

The Decorator pattern allows behavior to be added to individual objects dynamically
without affecting the behavior of other objects from the same class.

Use cases:
    - Adding features to objects without modifying their structure
    - When subclassing would be impractical (too many combinations)
    - Runtime feature addition
"""


from abc import ABC, abstractmethod


# Component interface
class Coffee(ABC):
    """Abstract component."""
    
    @abstractmethod
    def cost(self):
        """Get cost of coffee."""
        pass
    
    @abstractmethod
    def description(self):
        """Get description of coffee."""
        pass


# Concrete component
class SimpleCoffee(Coffee):
    """Concrete component."""
    
    def cost(self):
        return 5
    
    def description(self):
        return "Simple coffee"


# Base decorator
class CoffeeDecorator(Coffee):
    """Base decorator class."""
    
    def __init__(self, coffee):
        self._coffee = coffee
    
    def cost(self):
        return self._coffee.cost()
    
    def description(self):
        return self._coffee.description()


# Concrete decorators
class MilkDecorator(CoffeeDecorator):
    """Concrete decorator: Milk."""
    
    def cost(self):
        return self._coffee.cost() + 2
    
    def description(self):
        return self._coffee.description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    """Concrete decorator: Sugar."""
    
    def cost(self):
        return self._coffee.cost() + 1
    
    def description(self):
        return self._coffee.description() + ", Sugar"


class WhipDecorator(CoffeeDecorator):
    """Concrete decorator: Whip."""
    
    def cost(self):
        return self._coffee.cost() + 3
    
    def description(self):
        return self._coffee.description() + ", Whip"


# Example usage
if __name__ == "__main__":
    # Simple coffee
    coffee = SimpleCoffee()
    print(f"{coffee.description()}: ${coffee.cost()}")
    
    # Coffee with milk
    coffee_with_milk = MilkDecorator(SimpleCoffee())
    print(f"{coffee_with_milk.description()}: ${coffee_with_milk.cost()}")
    
    # Coffee with milk and sugar
    coffee_full = SugarDecorator(MilkDecorator(SimpleCoffee()))
    print(f"{coffee_full.description()}: ${coffee_full.cost()}")
    
    # Coffee with everything
    coffee_deluxe = WhipDecorator(SugarDecorator(MilkDecorator(SimpleCoffee())))
    print(f"{coffee_deluxe.description()}: ${coffee_deluxe.cost()}")

