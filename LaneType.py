from enum import Enum
class LaneType(Enum):
    # Roads
    # One-Way Roads
    Right = 0
    Up = 1
    Left = 2
    Down = 3
    # Two-Way Roads
    RightToUp = 5
    RightToDown = 100

    LeftToUp = 101
    LeftToDown = 8
    
    UpToLeft = 7
    UpToRight = 102
    
    DownToLeft = 103
    DownToRight = 6
    

    
    # Closed Loops
    InnerLoop = 14
    OuterLoop = 15
    # Three-Way Roads
    LeftUpDown = 16
    RightUpDown = 17
    UpRightLeft = 18
    DownRightLeft = 19
    # Four-Way Road
    FourWayRoad = 9
    # Fixed Structures
    FreePark = 10
    FullPark = 11
    Building = 12
    TrafficLight = 13

    def __str__(self):
        # Right 
        if(self.value == self.Right.value):
            return u"\u2b62"
        # Up 
        elif(self.value == self.Up.value):
            return u"\u2b61"
        # Left 
        elif(self.value == self.Left.value):
            return u"\u2b60"
        # Down 
        elif(self.value == self.Down.value):
            return u"\u2b63"
        # Park 
        elif(self.value == self.FreePark.value):
            return "p"
        # Building 
        elif(self.value == self.Building.value):
            return u"\u2592"
        # TrafficLight 
        elif(self.value == self.TrafficLight.value):
            return "!"
        # Parked
        elif(self.value == self.FullPark.value):
            return "f"
        # InnerLoop
        elif(self.value == self.InnerLoop.value):
            return u"\u21ba"
        # OuterLoop
        elif(self.value == self.OuterLoop.value):
            return u"\u21bb"

        elif(self.value == self.RightToUp.value):
            return u"\u2ba5"
        elif(self.value == self.RightToDown.value):
            return u"\u2ba7"

        elif(self.value == self.LeftToUp.value):
            return u"\u2ba4"
        elif(self.value == self.LeftToDown.value):
            return u"\u2ba6"

        elif(self.value == self.UpToRight.value):
            return u"\u2ba3"
        elif(self.value == self.DownToRight.value):
            return u"\u2ba1"

        elif(self.value == self.UpToLeft.value):
            return u"\u2ba2"
        elif(self.value == self.DownToLeft.value):
            return u"\u2ba0"



        elif(self.value == self.LeftUpDown.value):
            return u"\u2ba5"
        elif(self.value == self.RightUpDown.value):
            return "x"
        elif(self.value == self.UpRightLeft.value):
            return "x"
        elif(self.value == self.DownRightLeft.value):
            return "x"
        elif(self.value == self.FourWayRoad.value):
            return "x"
        # None
        else:
            return "?"
