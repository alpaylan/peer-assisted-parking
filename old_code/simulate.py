import simpy
import os
import time
NOTIF_RANGE = 5

class Position():
    def __init__(self, y = 0, x = 0):
        self.y = y
        self.x = x
    def __sub__(self, other):
        return Position(self.y - other.y, self.x - other.x)
    def __add__(self, other):
        return Position(self.y + other.y, self.x + other.x)
    def __str__(self):
        return "(" + str(self.y) + ", " + str(self.x) + ")"
    def turn(self):
        tmp = self.y
        self.y = self.x
        self.x = tmp

class Grid():
    def __init__(self, m = 1, n = 1):
        self.grid = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if(i % 7 <= 2 and j % 7 <= 2): # Building
                    self.grid[i][j] = "#"
                elif((i % 7 == 3 and j % 7 == 3) # Traffic Light
                    or (i % 7 == 6 and j % 7 == 6)
                    or (i % 7 == 3 and j % 7 == 6)
                    or (i % 7 == 6 and j % 7 == 3)):
                    self.grid[i][j] = 1
                elif((i % 7 == 3 and j % 7 < 3) # Parking Spot
                    or (i % 7 < 3 and j % 7 == 3)
                    or (i % 7 < 3 and j % 7 == 6)
                    or (i % 7 == 6 and j % 7 <= 3)):
                    self.grid[i][j] = 2
                elif((i % 7 == 5 and j % 7 == 5) # Intersection
                    or (i % 7 == 4 and j % 7 == 4)
                    or (i % 7 == 4 and j % 7 == 5)
                    or (i % 7 == 5 and j % 7 == 4)):
                    self.grid[i][j] = "x"
                elif(i % 7 == 5): # West  Road
                    self.grid[i][j] = ">"
                elif(j % 7 == 5): # North Road
                    self.grid[i][j] = "^"
                elif(i % 7 == 4): # East and South Road
                    self.grid[i][j] = "<"
                elif(j % 7 == 4):
                    self.grid[i][j] = "v"
    def __str__(self):
        g_str = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                g_str += str(self.grid[i][j]) + " "
            g_str += "\n"
        g_str = g_str[:len(g_str) - 1]
        return g_str

# class City(object):
#     def __init__(self, env, grid):
#         self.env = env
#         self.grid = grid

class Car(object):
    def __init__(self, c_pos, t_pos, grid):
        # self.env = env
        self.c_pos = c_pos
        self.t_pos = t_pos
        self.grid = grid
        self.calculate_direction() # self.c_dir
        self.notif_range = NOTIF_RANGE
        self.park_spaces = []


    def __str__(self):
        return "(" + str(self.c_pos.x) + "," + str(self.c_pos.y) + ")"

    def is_out(self):
        return (self.c_pos.x <= 0
            or self.c_pos.y <= 0
            or self.c_pos.x >= len(self.grid)
            or self.c_pos.y >= len(self.grid))

    def move(self):
        self.calculate_direction()
        return self.c_pos + self.c_dir

    def calculate_direction(self):
        print(self.grid[self.c_pos.x][self.c_pos.y])
        if(self.grid[self.c_pos.x][self.c_pos.y] == ">"):
            self.c_dir = Position(1, 0)
        elif(self.grid[self.c_pos.x][self.c_pos.y] == "<"):
            self.c_dir = Position(-1, 0)
        elif(self.grid[self.c_pos.x][self.c_pos.y] == "^"):
            self.c_dir = Position(0, -1)
        elif(self.grid[self.c_pos.x][self.c_pos.y] == "v"):
            self.c_dir = Position(0, 1)
        else:
            self.c_dir.turn()
# Create environment and start processes
# env = simpy.Environment()

g = Grid(24, 24)
import copy
g_original = copy.deepcopy(g)

c1 = Car(Position(4,0), Position(5, 23), g.grid)
c2 = Car(Position(5,23), Position(4, 0), g.grid)
while True:
    move_list = {}
    old_sym = {}
    move_list[c1] = c1.move()
    move_list[c2] = c2.move()
    for i in move_list:
        if(i.is_out()):
            print("Alarm")
            exit(0)
        old_sym[i] = g.grid[i.c_pos.x][i.c_pos.y]
        g.grid[i.c_pos.x][i.c_pos.y] = "c"

    os.system("clear")
    print(g)

    time.sleep(3)
