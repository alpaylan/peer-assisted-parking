from dataclasses import dataclass
from Position import Position, Direction
from City import City


@dataclass
class CarProperties:
    carId : int
    position : Position
    target: Position
    city: City

class CarState():
    def __init__(self, state):
        self.__class__ = state
    def switch(self, state):
        self.__class__ = state
    
    def advance(self):
        return NotImplementedError("")

    def move(self):
        return NotImplementedError("")
    
    def park(self):
        return NotImplementedError("")

    def stop(self):
        return NotImplementedError("")

class IdleCar(CarState):    
    def advance(self):
        pass

    def move(self):
        self.switch(MovingCar)
    
    def park(self):
        self.switch(ParkingCar)

    def stop(self):
        pass

class ParkedCar(CarState):
    def advance(self):
        pass

    def move(self):
        self.switch(MovingCar)
    
    def park(self):
        pass

    def stop(self):
        self.switch(IdleCar)

class ParkingCar(CarState):
    def advance(self):
        pass

    def move(self):
        self.switch(MovingCar)
    
    def park(self):
        pass

    def stop(self):
        self.switch(IdleCar)

class MovingCar(CarState):
    def advance(self):
        self.props.position = self.calculate_next_position()

    def move(self):
        pass
    
    def park(self):
        self.switch(ParkingCar)

    def stop(self):
        self.switch(IdleCar)

    def calculate_next_position(self):
        relative_position = self.calculate_relative_position()
        properties = self.props
        lane_type = properties.city.lane_type_of_position(properties.position)
        direction = self.calculate_direction(relative_position, lane_type)
        return self.props.position + direction

    def calculate_relative_position(self):
        relative_position = Position(0, 0)

        if(self.props.position.x > self.props.target.x):
            relative_position.x = -1
        elif(self.props.position.x < self.props.target.x):
            relative_position.x = 1

        if(self.props.position.y > self.props.target.y):
            relative_position.y = -1
        elif(self.props.position.y < self.props.target.y):
            relative_position.y = 1

        return relative_position

    def calculate_direction(self, relative_position: Position, lane_type: str):
        if(lane_type == ">"):
            return Direction(1, 0)
        elif(lane_type == "<"):
            return Direction(-1, 0)
        elif(lane_type == "^"):
            return Direction(0, -1)
        elif(lane_type == "v"):
            return Direction(0, 1)
        elif(lane_type == "x"):
            return self.calculate_direction_at_x(relative_position)
        else:
            return Direction(0, 0)

    def calculate_direction_at_x(self, relative_position: Position):
        properties = self.props

        # There are 4 cases
        if(relative_position == Position(0, 0)):
            return Direction(0, 0)

        # Upper Right X
        elif(properties.city[properties.position.x - 1, properties.position.y] == "x"
            and properties.city[properties.position.x, properties.position.y + 1] == "x"):
            if(relative_position.y == -1):              # Go Up
                return Direction(0, -1)
            elif(relative_position.x == -1):            # Go Left
                return Direction(-1, 0)
            else:                                       # Go Below
                return Direction(0, 1)
        # Upper Left X
        elif(properties.city[properties.position.x + 1, properties.position.y] == "x"
            and properties.city[properties.position.x, properties.position.y + 1] == "x"):
            if(relative_position.x == -1):              # Go Left
                return Direction(-1, 0)
            elif(relative_position.y == 1):             # Go Below
                return Direction(0, 1)
            else:                                       # Go Right
                return Direction(1, 0)
        # Lower Left X
        elif(properties.city[properties.position.x + 1, properties.position.y] == "x"
            and properties.city[properties.position.x, properties.position.y - 1] == "x"):
            if(relative_position.y == 1):               # Go Below
                return Direction(0, 1)
            elif(relative_position.x == 1):             # Go Right
                return Direction(1, 0)
            else:                                       # Go Up
                return Direction(0, -1)
        # Lower Right X
        elif(properties.city[properties.position.x - 1, properties.position.y] == "x"
            and properties.city[properties.position.x, properties.position.y - 1] == "x"):
            if(relative_position.x == 1):               # Go Right
                return Direction(1, 0)
            elif(relative_position.y == -1):            # Go Up
                return Direction(0, -1)
            else:                                       # Go Left
                return Direction(-1, 0)

        
        

class CirclingCar(CarState):
    def advance(self):
        self.props.position = self.calculate_next_position()

    def move(self):
        self.switch(MovingCar)
    
    def park(self):
        self.switch(ParkingCar)

    def calculate_next_position(self):
        relative_position = self.calculate_relative_position()
        properties = self.props
        lane_type = properties.city.lane_type_of_position(properties.position)
        direction = self.calculate_direction(relative_position, lane_type)
        return self.props.position + direction

    def calculate_relative_position(self):
        relative_position = Position(0, 0)

        if(self.props.position.x > self.props.target.x):
            relative_position.x = -1
        elif(self.props.position.x < self.props.target.x):
            relative_position.x = 1

        if(self.props.position.y > self.props.target.y):
            relative_position.y = -1
        elif(self.props.position.y < self.props.target.y):
            relative_position.y = 1

        return relative_position

    def calculate_direction(self, relative_position, lane_type):
        if(lane_type == ">"):
            return Direction(1, 0)
        elif(lane_type == "<"):
            return Direction(-1, 0)
        elif(lane_type == "^"):
            return Direction(0, -1)
        elif(lane_type == "v"):
            return Direction(0, 1)
        elif(lane_type == "x"):
            return self.calculate_direction_at_x(relative_position)
        else:
            return Direction(0, 0)

    def calculate_direction_at_x(self, relative_position):
        properties = self.props

        # Upper Right X
        if(properties.city[properties.position.x - 1, properties.position.y] == "x"
            and properties.city[properties.position.x, properties.position.y + 1] == "x"):
                return Direction(0, -1)
        # Upper Left X
        elif(properties.city[properties.position.x + 1, properties.position.y] == "x"
            and properties.city[properties.position.x, properties.position.y + 1] == "x"):
                return Direction(-1, 0)
        # Lower Left X
        elif(properties.city[properties.position.x + 1, properties.position.y] == "x"
            and properties.city[properties.position.x, properties.position.y - 1] == "x"):
                return Direction(0, 1)
        # Lower Right X
        elif(properties.city[properties.position.x - 1, properties.position.y] == "x"
            and properties.city[properties.position.x, properties.position.y - 1] == "x"):
                return Direction(1, 0)
            
        



class Car:
    def __init__(self, state: CarState, carId: int, position: Position, target: Position, city: City):
        self.state = CarState(state)
        self.state.props = CarProperties(carId, position, target, city)

    def __str__(self):
        return str(self.state.props) + "in state " + str(self.state.__class__)

    def advance(self):
        self.state.advance()

    def move(self):
        self.state.move()
    
    def park(self):
        self.state.park()
    
    def stop(self):
        self.state.stop()
