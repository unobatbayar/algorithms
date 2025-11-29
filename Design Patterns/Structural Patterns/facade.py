"""
Facade Design Pattern

The Facade pattern provides a simplified interface to a complex subsystem.
It defines a higher-level interface that makes the subsystem easier to use.

Use cases:
    - Simplifying complex subsystems
    - Providing a simple interface to a complex library
    - Reducing dependencies between client and subsystem
"""


# Complex subsystem classes
class CPU:
    """CPU subsystem."""
    
    def freeze(self):
        return "CPU: Freezing..."
    
    def jump(self, position):
        return f"CPU: Jumping to {position}"
    
    def execute(self):
        return "CPU: Executing..."


class Memory:
    """Memory subsystem."""
    
    def load(self, position, data):
        return f"Memory: Loading data '{data}' at position {position}"


class HardDrive:
    """Hard drive subsystem."""
    
    def read(self, lba, size):
        return f"HardDrive: Reading {size} bytes from LBA {lba}"


# Facade
class Computer:
    """Facade that simplifies the computer boot process."""
    
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()
    
    def start_computer(self):
        """Simplified method to start the computer."""
        steps = []
        steps.append(self.cpu.freeze())
        steps.append(self.memory.load("0x0000", "boot_data"))
        steps.append(self.cpu.jump("0x0000"))
        steps.append(self.cpu.execute())
        steps.append(self.hard_drive.read("0", "1024"))
        return "\n".join(steps)


# Example usage
if __name__ == "__main__":
    computer = Computer()
    print("Starting computer:")
    print(computer.start_computer())

