"""
Command Design Pattern

The Command pattern encapsulates a request as an object, allowing you to
parameterize clients with different requests, queue operations, and support undo.

Use cases:
    - Undo/Redo functionality
    - Macro recording
    - Queue operations
    - Logging requests
"""


from abc import ABC, abstractmethod


# Receiver
class Light:
    """Receiver class that performs actions."""
    
    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        """Turn on the light."""
        self.is_on = True
        return "Light is ON"
    
    def turn_off(self):
        """Turn off the light."""
        self.is_on = False
        return "Light is OFF"


# Command interface
class Command(ABC):
    """Abstract command interface."""
    
    @abstractmethod
    def execute(self):
        """Execute the command."""
        pass
    
    @abstractmethod
    def undo(self):
        """Undo the command."""
        pass


# Concrete commands
class TurnOnCommand(Command):
    """Concrete command: Turn on light."""
    
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.turn_on()
    
    def undo(self):
        return self.light.turn_off()


class TurnOffCommand(Command):
    """Concrete command: Turn off light."""
    
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        return self.light.turn_off()
    
    def undo(self):
        return self.light.turn_on()


# Invoker
class RemoteControl:
    """Invoker that executes commands."""
    
    def __init__(self):
        self.command_history = []
    
    def execute_command(self, command):
        """Execute a command and add to history."""
        result = command.execute()
        self.command_history.append(command)
        return result
    
    def undo_last(self):
        """Undo the last command."""
        if self.command_history:
            command = self.command_history.pop()
            return command.undo()
        return "No command to undo"


# Example usage
if __name__ == "__main__":
    light = Light()
    remote = RemoteControl()
    
    # Execute commands
    print(remote.execute_command(TurnOnCommand(light)))
    print(remote.execute_command(TurnOffCommand(light)))
    
    # Undo
    print(f"\nUndoing last command: {remote.undo_last()}")

