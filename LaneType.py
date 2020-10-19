from enum import Enum
from dataclasses import dataclass

class Masks:
    ROAD_MASK = 0x3f0
    BUILDING_MASK = 0x400
    OW_ROAD_MASK = 0x010
    BORDER_ROAD_MASK = 0x020
    TW_ROAD_MASK = 0x040

class LaneType(Enum):
    # Roads

    # One-Way Roads
    Right = 0x011
    Up = 0x012
    Left = 0x014
    Down = 0x018

    # Two-Way Roads

    # Border
    RightToUp = 0x021
    LeftToDown = 0x022
    UpToLeft = 0x024
    DownToRight = 0x028

    # Center
    RightToDown = 0x041
    LeftToUp = 0x042
    UpToRight = 0x044
    DownToLeft = 0x048
    
    # Three-Way Roads
    LeftUpDown = 0x081
    RightUpDown = 0x082
    UpRightLeft = 0x084
    DownRightLeft = 0x088

    # Four-Way Road
    FourWayRoad = 0x101

    # Closed Loops
    InnerLoop = 0x201
    OuterLoop = 0x202

    # Fixed Structures
    FreePark = 0x401
    FullPark = 0x402
    Building = 0x404
    TrafficLight = 0x408

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
