"""
Interface Example in Python

Python doesn't have explicit interfaces like Java or TypeScript, but we can
achieve similar functionality using abstract base classes (ABC) from the abc module.

This demonstrates how to create interface-like structures in Python.
"""


from abc import ABC, abstractmethod


# Interface-like abstract class
class Vehicle(ABC):
    """Abstract base class that acts like an interface."""
    
    @abstractmethod
    def start(self):
        """Start the vehicle."""
        pass
    
    @abstractmethod
    def stop(self):
        """Stop the vehicle."""
        pass
    
    @abstractmethod
    def get_speed(self):
        """Get current speed."""
        pass


# Concrete implementation
class Car(Vehicle):
    """Concrete implementation of Vehicle interface."""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0
        self.is_running = False
    
    def start(self):
        """Start the car."""
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model} ({self.year}) is starting."
        return f"{self.brand} {self.model} is already running."
    
    def stop(self):
        """Stop the car."""
        if self.is_running:
            self.is_running = False
            self.speed = 0
            return f"{self.brand} {self.model} is stopping."
        return f"{self.brand} {self.model} is already stopped."
    
    def get_speed(self):
        """Get current speed."""
        return self.speed
    
    def accelerate(self, amount):
        """Accelerate the car."""
        if self.is_running:
            self.speed += amount
            return f"Accelerating to {self.speed} mph"
        return "Cannot accelerate: Car is not running"


class ElectricCar(Car):
    """Electric car implementation."""
    
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.electric = True
    
    def start(self):
        """Start the electric car."""
        return f"{self.brand} {self.model} ({self.year}) is starting silently (electric)."


# Example usage
if __name__ == "__main__":
    # Regular car
    car = Car("Toyota", "Camry", 2014)
    print(car.start())
    print(car.accelerate(30))
    print(f"Speed: {car.get_speed()} mph")
    print(car.stop())
    
    # Electric car
    print("\n" + "="*50)
    tesla = ElectricCar("Tesla", "Model 3", 2023, "75 kWh")
    print(tesla.start())
    print(tesla.accelerate(50))
    print(f"Speed: {tesla.get_speed()} mph")
    print(tesla.stop())
    
    # Type checking
    print("\n" + "="*50)
    print("Type checking:")
    print(f"car is Vehicle: {isinstance(car, Vehicle)}")
    print(f"tesla is Vehicle: {isinstance(tesla, Vehicle)}")
    print(f"tesla is Car: {isinstance(tesla, Car)}")

