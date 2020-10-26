from __future__ import annotations
from enum import Enum

from Position import Position, Direction
from City import City
from LaneType import LaneType, Masks

import Logger

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
        if((car.city.lane_type_of_position(car.position) == LaneType.Right)
            and (car.city.is_inside(car.position.x, car.position.y + 1))):
            return (car.city[car.position.x, car.position.y + 1] == LaneType.FreePark)
        elif((car.city.lane_type_of_position(car.position) == LaneType.Left)
            and (car.city.is_inside(car.position.x, car.position.y - 1))):
            return (car.city[car.position.x, car.position.y - 1] == LaneType.FreePark)
        elif((car.city.lane_type_of_position(car.position) == LaneType.Up)
            and (car.city.is_inside(car.position.x + 1, car.position.y))):
            return (car.city[car.position.x + 1, car.position.y] == LaneType.FreePark)
        elif((car.city.lane_type_of_position(car.position) == LaneType.Down)
            and (car.city.is_inside(car.position.x - 1, car.position.y))):
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
        Logger.logCritical("park")

        car.position = park_position
        Logger.logCritical("Before:" + str(car.state))
        Logger.logCritical("\n")
        car.state = ParkedCar
        Logger.logCritical("After:" + str(car.state))
        Logger.logCritical("\n")
        car.city[car.position.x, car.position.y] = LaneType.FullPark
        Logger.logCritical(str(car.position))

class MovingCar:
    @classmethod
    def advance(cls, car: Car):
        car.position = cls.calculate_next_position(car)

    @classmethod
    def calculate(cls, car: Car) -> Position:
        return cls.calculate_next_position(car)

    @classmethod
    def calculate_next_position(cls, car):
        relative_position = car.calculate_relative_position(car)
        lane_type = car.city.lane_type_of_position(car.position)
        direction = cls.calculate_direction(car, relative_position, lane_type)
        return car.position + direction

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
            return cls.relative_direction(car, relative_position, lane_type)

    @classmethod
    def relative_direction(cls, car: Car, relative_position: Position, lane_type: LaneType):
        if(lane_type == LaneType.RightToDown):
            """ Move Right or Down """
            if(relative_position.x == 1):
                return Direction(1, 0)
            return Direction(0, 1)
        if(lane_type == LaneType.DownToRight):
            """ Move Right """
            return Direction(1, 0)
        if(lane_type == LaneType.LeftToDown):
            """ Move Down """
            return Direction(0, 1)
        if(lane_type == LaneType.DownToLeft):
            """ Move Down or Left """
            if(relative_position.y == 1):
                return Direction(0, 1)
            return Direction(-1, 0)
        if(lane_type == LaneType.RightToUp):
            """ Move Up """
            return Direction(0, -1)
        if(lane_type == LaneType.UpToRight):
            """ Move Up or Right """
            if(relative_position.y == -1):
                return Direction(0, -1)
            return Direction(1, 0)
        if(lane_type == LaneType.LeftToUp):
            """ Move Left or Up """
            if(relative_position.x == -1):
                return Direction(-1, 0)
            return Direction(0, -1)
        if(lane_type == LaneType.UpToLeft):
            """ Move Left """
            return Direction(-1, 0)
        return Direction(0, 0)

