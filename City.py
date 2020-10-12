from __future__ import annotations

from enum import Enum

from Position import Position
from LaneType import LaneType
"""
A city is an object that contains roads and building.
There are three types of cities.
1- Default Grid
2- Bordered Grid
3- Line

"""

"""
Default Grid Example

  0 1 2 3 4 5 6 7
0 # # 2 v ^ 2 # #
1 # # 2 v ^ 2 # #
2 2 2 1 v ^ 1 2 2
3 < < < x x < < <
4 > > > x x > > >
5 2 2 1 v ^ 1 2 2
6 # # 2 v ^ 2 # #
7 # # 2 v ^ 2 # #

"""

"""
Bordered Grid Example

v < < < < < < < < < < < < <
v > > > > > > > > > > > v ^
v ^ 1 2 2 1 v ^ 1 2 2 1 v ^ 
v ^ 2 # # 2 v ^ 2 # # 2 v ^
v ^ 2 # # 2 v ^ 2 # # 2 v ^
v ^ 1 2 2 1 v ^ 1 2 2 1 v ^
v ^ < < < < x x < < < < v ^
v ^ > > > > x x > > > > v ^
v ^ 1 2 2 1 v ^ 1 2 2 1 v ^
v ^ 2 # # 2 v ^ 2 # # 2 v ^
v ^ 2 # # 2 v ^ 2 # # 2 v ^
v ^ 1 2 2 1 v ^ 1 2 2 1 v ^
v ^ < < < < < < < < < < < ^
> > > > > > > > > > > > > ^

"""

"""
Line Example

v < < < < < < < < < < <
v > > > > > > > > > v ^
v ^ 2 2 1 v ^ 1 2 2 v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 1 v ^ 2 # # v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 1 v ^ 2 # # v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 2 v ^ 2 # # v ^ 
v ^ # # 1 v ^ 1 # # v ^ 
v ^ < < < < < < < < < ^
> > > > > > > > > > > ^

"""

class CityType(Enum):
    Default = 0
    Bordered = 1
    Line = 2

