from __future__ import annotations
from enum import Enum

from Position import Position, Direction
from City import City
from LaneType import LaneType

class IdleCar:
    @classmethod
    def advance(cls, car: Car):
        pass

class ParkedCar:
    @classmethod    
    def advance(cls, car: Car):
        pass

class ParkingCar:    
    @classmethod
    def advance(cls, car: Car):
        pass

class MovingCar:
    @classmethod
    def advance(cls, car: Car):
        car.position = cls.calculate_next_position(car)
    
    @classmethod
    def calculate_next_position(cls, car):
        relative_position = cls.calculate_relative_position(car)
        lane_type = car.city.lane_type_of_position(car.position)
        direction = cls.calculate_direction(car, relative_position, lane_type)
        return car.position + direction

    @classmethod
    def calculate_relative_position(cls, car):
        relative_position = Position(0, 0)

        if(car.position.x > car.target.x):
            relative_position.x = -1
        elif(car.position.x < car.target.x):
            relative_position.x = 1

        if(car.position.y > car.target.y):
            relative_position.y = -1
        elif(car.position.y < car.target.y):
            relative_position.y = 1

        return relative_position

    @classmethod
    def calculate_direction(cls, car: Car, relative_position: Position, lane_type: LaneType):
        if(lane_type == LaneType.East):
            return Direction(1, 0)
        elif(lane_type == LaneType.West):
            return Direction(-1, 0)
        elif(lane_type == LaneType.North):
            return Direction(0, -1)
        elif(lane_type == LaneType.South):
            return Direction(0, 1)
        elif(lane_type == LaneType.CrossRoad):
            return cls.calculate_direction_at_x(car, relative_position)
        else:
            return Direction(0, 0)

    @classmethod
    def calculate_direction_at_x(cls, car: Car, relative_position: Position):
        # There are 4 cases
        if(relative_position == Position(0, 0)):
            return Direction(0, 0)

        # Upper Right X
        elif(car.city[car.position.x - 1, car.position.y] == LaneType.CrossRoad
            and car.city[car.position.x, car.position.y + 1] == LaneType.CrossRoad):
            if(relative_position.y == -1):              # Go Up
                return Direction(0, -1)
            elif(relative_position.x == -1):            # Go Left
                return Direction(-1, 0)
            else:                                       # Go Below
                return Direction(0, 1)
        # Upper Left X
        elif(car.city[car.position.x + 1, car.position.y] == LaneType.CrossRoad
            and car.city[car.position.x, car.position.y + 1] == LaneType.CrossRoad):
            if(relative_position.x == -1):              # Go Left
                return Direction(-1, 0)
            elif(relative_position.y == 1):             # Go Below
                return Direction(0, 1)
            else:                                       # Go Right
                return Direction(1, 0)
        # Lower Left X
        elif(car.city[car.position.x + 1, car.position.y] == LaneType.CrossRoad
            and car.city[car.position.x, car.position.y - 1] == LaneType.CrossRoad):
            if(relative_position.y == 1):               # Go Below
                return Direction(0, 1)
            elif(relative_position.x == 1):             # Go Right
                return Direction(1, 0)
            else:                                       # Go Up
                return Direction(0, -1)
        # Lower Right X
        elif(car.city[car.position.x - 1, car.position.y] == LaneType.CrossRoad
            and car.city[car.position.x, car.position.y - 1] == LaneType.CrossRoad):
            if(relative_position.x == 1):               # Go Right
                return Direction(1, 0)
            elif(relative_position.y == -1):            # Go Up
                return Direction(0, -1)
            else:                                       # Go Left
                return Direction(-1, 0)

class CirclingCar:
    @classmethod
    def advance(cls, car: Car):
        car.position = cls.calculate_next_position(car)

    @classmethod
    def calculate_next_position(cls, car: Car):
        relative_position = cls.calculate_relative_position(car)
        lane_type = car.city.lane_type_of_position(car.position)
        direction = cls.calculate_direction(car, relative_position, lane_type)
        return car.position + direction

    @classmethod
    def calculate_relative_position(cls, car: Car):
        relative_position = Position(0, 0)

        if(car.position.x > car.target.x):
            relative_position.x = -1
        elif(car.position.x < car.target.x):
            relative_position.x = 1

        if(car.position.y > car.target.y):
            relative_position.y = -1
        elif(car.position.y < car.target.y):
            relative_position.y = 1

        return relative_position

    @classmethod
    def calculate_direction(cls, car: Car, relative_position, lane_type):
        if(lane_type == LaneType.East):
            return Direction(1, 0)
        elif(lane_type == LaneType.West):
            return Direction(-1, 0)
        elif(lane_type == LaneType.North):
            return Direction(0, -1)
        elif(lane_type == LaneType.South):
            return Direction(0, 1)
        elif(lane_type == LaneType.CrossRoad):
            return cls.calculate_direction_at_x(car, relative_position)
        else:
            return Direction(0, 0)

    @classmethod
    def calculate_direction_at_x(cls, car, relative_position):
        # Upper Right X
        if(car.city[car.position.x - 1, car.position.y] == LaneType.CrossRoad
            and car.city[car.position.x, car.position.y + 1] == LaneType.CrossRoad):
                return Direction(0, -1)
        # Upper Left X
        elif(car.city[car.position.x + 1, car.position.y] == LaneType.CrossRoad
            and car.city[car.position.x, car.position.y + 1] == LaneType.CrossRoad):
                return Direction(-1, 0)
        # Lower Left X
        elif(car.city[car.position.x + 1, car.position.y] == LaneType.CrossRoad
            and car.city[car.position.x, car.position.y - 1] == LaneType.CrossRoad):
                return Direction(0, 1)
        # Lower Right X
        elif(car.city[car.position.x - 1, car.position.y] == LaneType.CrossRoad
            and car.city[car.position.x, car.position.y - 1] == LaneType.CrossRoad):
                return Direction(1, 0)

class Car:
    def __init__(self, carId: int, position: Position, target: Position, city: City):
        self.carId = carId
        self.position = position
        self.target = target
        self.city = city
        self.state = IdleCar

    def __str__(self):
        return "("+str(self.carId) + ","+ str(self.position) + "," + str(self.target) + "," + str(self.state) + ")"

    def advance(self):
        self.state.advance(self)

    def move(self):
        self.state = MovingCar
    
    def park(self):
        self.state = ParkingCar
    
    def stop(self):
        self.state = IdleCar
