"""
Composite Design Pattern

The Composite pattern composes objects into tree structures to represent
part-whole hierarchies. It lets clients treat individual objects and compositions
uniformly.

Use cases:
    - Tree structures
    - File systems
    - UI components
    - Organizational structures
"""


from abc import ABC, abstractmethod


# Component interface
class FileSystemComponent(ABC):
    """Abstract component interface."""
    
    @abstractmethod
    def get_size(self):
        """Get size of component."""
        pass
    
    @abstractmethod
    def display(self, indent=0):
        """Display component."""
        pass


# Leaf
class File(FileSystemComponent):
    """Leaf class: File."""
    
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def get_size(self):
        return self.size
    
    def display(self, indent=0):
        print("  " * indent + f"File: {self.name} ({self.size} bytes)")


# Composite
class Directory(FileSystemComponent):
    """Composite class: Directory."""
    
    def __init__(self, name):
        self.name = name
        self.children = []
    
    def add(self, component):
        """Add a component."""
        self.children.append(component)
    
    def remove(self, component):
        """Remove a component."""
        self.children.remove(component)
    
    def get_size(self):
        return sum(child.get_size() for child in self.children)
    
    def display(self, indent=0):
        print("  " * indent + f"Directory: {self.name} ({self.get_size()} bytes)")
        for child in self.children:
            child.display(indent + 1)


# Example usage
if __name__ == "__main__":
    # Create file system structure
    root = Directory("root")
    
    documents = Directory("documents")
    documents.add(File("readme.txt", 100))
    documents.add(File("notes.txt", 200))
    
    pictures = Directory("pictures")
    pictures.add(File("photo1.jpg", 1000))
    pictures.add(File("photo2.jpg", 1500))
    
    root.add(documents)
    root.add(pictures)
    root.add(File("config.txt", 50))
    
    # Display structure
    root.display()

