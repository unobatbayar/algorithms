"""
Builder Design Pattern

The Builder pattern constructs complex objects step by step. It allows you to
produce different types and representations of an object using the same construction code.

Use cases:
    - When constructing complex objects with many optional parameters
    - When you want to construct objects step by step
    - When you need different representations of the same object
"""


class Pizza:
    """Product class."""
    
    def __init__(self):
        self.size = None
        self.crust = None
        self.cheese = False
        self.pepperoni = False
        self.bacon = False
        self.mushrooms = False
    
    def __str__(self):
        parts = [f"Size: {self.size}", f"Crust: {self.crust}"]
        if self.cheese:
            parts.append("Cheese")
        if self.pepperoni:
            parts.append("Pepperoni")
        if self.bacon:
            parts.append("Bacon")
        if self.mushrooms:
            parts.append("Mushrooms")
        return ", ".join(parts)


class PizzaBuilder:
    """Builder class."""
    
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        """Set pizza size."""
        self.pizza.size = size
        return self
    
    def set_crust(self, crust):
        """Set crust type."""
        self.pizza.crust = crust
        return self
    
    def add_cheese(self):
        """Add cheese."""
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        """Add pepperoni."""
        self.pizza.pepperoni = True
        return self
    
    def add_bacon(self):
        """Add bacon."""
        self.pizza.bacon = True
        return self
    
    def add_mushrooms(self):
        """Add mushrooms."""
        self.pizza.mushrooms = True
        return self
    
    def build(self):
        """Build and return the pizza."""
        return self.pizza


# Example usage
if __name__ == "__main__":
    # Build a custom pizza
    builder = PizzaBuilder()
    pizza = (builder
             .set_size("Large")
             .set_crust("Thin")
             .add_cheese()
             .add_pepperoni()
             .add_mushrooms()
             .build())
    
    print(f"Custom Pizza: {pizza}")
    
    # Build another pizza
    pizza2 = (PizzaBuilder()
              .set_size("Medium")
              .set_crust("Thick")
              .add_cheese()
              .add_bacon()
              .build())
    
    print(f"\nAnother Pizza: {pizza2}")

