"""
Template Method Design Pattern

The Template Method pattern defines the skeleton of an algorithm in a method,
deferring some steps to subclasses. It lets subclasses redefine certain steps
without changing the algorithm's structure.

Use cases:
    - Code reuse
    - Framework design
    - Defining algorithm structure
    - Preventing code duplication
"""


from abc import ABC, abstractmethod


# Abstract class with template method
class DataProcessor(ABC):
    """Abstract class defining template method."""
    
    def process(self):
        """Template method defining the algorithm structure."""
        self.read_data()
        self.process_data()
        self.save_data()
    
    @abstractmethod
    def read_data(self):
        """Abstract method: Read data."""
        pass
    
    @abstractmethod
    def process_data(self):
        """Abstract method: Process data."""
        pass
    
    def save_data(self):
        """Concrete method: Save data (can be overridden)."""
        print("Saving data to default location...")


# Concrete implementations
class CSVProcessor(DataProcessor):
    """Concrete implementation: CSV processor."""
    
    def read_data(self):
        print("Reading data from CSV file...")
    
    def process_data(self):
        print("Processing CSV data...")


class JSONProcessor(DataProcessor):
    """Concrete implementation: JSON processor."""
    
    def read_data(self):
        print("Reading data from JSON file...")
    
    def process_data(self):
        print("Processing JSON data...")
    
    def save_data(self):
        print("Saving data to JSON file...")


class XMLProcessor(DataProcessor):
    """Concrete implementation: XML processor."""
    
    def read_data(self):
        print("Reading data from XML file...")
    
    def process_data(self):
        print("Processing XML data...")


# Example usage
if __name__ == "__main__":
    print("CSV Processor:")
    csv_processor = CSVProcessor()
    csv_processor.process()
    
    print("\nJSON Processor:")
    json_processor = JSONProcessor()
    json_processor.process()
    
    print("\nXML Processor:")
    xml_processor = XMLProcessor()
    xml_processor.process()

