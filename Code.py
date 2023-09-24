from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self, rover):
        pass

# Concrete Commands
class MoveForward(Command):
    def execute(self, rover):
        rover.move()

class TurnLeft(Command):
    def execute(self, rover):
        rover.turn_left()

class TurnRight(Command):
    def execute(self, rover):
        rover.turn_right()

# Receiver (Rover)
class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

    def turn_left(self):
        directions = ['N', 'W', 'S', 'E']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % 4]

    def turn_right(self):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % 4]

    def get_status(self):
        return f"Rover is at ({self.x}, {self.y}) facing {self.direction}. No obstacles detected."

# Command Factory
class CommandFactory:
    @staticmethod
    def create_command(command_str):
        if command_str == 'M':
            return MoveForward()
        elif command_str == 'L':
            return TurnLeft()
        elif command_str == 'R':
            return TurnRight()
        else:
            raise ValueError(f"Invalid command: {command_str}")

# Composite Pattern: Grid with Obstacles
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def is_obstacle(self, x, y):
        return (x, y) in self.obstacles

# Invoker
class RoverController:
    def __init__(self, rover, grid):
        self.rover = rover
        self.grid = grid

    def execute_commands(self, command_strs):
        for command_str in command_strs:
            command = CommandFactory.create_command(command_str)
            command.execute(self.rover)

if __name__ == "__main__":
    grid = Grid(10, 10)
    grid.add_obstacle(2, 2)
    grid.add_obstacle(3, 5)

    rover = Rover(0, 0, 'N')

    command_strs = ['M', 'M', 'R', 'M', 'L', 'M']

    controller = RoverController(rover, grid)
    controller.execute_commands(command_strs)

    final_position = (rover.x, rover.y, rover.direction)
    status_report = rover.get_status()

    print(f"Final Position: {final_position}")
    print(f"Status Report: {status_report}")