class City:
    def __init__(self, b_size:int = 1, b_num:int = 1, c_type = CityType.Default) -> None:
        self.type = c_type
        self.building_size = b_size
        self.building_num = b_num
        self.building_positions = self.calculate_building_positions()
        self.grid = self.create_empty_grid()
        self.create_grid()
    def __str__(self) -> str:
        g_str = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                g_str += str(self.grid[i][j]) + " "
            g_str += "\n"
        g_str = g_str[:len(g_str) - 1]
        return g_str
    
    def print_city_with_cars(self, car_position_list):
        """
        Prints City Grid, adding cars in given positions
        """
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
                elif((j + 1, i + 1) in self.building_positions):
                    g_str += str(self.num_free_park_spaces(j+1, i+1)).ljust(3)
                else:
                    g_str += str(self.grid[i][j]).ljust(3)
            g_str += "\n"
        g_str = g_str[:len(g_str) - 1]
        return g_str

    def __getitem__(self, key):
        """
        Get is overridden for convenient indexing
        """
        (k1, k2) = key
        return self.grid[k2][k1]
    
    def get(self, k1, k2):
        return self.grid[k2][k1]

    def __setitem__(self, key, item):
        (k1, k2) = key
        self.grid[k2][k1] = item
    
    def set(self, k1, k2, item):
        self.grid[k2][k1] = item

    def create_empty_grid(self):

        def create_empty_grid_default():
            size = (self.building_size + 4)*self.building_num - 4
            return [[0 for _ in range(size)] for _ in range(size)]

        def create_empty_grid_bordered():
            size = (self.building_size + 4)*self.building_num + 2
            return [[0 for _ in range(size)] for _ in range(size)]

        def create_empty_grid_line():
            raise NotImplementedError
        
        if(self.type == CityType.Default):
            return create_empty_grid_default()
        if(self.type == CityType.Bordered):
            return create_empty_grid_bordered()
        if(self.type == CityType.Line):
            return create_empty_grid_line()
            
    def lane_type_of_position(self, position: Position):
        return self[position.x, position.y]

    def calculate_building_positions(self):
        building_positions = []
        for i in range(self.building_num):
            for j in range(self.building_num):
                building_positions.append(self.calculate_building_position(i, j))
        
        return building_positions
   
    def calculate_building_position(self, x, y):

        def calculate_building_position_default():
            return (int(self.building_size/2 + x*(self.building_size + 4)), 
                    int(self.building_size/2 + y*(self.building_size + 4))) 

        def calculate_building_position_bordered():
            return (int(3 + (self.building_size + 1)//2 + x*(self.building_size + 4)), 
                    int(3 + (self.building_size + 1)/2 + y*(self.building_size + 4))) 

        def calculate_building_position_line():
            raise NotImplementedError

        if(self.type == CityType.Default):
            return calculate_building_position_default()
        if(self.type == CityType.Bordered):
            return calculate_building_position_bordered()
        if(self.type == CityType.Line):
            return calculate_building_position_line()

    def create_grid(self):

        for x, y in self.building_positions:
            b_left = int(x - self.building_size/2)
            b_right = int(x + self.building_size/2)
            b_up = int(y - self.building_size/2)
            b_down = int(y + self.building_size/2)

            self.mark_building(b_left, b_right, b_up, b_down)
            self.mark_parking(b_left, b_right, b_up, b_down)   
            self.mark_lights(b_left, b_right, b_up, b_down)         
            self.mark_roads(b_left, b_right, b_up, b_down) 
        if(self.type == CityType.Bordered):
            self.mark_outer_ring()

    def mark_building(self, b_left, b_right, b_up, b_down):
        for i in range(b_left, b_right):
            for j in range(b_up, b_down):
                self.mark_grid(i, j, LaneType.Building)

    def mark_lights(self, b_left, b_right, b_up, b_down):
        if(b_left - 1 >= 0 and b_up - 1 >= 0):
            self[b_left - 1, b_up - 1] = LaneType.TrafficLight
        if(b_right < len(self.grid) and b_up - 1 >= 0):
            self[b_right, b_up - 1] = LaneType.TrafficLight
        if(b_left - 1 >= 0 and b_down < len(self.grid)):
            self[b_left - 1, b_down] = LaneType.TrafficLight
        if(b_right < len(self.grid) and b_down < len(self.grid)):
            self[b_right, b_down] = LaneType.TrafficLight

    def mark_parking(self, b_left, b_right, b_up, b_down):
        self.mark_four_sides(LaneType.FreePark, 1, b_left, b_right, b_up, b_down)

    def mark_roads(self, b_left, b_right, b_up, b_down):
        self.mark_down(LaneType.Left, 2, b_left - 1, b_right + 1, b_up, b_down)
        self.mark_up(LaneType.Right, 2, b_left - 1, b_right + 1, b_up, b_down)
        self.mark_left(LaneType.Up, 2, b_left, b_right, b_up - 1, b_down + 1)
        self.mark_right(LaneType.Down, 2, b_left, b_right, b_up - 1, b_down + 1)

        
        self.mark_grid(b_left - 2, b_up - 2, LaneType.UpToRight)
        self.mark_grid(b_right + 1, b_up - 2, LaneType.RightToDown)
        self.mark_grid(b_left - 2, b_down + 1, LaneType.LeftToUp)
        self.mark_grid(b_right + 1, b_down + 1, LaneType.DownToLeft)

    def is_inside(self, x, y):
        return (x >= 0) and (x < len(self.grid)) and (y >= 0) and (y < len(self.grid))

    def mark_four_sides(self, mark, offset, b_left, b_right, b_up, b_down):
        self.mark_down(mark, offset, b_left, b_right, b_up, b_down)
        self.mark_up(mark, offset, b_left, b_right, b_up, b_down)
        self.mark_left(mark, offset, b_left, b_right, b_up, b_down)
        self.mark_right(mark, offset, b_left, b_right, b_up, b_down)

    def mark_up(self, mark, offset, b_left, b_right, b_up, b_down):
        for i in range(b_left, b_right):
            j = b_up - offset
            self.mark_grid(i, j, mark)

    def mark_down(self, mark, offset, b_left, b_right, b_up, b_down):
        for i in range(b_left, b_right):
            j = b_down + offset - 1
            self.mark_grid(i, j, mark)

    def mark_left(self, mark, offset, b_left, b_right, b_up, b_down):
        for i in range(b_up, b_down):
            j = b_left - offset
            self.mark_grid(j, i, mark)

    def mark_right(self, mark, offset, b_left, b_right, b_up, b_down):
        for i in range(b_up, b_down):
            j = b_right + offset - 1
            self.mark_grid(j, i, mark)
    
    def mark_grid(self, x, y, mark):
        if(self.is_inside(x, y)):
            self[x, y] = mark

    def mark_outer_ring(self):
        self.mark_grid(0, 0, LaneType.LeftToDown)
        self.mark_grid(len(self.grid) - 1, 0, LaneType.UpToLeft)
        self.mark_grid(0, len(self.grid) - 1, LaneType.DownToRight)
        self.mark_grid(len(self.grid) - 1, len(self.grid) - 1, LaneType.RightToUp)

        for i in range(1, len(self.grid) - 1):
            if(i % (self.building_size + 4) == 0):
                self.mark_grid(i, 0, LaneType.LeftToDown)    
            else:
                self.mark_grid(i, 0, LaneType.Left)
            if(i % (self.building_size + 4) == 1):
                self.mark_grid(i, len(self.grid) - 1, LaneType.RightToUp)
            else:
                self.mark_grid(i, len(self.grid) - 1, LaneType.Right)
            if(i % (self.building_size + 4) == 1):
                self.mark_grid(0, i, LaneType.DownToRight)
            else:
                self.mark_grid(0, i, LaneType.Down)
            if(i % (self.building_size + 4) == 0):
                self.mark_grid(len(self.grid) - 1, i, LaneType.UpToLeft)
            else:
                self.mark_grid(len(self.grid) - 1, i, LaneType.Up)

    def num_free_park_spaces(self, x, y):
        count = 0
        for i in range(x - (self.building_size + 1)//2 - 1, x + (self.building_size + 1)//2 + 1):
            for j in range(y - (self.building_size + 1)//2 - 1, y + (self.building_size + 1)//2 + 1):
                if(self[i, j] == LaneType.FreePark):
                    count += 1
        return count
