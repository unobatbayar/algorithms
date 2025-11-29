"""
Singleton Design Pattern

The Singleton pattern ensures a class has only one instance and provides
a global point of access to it.

Use cases:
    - Database connections
    - Logger instances
    - Configuration managers
    - Cache managers
"""


class Singleton:
    """Singleton implementation using __new__ method."""
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.value = None
            self.initialized = True
    
    def set_value(self, value):
        """Set a value."""
        self.value = value
    
    def get_value(self):
        """Get the value."""
        return self.value


# Alternative: Using decorator
def singleton(cls):
    """Singleton decorator."""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


@singleton
class Config:
    """Example singleton using decorator."""
    
    def __init__(self):
        self.settings = {}


# Example usage
if __name__ == "__main__":
    # Test basic singleton
    s1 = Singleton()
    s1.set_value("Hello")
    
    s2 = Singleton()
    print(f"s1 value: {s1.get_value()}")
    print(f"s2 value: {s2.get_value()}")
    print(f"Same instance: {s1 is s2}")
    
    # Test decorator singleton
    c1 = Config()
    c1.settings['key'] = 'value'
    
    c2 = Config()
    print(f"\nc1 settings: {c1.settings}")
    print(f"c2 settings: {c2.settings}")
    print(f"Same instance: {c1 is c2}")

