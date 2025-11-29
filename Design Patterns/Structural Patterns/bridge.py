"""
Bridge Design Pattern

The Bridge pattern decouples an abstraction from its implementation so that
the two can vary independently. It uses composition instead of inheritance.

Use cases:
    - When you want to avoid permanent binding between abstraction and implementation
    - When both abstractions and implementations should be extensible
    - When implementation should be switchable at runtime
"""


from abc import ABC, abstractmethod


# Implementation interface
class Renderer(ABC):
    """Abstract renderer interface."""
    
    @abstractmethod
    def render_circle(self, radius):
        """Render a circle."""
        pass


# Concrete implementations
class VectorRenderer(Renderer):
    """Vector renderer implementation."""
    
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} as vector graphics"


class RasterRenderer(Renderer):
    """Raster renderer implementation."""
    
    def render_circle(self, radius):
        return f"Drawing a circle of radius {radius} as pixels"


# Abstraction
class Shape(ABC):
    """Abstract shape class."""
    
    def __init__(self, renderer):
        self.renderer = renderer
    
    @abstractmethod
    def draw(self):
        """Draw the shape."""
        pass


# Refined abstraction
class Circle(Shape):
    """Concrete shape: Circle."""
    
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius
    
    def draw(self):
        return self.renderer.render_circle(self.radius)


# Example usage
if __name__ == "__main__":
    # Circle with vector renderer
    vector_circle = Circle(VectorRenderer(), 5)
    print(vector_circle.draw())
    
    # Circle with raster renderer
    raster_circle = Circle(RasterRenderer(), 5)
    print(raster_circle.draw())

