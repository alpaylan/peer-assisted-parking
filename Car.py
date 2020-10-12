from __future__ import annotations
from enum import Enum

from Position import Position, Direction
from City import City
from LaneType import LaneType

class IdleCar:
    @classmethod
    def advance(cls, car: Car):
        pass
    
    @classmethod
    def calculate(cls, car: Car) -> Position:
        return car.position
    
class ParkedCar:
    @classmethod    
    def advance(cls, car: Car):
        pass

    @classmethod
    def calculate(cls, car: Car) -> Position:
        return car.position

class ParkingCar:    
    @classmethod
    def advance(cls, car: Car):
        if(cls.check_sides(car) == True):
            cls.park(car, cls.park_position(car))
            
        else:
            car.state = CirclingCar
            car.advance()
            car.state = ParkingCar
        
    @classmethod
    def calculate(cls, car: Car) -> Position:
        if(cls.check_sides(car) == True):
            return cls.park_position(car)        
        else:
            car.state = CirclingCar
            calculated_position = car.calculate()
            car.state = ParkingCar
            return calculated_position
        
    @classmethod
    def check_sides(cls, car):
        if(car.city.lane_type_of_position(car.position) == LaneType.Right):
            return (car.city[car.position.x, car.position.y + 1] == LaneType.FreePark)
        elif(car.city.lane_type_of_position(car.position) == LaneType.Left):
            return (car.city[car.position.x, car.position.y - 1] == LaneType.FreePark)
        elif(car.city.lane_type_of_position(car.position) == LaneType.Up):
            return (car.city[car.position.x + 1, car.position.y] == LaneType.FreePark)
        elif(car.city.lane_type_of_position(car.position) == LaneType.Down):
            return (car.city[car.position.x - 1, car.position.y] == LaneType.FreePark)
        else:
            return False

    @classmethod
    def park_position(cls, car):
        if(car.city.lane_type_of_position(car.position) == LaneType.Right):
            return Position(car.position.x, car.position.y + 1)
        elif(car.city.lane_type_of_position(car.position) == LaneType.Left):
            return Position(car.position.x, car.position.y - 1)
        elif(car.city.lane_type_of_position(car.position) == LaneType.Up):
            return Position(car.position.x + 1, car.position.y)
        elif(car.city.lane_type_of_position(car.position) == LaneType.Down):
            return Position(car.position.x - 1, car.position.y)
        else:
            raise Exception

    @classmethod
    def park(cls, car, park_position):
        car.position = park_position
        car.state = ParkedCar
        car.city[car.position.x, car.position.y] = LaneType.FullPark

class MovingCar:
    @classmethod
    def advance(cls, car: Car):
        car.position = cls.calculate_next_position(car)
    
    @classmethod
    def calculate(cls, car: Car) -> Position:
        return cls.calculate_next_position(car)
    
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
        if(lane_type == LaneType.Right):
            return Direction(1, 0)
        elif(lane_type == LaneType.Left):
            return Direction(-1, 0)
        elif(lane_type == LaneType.Up):
            return Direction(0, -1)
        elif(lane_type == LaneType.Down):
            return Direction(0, 1)
        else:
            return cls.calculate_direction_relatively(car, relative_position, lane_type)

    @classmethod
    def calculate_direction_relatively(cls, car: Car, relative_position: Position, lane_type: LaneType):
        if(lane_type == LaneType.RightToDown):
            """ Move Right or Down"""
            if(relative_position.x == 1):
                return Direction(1, 0)
            return Direction(0, 1)
        if(lane_type == LaneType.DownToRight):
            """ Move Right"""
            return Direction(1, 0)
        if(lane_type == LaneType.LeftToDown):
            """ Move Down"""
            return Direction(0, 1)
        if(lane_type == LaneType.DownToLeft):
            """ Move Down or Left"""
            if(relative_position.y == 1):
                return Direction(0, 1)
            return Direction(-1, 0)
        if(lane_type == LaneType.RightToUp):
            """ Move Up"""
            return Direction(0, -1)
        if(lane_type == LaneType.UpToRight):
            """ Move Up or Right"""
            if(relative_position.y == -1):
                return Direction(0, -1)
            return Direction(1, 0)
        if(lane_type == LaneType.LeftToUp):
            """ Move Left or Up"""
            if(relative_position.x == -1):
                return Direction(-1, 0)
            return Direction(0, -1)
        if(lane_type == LaneType.UpToLeft):
            """ Move Left"""
            return Direction(-1, 0)
        return Direction(0, 0)
class CirclingCar:
    @classmethod
    def advance(cls, car: Car):
        car.position = cls.calculate_next_position(car)

    @classmethod
    def calculate(cls, car: Car) -> Position:
        return cls.calculate_next_position(car)
    
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
        if(lane_type == LaneType.Right):
            return Direction(1, 0)
        elif(lane_type == LaneType.Left):
            return Direction(-1, 0)
        elif(lane_type == LaneType.Up):
            return Direction(0, -1)
        elif(lane_type == LaneType.Down):
            return Direction(0, 1)
        else:
            return cls.calculate_direction_relatively(car, relative_position, lane_type)

    @classmethod
    def calculate_direction_relatively(cls, car, relative_position, lane_type):
        if(lane_type == LaneType.RightToDown):
            """ Move Down"""
            return Direction(0, 1)
        if(lane_type == LaneType.DownToRight):
            """ Move Right"""
            return Direction(1, 0)
        if(lane_type == LaneType.LeftToDown):
            """ Move Down"""
            return Direction(0, 1)
        if(lane_type == LaneType.DownToLeft):
            """ Move Left"""
            return Direction(-1, 0)
        if(lane_type == LaneType.RightToUp):
            """ Move Up"""
            return Direction(0, -1)
        if(lane_type == LaneType.UpToRight):
            """ Move Right"""
            return Direction(1, 0)
        if(lane_type == LaneType.LeftToUp):
            """ Move Up"""
            return Direction(0, -1)
        if(lane_type == LaneType.UpToLeft):
            """ Move Left"""
            return Direction(-1, 0)
        return Direction(0, 0)
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
        if(self.position.manhattan(self.target) < 8):
            self.park()

    def calculate(self):
        return self.state.calculate(self)

    def move(self):
        self.state = MovingCar
    
    def park(self):
        if(self.state == ParkedCar or self.state == IdleCar):
            pass
        self.state = ParkingCar
    
    def stop(self):
        self.state = IdleCar