class CirclingCar:
    @classmethod
    def advance(cls, car: Car):
        car.position = cls.calculate_next_position(car, "adv")
        car.circling_time += 1
    @classmethod
    def calculate(cls, car: Car) -> Position:
        return cls.calculate_next_position(car, "calc")

    @classmethod
    def calculate_next_position(cls, car: Car, type):
        lane_type = car.city.lane_type_of_position(car.position)
        """ todo@alpkeles: 20 is a magic number, change it """
        """ supposed to stop infinite loop around the block """
        if(car.circling_time >= 20 and ((lane_type.value & Masks.TW_ROAD_MASK) != 0)):
            direction = cls.forward_direction(car, lane_type)
            """ todo@alpkeles: Tricky hack, get rid of it!! """
            """ supposed to help with the infinite loop hack  """
            if(type == "adv"):
                car.circling_time = 0
        else:
            direction = cls.calculate_direction(car, lane_type)
        return car.position + direction

    @classmethod
    def calculate_direction(cls, car: Car, lane_type):
        if(lane_type == LaneType.Right):
            return Direction(1, 0)
        elif(lane_type == LaneType.Left):
            return Direction(-1, 0)
        elif(lane_type == LaneType.Up):
            return Direction(0, -1)
        elif(lane_type == LaneType.Down):
            return Direction(0, 1)
        else:
            return cls.turning_direction(car, lane_type)

    @classmethod
    def turning_direction(cls, car, lane_type):
        if((lane_type == LaneType.RightToDown)
            or (lane_type == LaneType.LeftToDown)):
            """ Move Down """
            return Direction(0, 1)
        if((lane_type == LaneType.DownToLeft)
            or (lane_type == LaneType.UpToLeft)):
            """ Move Left """
            return Direction(-1, 0)
        if((lane_type == LaneType.DownToRight)
            or (lane_type == LaneType.UpToRight)):
            """ Move Right """
            return Direction(1, 0)
        if((lane_type == LaneType.RightToUp)
            or (lane_type == LaneType.LeftToUp)):
            """ Move Up """
            return Direction(0, -1)

        return Direction(0, 0)

    @classmethod
    def forward_direction(cls, car, lane_type):
        """
        There are 2 cases, either position is at the border
        or the positions is at the center. If border, there
        exists no choice but turn, but at center, the vehicle
        goes forward. First 4 cases are border, last 4 are center.
        """
        # Border
        if(lane_type == LaneType.DownToRight):
            """ Move Right """
            return Direction(1, 0)
        if(lane_type == LaneType.RightToUp):
            """ Move Up """
            return Direction(0, -1)
        if(lane_type == LaneType.UpToLeft):
            """ Move Left """
            return Direction(-1, 0)
        if(lane_type == LaneType.LeftToDown):
            """ Move Down """
            return Direction(0, 1)

        # Center
        if(lane_type == LaneType.RightToDown):
            """ Move Down """
            return Direction(1, 0)
        if(lane_type == LaneType.DownToLeft):
            """ Move Left """
            return Direction(0, 1)
        if(lane_type == LaneType.LeftToUp):
            """ Move Up """
            return Direction(-1, 0)
        if(lane_type == LaneType.UpToRight):
            """ Move Right """
            return Direction(0, -1)

        return Direction(0, 0)


class Car:
    def __init__(self, carId: int, position: Position, target: Position, city: City):
        self.carId = carId
        self.position = position
        self.target = target
        self.city = city
        self.state = IdleCar
        self.free_park_spaces = []
        self.circling_time = 0
    def __str__(self):
        return "("+str(self.carId) + ","+ str(self.position) + "," + str(self.target) + "," + str(self.state) + ")"

    def advance(self):
        self.state.advance(self)
        """ 8 is magic, fix it!! """
        if(self.position.manhattan(self.target) < 8):
            self.park()

    def calculate(self):
        return self.state.calculate(self)

    def move(self):
        self.state = MovingCar

    def park(self):
        if(self.state == ParkedCar or self.state == IdleCar):
            return
        self.state = ParkingCar

    def stop(self):
        self.state = IdleCar

    def notify(self, other):
        other.free_park_spaces.append(self.free_park_spaces.copy())

    def check_free_parking_spaces(self):
        fps = []
        for i in range(self.position.x - 3, self.position.x + 3):
            for j in range(self.position.y - 3, self.position.y + 3):
                if(self.city[i, j] == LaneType.FreePark):
                    fps.append(Position(i, j))
        return fps

    def calculate_relative_position(self, car):
        """
               0,-1
                |
        -1,-1   |   1, -1
                |
     -1,0 ------c------ 1, 0
                |
        -1, 1   |   1, 1
                |
               0,1
        """

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
