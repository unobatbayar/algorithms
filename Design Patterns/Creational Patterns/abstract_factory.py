"""
Abstract Factory Design Pattern

The Abstract Factory pattern provides an interface for creating families of
related objects without specifying their concrete classes.

Use cases:
    - When you need to create families of related products
    - When you want to provide a library of products and reveal only interfaces
    - When you want to ensure products are compatible with each other
"""


from abc import ABC, abstractmethod


# Abstract products
class Button(ABC):
    """Abstract product: Button."""
    
    @abstractmethod
    def render(self):
        """Render the button."""
        pass


class Checkbox(ABC):
    """Abstract product: Checkbox."""
    
    @abstractmethod
    def render(self):
        """Render the checkbox."""
        pass


# Concrete products for Windows
class WindowsButton(Button):
    """Concrete product: Windows button."""
    
    def render(self):
        return "Rendering Windows button"


class WindowsCheckbox(Checkbox):
    """Concrete product: Windows checkbox."""
    
    def render(self):
        return "Rendering Windows checkbox"


# Concrete products for Mac
class MacButton(Button):
    """Concrete product: Mac button."""
    
    def render(self):
        return "Rendering Mac button"


class MacCheckbox(Checkbox):
    """Concrete product: Mac checkbox."""
    
    def render(self):
        return "Rendering Mac checkbox"


# Abstract factory
class GUIFactory(ABC):
    """Abstract factory interface."""
    
    @abstractmethod
    def create_button(self) -> Button:
        """Create a button."""
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """Create a checkbox."""
        pass


# Concrete factories
class WindowsFactory(GUIFactory):
    """Concrete factory: Windows GUI."""
    
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    """Concrete factory: Mac GUI."""
    
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# Client code
class Application:
    """Application that uses the factory."""
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()
    
    def render(self):
        """Render the UI."""
        print(self.button.render())
        print(self.checkbox.render())


# Example usage
if __name__ == "__main__":
    # Windows application
    print("Windows Application:")
    windows_app = Application(WindowsFactory())
    windows_app.render()
    
    # Mac application
    print("\nMac Application:")
    mac_app = Application(MacFactory())
    mac_app.render()

