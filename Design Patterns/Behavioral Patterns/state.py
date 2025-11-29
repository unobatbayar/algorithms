"""
State Design Pattern

The State pattern allows an object to alter its behavior when its internal state
changes. The object will appear to change its class.

Use cases:
    - Object behavior depends on its state
    - Many conditional statements based on object state
    - State transitions are well-defined
"""


from abc import ABC, abstractmethod


# State interface
class State(ABC):
    """Abstract state interface."""
    
    @abstractmethod
    def handle(self, context):
        """Handle state-specific behavior."""
        pass


# Concrete states
class PlayingState(State):
    """Concrete state: Playing."""
    
    def handle(self, context):
        print("Music is already playing")
        return self
    
    def __str__(self):
        return "Playing"


class PausedState(State):
    """Concrete state: Paused."""
    
    def handle(self, context):
        print("Resuming music...")
        context.state = PlayingState()
        return context.state
    
    def __str__(self):
        return "Paused"


class StoppedState(State):
    """Concrete state: Stopped."""
    
    def handle(self, context):
        print("Starting music...")
        context.state = PlayingState()
        return context.state
    
    def __str__(self):
        return "Stopped"


# Context
class MusicPlayer:
    """Context class that maintains state."""
    
    def __init__(self):
        self.state = StoppedState()
    
    def play(self):
        """Play music."""
        self.state = self.state.handle(self)
    
    def pause(self):
        """Pause music."""
        if isinstance(self.state, PlayingState):
            print("Pausing music...")
            self.state = PausedState()
        else:
            print("Cannot pause: Music is not playing")
    
    def stop(self):
        """Stop music."""
        if not isinstance(self.state, StoppedState):
            print("Stopping music...")
            self.state = StoppedState()
        else:
            print("Music is already stopped")


# Example usage
if __name__ == "__main__":
    player = MusicPlayer()
    
    print(f"Initial state: {player.state}")
    player.play()
    print(f"State after play: {player.state}")
    
    player.pause()
    print(f"State after pause: {player.state}")
    
    player.play()
    print(f"State after play: {player.state}")
    
    player.stop()
    print(f"State after stop: {player.state}")

