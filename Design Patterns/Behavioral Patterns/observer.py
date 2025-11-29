"""
Observer Design Pattern

The Observer pattern defines a one-to-many dependency between objects so that
when one object changes state, all its dependents are notified and updated automatically.

Use cases:
    - Event handling systems
    - Model-View architectures
    - Real-time data feeds
    - Notification systems
"""


from abc import ABC, abstractmethod


# Subject (Observable)
class Subject(ABC):
    """Abstract subject class."""
    
    @abstractmethod
    def attach(self, observer):
        """Attach an observer."""
        pass
    
    @abstractmethod
    def detach(self, observer):
        """Detach an observer."""
        pass
    
    @abstractmethod
    def notify(self):
        """Notify all observers."""
        pass


# Concrete subject
class WeatherStation(Subject):
    """Concrete subject: Weather station."""
    
    def __init__(self):
        self._observers = []
        self._temperature = 0
    
    def attach(self, observer):
        """Attach an observer."""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        """Detach an observer."""
        self._observers.remove(observer)
    
    def notify(self):
        """Notify all observers."""
        for observer in self._observers:
            observer.update(self._temperature)
    
    def set_temperature(self, temperature):
        """Set temperature and notify observers."""
        self._temperature = temperature
        self.notify()


# Observer interface
class Observer(ABC):
    """Abstract observer class."""
    
    @abstractmethod
    def update(self, temperature):
        """Update observer with new temperature."""
        pass


# Concrete observers
class TemperatureDisplay(Observer):
    """Concrete observer: Temperature display."""
    
    def __init__(self, name):
        self.name = name
        self.temperature = 0
    
    def update(self, temperature):
        """Update temperature."""
        self.temperature = temperature
        print(f"{self.name}: Temperature is now {self.temperature}°C")


class AlertSystem(Observer):
    """Concrete observer: Alert system."""
    
    def __init__(self, threshold):
        self.threshold = threshold
        self.temperature = 0
    
    def update(self, temperature):
        """Update and check threshold."""
        self.temperature = temperature
        if self.temperature > self.threshold:
            print(f"ALERT: Temperature {self.temperature}°C exceeds threshold {self.threshold}°C!")


# Example usage
if __name__ == "__main__":
    # Create subject
    weather_station = WeatherStation()
    
    # Create observers
    display1 = TemperatureDisplay("Display 1")
    display2 = TemperatureDisplay("Display 2")
    alert = AlertSystem(25)
    
    # Attach observers
    weather_station.attach(display1)
    weather_station.attach(display2)
    weather_station.attach(alert)
    
    # Change temperature (observers will be notified)
    print("Setting temperature to 20°C:")
    weather_station.set_temperature(20)
    
    print("\nSetting temperature to 30°C:")
    weather_station.set_temperature(30)
    
    # Detach an observer
    print("\nDetaching Display 1:")
    weather_station.detach(display1)
    
    print("Setting temperature to 15°C:")
    weather_station.set_temperature(15)

