"""
Proxy Design Pattern

The Proxy pattern provides a surrogate or placeholder for another object to
control access to it. The proxy acts as an intermediary between client and real object.

Use cases:
    - Lazy initialization
    - Access control
    - Remote proxies
    - Caching
    - Logging
"""


from abc import ABC, abstractmethod


# Subject interface
class Image(ABC):
    """Subject interface."""
    
    @abstractmethod
    def display(self):
        """Display the image."""
        pass


# Real subject
class RealImage(Image):
    """Real image class that loads from disk."""
    
    def __init__(self, filename):
        self.filename = filename
        self.load_from_disk()
    
    def load_from_disk(self):
        """Simulate loading image from disk."""
        print(f"Loading {self.filename} from disk...")
    
    def display(self):
        print(f"Displaying {self.filename}")


# Proxy
class ProxyImage(Image):
    """Proxy that controls access to RealImage."""
    
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None
    
    def display(self):
        """Lazy initialization: create RealImage only when needed."""
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


# Example usage
if __name__ == "__main__":
    # Image is not loaded until display() is called
    image = ProxyImage("photo.jpg")
    
    print("Image proxy created (image not loaded yet)")
    print("\nDisplaying image (now it will be loaded):")
    image.display()
    
    print("\nDisplaying again (already loaded):")
    image.display()

