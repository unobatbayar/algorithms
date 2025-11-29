"""
Mediator Design Pattern

The Mediator pattern defines an object that encapsulates how a set of objects
interact. It promotes loose coupling by keeping objects from referring to each
other explicitly.

Use cases:
    - Reducing coupling between components
    - Simplifying object interactions
    - Centralizing control logic
    - Chat applications, air traffic control
"""


from abc import ABC, abstractmethod


# Mediator interface
class Mediator(ABC):
    """Abstract mediator interface."""
    
    @abstractmethod
    def notify(self, sender, event):
        """Notify mediator of an event."""
        pass


# Concrete mediator
class ChatRoom(Mediator):
    """Concrete mediator: Chat room."""
    
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        """Add user to chat room."""
        self.users.append(user)
        user.mediator = self
    
    def notify(self, sender, event):
        """Handle notification from a user."""
        for user in self.users:
            if user != sender:
                user.receive(event)


# Colleague interface
class Colleague(ABC):
    """Abstract colleague interface."""
    
    def __init__(self, name):
        self.name = name
        self.mediator = None
    
    @abstractmethod
    def send(self, message):
        """Send a message."""
        pass
    
    @abstractmethod
    def receive(self, message):
        """Receive a message."""
        pass


# Concrete colleagues
class User(Colleague):
    """Concrete colleague: User."""
    
    def send(self, message):
        if self.mediator:
            self.mediator.notify(self, f"{self.name}: {message}")
    
    def receive(self, message):
        print(f"[{self.name}] received: {message}")


# Example usage
if __name__ == "__main__":
    chat_room = ChatRoom()
    
    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Charlie")
    
    chat_room.add_user(user1)
    chat_room.add_user(user2)
    chat_room.add_user(user3)
    
    user1.send("Hello everyone!")
    user2.send("Hi Alice!")
    user3.send("Hey there!")

