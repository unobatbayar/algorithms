"""
Memento Design Pattern

The Memento pattern provides the ability to restore an object to its previous
state without violating encapsulation. It captures and externalizes an object's
internal state.

Use cases:
    - Undo/Redo functionality
    - Save/Load game states
    - Transaction rollback
    - State snapshots
"""


# Memento
class Memento:
    """Memento class that stores state."""
    
    def __init__(self, state):
        self._state = state
    
    def get_state(self):
        """Get saved state."""
        return self._state


# Originator
class TextEditor:
    """Originator class that creates and uses mementos."""
    
    def __init__(self):
        self._content = ""
    
    def write(self, text):
        """Write text."""
        self._content += text
    
    def get_content(self):
        """Get current content."""
        return self._content
    
    def save(self):
        """Save current state to memento."""
        return Memento(self._content)
    
    def restore(self, memento):
        """Restore state from memento."""
        self._content = memento.get_state()


# Caretaker
class History:
    """Caretaker that manages mementos."""
    
    def __init__(self):
        self._history = []
    
    def save(self, editor):
        """Save editor state."""
        self._history.append(editor.save())
    
    def undo(self, editor):
        """Restore previous state."""
        if self._history:
            memento = self._history.pop()
            editor.restore(memento)
            return True
        return False


# Example usage
if __name__ == "__main__":
    editor = TextEditor()
    history = History()
    
    editor.write("Hello ")
    history.save(editor)
    print(f"Content: {editor.get_content()}")
    
    editor.write("World")
    history.save(editor)
    print(f"Content: {editor.get_content()}")
    
    editor.write("!")
    print(f"Content: {editor.get_content()}")
    
    print("\nUndoing...")
    history.undo(editor)
    print(f"Content: {editor.get_content()}")
    
    print("\nUndoing again...")
    history.undo(editor)
    print(f"Content: {editor.get_content()}")

