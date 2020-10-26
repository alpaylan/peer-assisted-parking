# -*- coding: utf-8 -*-
from typing import List
from random import randint, seed

from City import City
from Car import Car, IdleCar, ParkedCar
from Position import Position, Direction


class CitySimulation:
    def __init__(self, **kwargs):
        self.city = City(
            kwargs["building_size"], kwargs["building_number"], kwargs["c_type"]
        )
        self.car_num = kwargs["number_of_cars"]
        self.cars: List[Car] = []
        self.car_notification_on = kwargs["car_notification_on"]
        self.CAR_NOTIFICATION_RANGE = kwargs["car_notification_range"]
        self.RANDOM_SEED = kwargs["random_seed"]
        seed(self.RANDOM_SEED)

    def advance(self) -> None:
        self.calculate()

    def print(self, p_type="city") -> None:
        if p_type == "city":
            self.print_city()
        elif p_type == "cars":
            self.print_cars()
        else:
            self.print_city()

    def activate_cars(self) -> None:
        for c in self.cars:
            c.move()

    def activate_car(self, carId) -> None:
        car = self.find_car_with_id(carId)
        if car == None:
            print("Car with carID: {} not found. Exiting.", carId)
            exit(0)
        car.move()

    def deactivate_car(self, carId) -> None:
        car = self.find_car_with_id(carId)
        if car == None:
            print("Car with carID: {} not found. Exiting.", carId)
            exit(0)

    def add_car(self, start: Position, target: Position) -> int:
        carId = len(self.cars)
        c = Car(carId, start, target, self.city)
        self.cars.append(c)
        return carId

    def add_random_car(self):
        border = randint(0, 3)
        pos = randint(0, len(self.city.grid) - 1)
        target_building = randint(0, len(self.city.building_positions) - 1)
        t_pos = Position(
            self.city.building_positions[target_building][0],
            self.city.building_positions[target_building][1],
        )
        if border == 0:
            return self.add_car(Position(pos, 0), t_pos)
        elif border == 1:
            return self.add_car(Position(0, pos), t_pos)
        elif border == 2:
            return self.add_car(Position(pos, len(self.city.grid) - 1), t_pos)
        elif border == 3:
            return self.add_car(Position(len(self.city.grid) - 1, pos), t_pos)

        return self.add_car(0, 0)

    def find_car_with_id(self, carID) -> Car:
        return self.cars[carID]

    def calculate(self) -> None:
        next_positions = set()
        for car in self.cars:
            if car.state == IdleCar or car.state == ParkedCar:
                continue
            c_pos = set()
            c_pos.add(car.calculate())
            if c_pos.issubset(next_positions) == False:
                next_positions = next_positions.union(c_pos)
                car.advance()
            else:
                car.waited_epochs += 1

        if self.car_notification_on:
            car.free_park_spaces = car.check_free_parking_spaces()
            self.notify_neighbor_cars(car)

    def notify_neighbor_cars(self, car) -> None:
        for c in self.cars:
            if car.position.euclid(c.position) < self.CAR_NOTIFICATION_RANGE:
                car.notify(c)
        pass

    def print_city(self) -> str:
        car_position_list = []

        for car in self.cars:
            car_position_list.append(car.position)

        return self.city.print_city_with_cars(car_position_list)

    def print_cars(self) -> str:
        car_str = ""
        for car in self.cars:
            car_str += str(car) + "\n"
        return car_str
