from position import *
from enum import Enum

class CarMode(Enum):
    idle = 0
    moving = 1
    parking = 2
    parked = 3

class Car():
    def __init__(self, x1, y1, x2, y2, grid):
        self.pos = Position(x1, y1)
        self.target = Position(x2, y2)
        self.mode = CarMode.idle
        self.grid = grid
        self.dir = Direction(0, 0)
        self.dir = self.direction()
        self.next_pos = self.pos
        self.lane = self.grid[self.pos.x, self.pos.y]

    def __str__(self):
        return "(" + str(self.pos[0]) + "," + str(self.pos[1]) + ")"

    def moving_direction(self):
        if(self.grid[self.pos[0], self.pos[1]] == ">"):
            return Direction(1, 0)
        elif(self.grid[self.pos[0], self.pos[1]] == "<"):
            return Direction(-1, 0)
        elif(self.grid[self.pos[0], self.pos[1]] == "^"):
            return Direction(0, -1)
        elif(self.grid[self.pos[0], self.pos[1]] == "v"):
            return Direction(0, 1)
        else:
            return self.dir_target()

    def parking_direction(self):
        return Direction(0, 0)

    def direction (self):
        if(self.mode == CarMode.moving):
            return self.moving_direction()
        elif(self.mode == CarMode.parking):
            return self.parking_direction()
        else:
            return Direction(0, 0)

    def dir_target(self):
        relative_positioning = Position(0, 0)

        if(self.pos.x > self.target.x):
            relative_positioning.x = -1
        elif(self.pos.x < self.target.x):
            relative_positioning.x = 1

        if(self.pos.y > self.target.y):
            relative_positioning.y = -1
        elif(self.pos.y < self.target.y):
            relative_positioning.y = 1

        # There are 4 cases
        if(relative_positioning == Position(0, 0)):
            return Direction(0, 0)
        # Upper Right X
        elif(self.grid[self.pos.x - 1, self.pos.y] == "x"
            and self.grid[self.pos.x, self.pos.y + 1] == "x"):
            if(relative_positioning.y == -1):   # Go Up
                return Direction(0, -1)
            elif(relative_positioning.x == -1): # Go Left
                return Direction(-1, 0)
            else:                               # Go Below
                return Direction(0, 1)
        # Upper Left X
        elif(self.grid[self.pos.x + 1, self.pos.y] == "x"
            and self.grid[self.pos.x, self.pos.y + 1] == "x"):
            if(relative_positioning.x == -1):   # Go Left
                return Direction(-1, 0)
            elif(relative_positioning.y == 1):  # Go Below
                return Direction(0, 1)
            else:                               # Go Right
                return Direction(1, 0)
        # Lower Left X
        elif(self.grid[self.pos.x + 1, self.pos.y] == "x"
            and self.grid[self.pos.x, self.pos.y - 1] == "x"):
            if(relative_positioning.y == 1):    # Go Below
                return Direction(0, 1)
            elif(relative_positioning.x == 1):  # Go Right
                return Direction(1, 0)
            else:                               # Go Up
                return Direction(0, -1)
        # Lower Right X
        elif(self.grid[self.pos.x - 1, self.pos.y] == "x"
            and self.grid[self.pos.x, self.pos.y - 1] == "x"):
            if(relative_positioning.x == 1):    # Go Right
                return Direction(1, 0)
            elif(relative_positioning.y == -1): # Go Up
                return Direction(0, -1)
            else:                               # Go Left
                return Direction(-1, 0)

    def next_out(self):
        return (self.next_pos.x < 0
            or self.next_pos.y < 0
            or self.next_pos.x >= len(self.grid.grid)
            or self.next_pos.y >= len(self.grid.grid))

    def calculate(self):
        self.dir = self.direction()
        self.next_pos = self.pos + self.dir

    def advance(self):
        self.pos = self.next_pos

    def move(self):
        self.mode = CarMode.moving

    def park(self):
        self.mode = CarMode.parking

    def end_park(self):
        self.mode = CarMode.parked
