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
    Parked = 8
    InnerLoop = 9
    OuterLoop = 10
    def __str__(self):
        # East 
        if(self.value == self.East.value):
            return ">"
        # North 
        elif(self.value == self.North.value):
            return "^"
        # West 
        elif(self.value == self.West.value):
            return "<"
        # South 
        elif(self.value == self.South.value):
            return "v"
        # CrossRoad 
        elif(self.value == self.CrossRoad.value):
            return "x"
        # Park 
        elif(self.value == self.Park.value):
            return "2"
        # Building 
        elif(self.value == self.Building.value):
            return "#"
        # TrafficLight 
        elif(self.value == self.TrafficLight.value):
            return "1"
        # Parked
        elif(self.value == self.Parked.value):
            return "p"
        # InnerLoop
        elif(self.value == self.InnerLoop.value):
            return "i"
        # OuterLoop
        elif(self.value == self.OuterLoop.value):
            return "o"
        # None
        else:
            return "?"
