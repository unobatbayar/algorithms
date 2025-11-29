"""
Flyweight Design Pattern

The Flyweight pattern minimizes memory usage by sharing as much data as possible
with similar objects. It's useful when you need to create many similar objects.

Use cases:
    - When you need to create many similar objects
    - When memory usage is a concern
    - When object identity is not important
    - Text editors, game development
"""


# Flyweight
class TreeType:
    """Flyweight class: Shared tree type data."""
    
    def __init__(self, name, color, texture):
        self.name = name
        self.color = color
        self.texture = texture
    
    def render(self, x, y):
        """Render tree at position (x, y)."""
        return f"Rendering {self.name} tree ({self.color}, {self.texture}) at ({x}, {y})"


# Flyweight factory
class TreeFactory:
    """Factory for creating and managing flyweights."""
    
    _tree_types = {}
    
    @staticmethod
    def get_tree_type(name, color, texture):
        """Get or create tree type."""
        key = (name, color, texture)
        if key not in TreeFactory._tree_types:
            TreeFactory._tree_types[key] = TreeType(name, color, texture)
        return TreeFactory._tree_types[key]


# Context (uses flyweight)
class Tree:
    """Tree object that uses flyweight."""
    
    def __init__(self, x, y, tree_type):
        self.x = x
        self.y = y
        self.tree_type = tree_type
    
    def render(self):
        """Render the tree."""
        return self.tree_type.render(self.x, self.y)


# Example usage
if __name__ == "__main__":
    # Create tree types (flyweights)
    oak_type = TreeFactory.get_tree_type("Oak", "Green", "Rough")
    pine_type = TreeFactory.get_tree_type("Pine", "Dark Green", "Smooth")
    
    # Create trees (contexts)
    trees = [
        Tree(1, 2, oak_type),
        Tree(3, 4, oak_type),  # Reuses oak_type
        Tree(5, 6, pine_type),
        Tree(7, 8, oak_type),  # Reuses oak_type again
    ]
    
    print("Rendering trees:")
    for tree in trees:
        print(f"  {tree.render()}")
    
    print(f"\nTree types created: {len(TreeFactory._tree_types)}")
    print(f"Total trees: {len(trees)}")

