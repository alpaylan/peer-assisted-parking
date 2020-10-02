class Position():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)
    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)        
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")" 
    def __getitem__(self, key):
        if(key == 0):
            return self.x
        elif(key == 1):
            return self.y
        else:
            return None
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
    def turn(self):
        return Position(self.y, self.x)



Direction = Position

