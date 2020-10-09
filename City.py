from enum import Enum

from Position import Position
from LaneType import LaneType
"""
City is represented with an m*n grid.
It consists of b_num*b_num buildings with size b_size*b_size
equality seperated by 1 parking spaces and 2 roads.
"""
class CityType(Enum):
    Default = 0
    Bordered = 1
    Line = 2

class City:
    def __init__(self, b_size:int = 1, b_num:int = 1, c_type = CityType.Default) -> None:
        self.type = c_type
        if(c_type == CityType.Default):
            self.grid = self.create_grid(b_num * (b_size + 4) - 4, b_num * (b_size + 4) - 4, b_size)
        elif(c_type == CityType.Bordered):
            self.grid = self.create_bordered_grid(b_size, b_num)
        elif(c_type == CityType.Line):
            pass
    def __str__(self) -> str:
        g_str = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                g_str += str(self.grid[i][j]) + " "
            g_str += "\n"
        g_str = g_str[:len(g_str) - 1]
        return g_str
    
    def print_city_with_cars(self, car_position_list):
        g_str = ""
        g_str += "".ljust(3)
        for i in range(len(self.grid)):
            g_str += str(i).ljust(3)
        g_str += "\n"
        for i in range(len(self.grid)):
            g_str += str(i).ljust(3)
            for j in range(len(self.grid[0])):
                if(Position(j, i) in car_position_list):
                    g_str += "c".ljust(3)
                else:
                    g_str += str(self.grid[i][j]).ljust(3)
            g_str += "\n"
        g_str = g_str[:len(g_str) - 1]
        return g_str

    def __getitem__(self, key):
        (k1, k2) = key
        return self.grid[k2][k1]
    
    def get(self, k1, k2):
        return self.grid[k2][k1]

    def __setitem__(self, key, item):
        (k1, k2) = key
        self.grid[k2][k1] = item
    
    def set(self, k1, k2, item):
        self.grid[k2][k1] = item

    def create_grid(self, m, n, b):
        # M x N grid 
        grid = [[0 for _ in range(m)] for _ in range(n)]
        t = b + 4

        for i in range(m):
                for j in range(n):
                    
                    # Building
                    if(i % t <= b-1 and j % t <= b-1):
                        grid[i][j] = LaneType.Building
                    
                    # Traffic Light
                    elif((i % t == b and j % t == b)
                        or (i % t == b+3 and j % t == b+3)
                        or (i % t == b and j % t == b+3)
                        or (i % t == b+3 and j % t == b)):
                        grid[i][j] = LaneType.TrafficLight
                    
                    # Parking Spot
                    elif((i % t == b and j % t < b)
                        or (i % t < b and j % t == b)
                        or (i % t < b and j % t == b+3)
                        or (i % t == b+3 and j % t <= b)):
                        grid[i][j] = LaneType.Park
                    
                    # Intersection
                    elif((i % t == b + 2 and j % t == b + 2)
                        or (i % t == b+1 and j % t == b+1)
                        or (i % t == b+1 and j % t == b + 2)
                        or (i % t == b + 2 and j % t == b+1)):
                        grid[i][j] = LaneType.CrossRoad
                    
                    # East Road
                    elif(i % t == b + 2):
                        grid[i][j] = LaneType.East

                    # North Road
                    elif(j % t == b + 2):
                        grid[i][j] = LaneType.North
                    
                    # West Road
                    elif(i % t == b+1):
                        grid[i][j] = LaneType.West
                    
                    # South Road
                    elif(j % t == b+1):
                        grid[i][j] = LaneType.South
        return grid

    def lane_type_of_position(self, position: Position):
        return self[position.x, position.y]

    def create__grid(self, b_size, b_num, building_positions):
        for x, y in building_positions:
            b_left = x - b_size/2
            b_right = x + b_size/2
            b_up = y - b_size/2
            b_down = y + b_size/2

            mark_building()
            mark_parking()   
            mark_lights()         
            mark_inner_loop() 
            mark_outer_loop()

        def mark_building():
            for i in range(b_left, b_right):
                for j in range(b_up, b_down):
                    self.grid[i, j] = LaneType.Building

        def mark_lights():
            self.grid[b_up - 1, b_left - 1] = LaneType.TrafficLight
            self.grid[b_up - 1, b_right + 1] = LaneType.TrafficLight
            self.grid[b_down + 1, b_left - 1] = LaneType.TrafficLight
            self.grid[b_down + 1, b_right + 1] = LaneType.TrafficLight

        def mark_parking():
            mark_four_sides(LaneType.Park, 1)

        def mark_inner_loop():
            mark_four_sides(LaneType.InnerLoop, 2)

        def mark_outer_loop():
            mark_four_sides(LaneType.OuterLoop, 3)

        def mark_four_sides(mark, offset):
            mark_down()
            mark_up()
            mark_left()
            mark_right()

            def mark_up():
                for i in range(b_left, b_right):
                    j = b_up + offset
                    self.grid[i, j] = mark

            def mark_down():
                for i in range(b_left, b_right):
                    j = b_down - offset
                    self.grid[i, j] = mark

            def mark_left():
                for i in range(b_up, b_down):
                    j = b_left - offset
                    self.grid[i, j] = mark

            def mark_right():
                for i in range(b_up, b_down):
                    j = b_right + offset
                    self.grid[i, j] = mark

    def create_bordered_grid(self, b_size, b_num):
        square = b_size + 4

        grid = [[0 for _ in range(square * b_num)] for _ in range(square * b_num)]
        
        
        return grid
    
    def is_inner_loop(self):

        pass
    def is_outer_loop(self):
        pass
    def is_cross(self):
        pass
