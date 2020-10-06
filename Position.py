from __future__ import annotations

class Position:
    def __init__(self, x:int = 0, y:int = 0) -> None:
        self.x = x
        self.y = y

    def __sub__(self, other) -> Position:
        return Position(self.x - other.x, self.y - other.y)

    def __add__(self, other:Position) -> Position:
        return Position(self.x + other.x, self.y + other.y)        

    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")" 

    def __getitem__(self, key:int) -> int:
        if(key == 0):
            return self.x
        elif(key == 1):
            return self.y
        else:
            return None

    def __eq__(self, other:Position) -> bool:
        return (self.x == other.x) and (self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def turn(self) -> Position:
        return Position(self.y, self.x)

Direction = Position

