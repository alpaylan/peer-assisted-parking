from enum import Enum
class LaneType(Enum):
    East = 0
    North = 1
    West = 2
    South = 3
    CrossRoad = 4
    Park = 5
    Building = 6
    TrafficLight = 7

    def __str__(self):
        # East 
        if(self.value == 0):
            return ">"
        # North 
        elif(self.value == 1):
            return "^"
        # West 
        elif(self.value == 2):
            return "<"
        # South 
        elif(self.value == 3):
            return "v"
        # CrossRoad 
        elif(self.value == 4):
            return "x"
        # Park 
        elif(self.value == 5):
            return "2"
        # Building 
        elif(self.value == 6):
            return "#"
        # TrafficLight 
        elif(self.value == 7):
            return "1"
        # None
        else:
            return "?"
