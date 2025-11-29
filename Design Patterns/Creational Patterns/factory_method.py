"""
Factory Method Design Pattern

The Factory Method pattern provides an interface for creating objects,
but lets subclasses decide which class to instantiate.

Use cases:
    - When you don't know the exact types of objects at compile time
    - When you want to provide a library of products and expose only interfaces
    - When you want to extend your code with new products easily
"""


from abc import ABC, abstractmethod


# Product interface
class Animal(ABC):
    """Abstract product class."""
    
    @abstractmethod
    def speak(self):
        """Make the animal speak."""
        pass


# Concrete products
class Dog(Animal):
    """Concrete product: Dog."""
    
    def speak(self):
        return "Woof!"


class Cat(Animal):
    """Concrete product: Cat."""
    
    def speak(self):
        return "Meow!"


class Duck(Animal):
    """Concrete product: Duck."""
    
    def speak(self):
        return "Quack!"


# Creator interface
class AnimalFactory(ABC):
    """Abstract creator class."""
    
    @abstractmethod
    def create_animal(self):
        """Factory method to create an animal."""
        pass
    
    def get_animal_sound(self):
        """Use the factory method."""
        animal = self.create_animal()
        return animal.speak()


# Concrete creators
class DogFactory(AnimalFactory):
    """Concrete creator: Dog factory."""
    
    def create_animal(self):
        return Dog()


class CatFactory(AnimalFactory):
    """Concrete creator: Cat factory."""
    
    def create_animal(self):
        return Cat()


class DuckFactory(AnimalFactory):
    """Concrete creator: Duck factory."""
    
    def create_animal(self):
        return Duck()


# Example usage
if __name__ == "__main__":
    # Using factory methods
    dog_factory = DogFactory()
    print(f"Dog says: {dog_factory.get_animal_sound()}")
    
    cat_factory = CatFactory()
    print(f"Cat says: {cat_factory.get_animal_sound()}")
    
    duck_factory = DuckFactory()
    print(f"Duck says: {duck_factory.get_animal_sound()}")

