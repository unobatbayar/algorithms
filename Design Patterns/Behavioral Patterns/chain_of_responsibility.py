"""
Chain of Responsibility Design Pattern

The Chain of Responsibility pattern passes requests along a chain of handlers.
Each handler decides either to process the request or pass it to the next handler.

Use cases:
    - Multiple handlers for a request
    - Decoupling sender and receiver
    - Dynamic handler assignment
    - Event handling systems
"""


from abc import ABC, abstractmethod


# Handler interface
class Handler(ABC):
    """Abstract handler class."""
    
    def __init__(self):
        self.next_handler = None
    
    def set_next(self, handler):
        """Set next handler in chain."""
        self.next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request):
        """Handle the request."""
        pass


# Concrete handlers
class ConcreteHandler1(Handler):
    """Concrete handler 1."""
    
    def handle(self, request):
        if request == "Request1":
            return f"Handler1: Processing {request}"
        elif self.next_handler:
            return self.next_handler.handle(request)
        return None


class ConcreteHandler2(Handler):
    """Concrete handler 2."""
    
    def handle(self, request):
        if request == "Request2":
            return f"Handler2: Processing {request}"
        elif self.next_handler:
            return self.next_handler.handle(request)
        return None


class ConcreteHandler3(Handler):
    """Concrete handler 3."""
    
    def handle(self, request):
        if request == "Request3":
            return f"Handler3: Processing {request}"
        elif self.next_handler:
            return self.next_handler.handle(request)
        return "No handler found for this request"


# Example usage
if __name__ == "__main__":
    # Create handlers
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()
    
    # Build chain
    handler1.set_next(handler2).set_next(handler3)
    
    # Process requests
    requests = ["Request1", "Request2", "Request3", "Request4"]
    
    for request in requests:
        print(f"\nProcessing {request}:")
        result = handler1.handle(request)
        print(f"  {result}")

