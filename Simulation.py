from City import City
from Car import Car, IdleCar
from Position import Position, Direction
from typing import List
class CitySimulation:
    def __init__(self, **kwargs):
        self.city = City(kwargs["building_size"], kwargs["building_number"], kwargs["c_type"])
        self.car_num = kwargs["number_of_cars"]
        self.cars: List[Car] = []
        self.car_notification_on = kwargs["car_notification_on"]
        self.CAR_NOTIFICATION_RANGE = kwargs["car_notification_range"]
    def advance(self) -> None:
        self.calculate()

    def print(self, p_type = "city") -> None:
        if(p_type == "city"):
            self.print_city()
        elif(p_type == "cars"):
            self.print_cars()
        else:
            self.print_city()


    def activate_cars(self) -> None:
        for c in self.cars:
            c.move()

    def activate_car(self, carId) -> None:
        car = self.find_car_with_id(carId)
        if(car == None):
            print("Car with carID: {} not found. Exiting.", carId)
            exit(0)
        car.move()

    def deactivate_car(self, carId) -> None:
        car = self.find_car_with_id(carId)
        if(car == None):
            print("Car with carID: {} not found. Exiting.", carId)
            exit(0)
        car.stop()

    def add_car(self, start: Position, target: Position) -> None:
        carId = len(self.cars)
        c = Car(carId, start, target, self.city)
        self.cars.append(c)

    def find_car_with_id(self, carID) -> Car:
        for i in self.cars:
            if(i.state.props.carID == carID):
                return i
        return None

    def calculate(self) -> None:
        next_positions = set()

        for car in self.cars:
            c_pos = set()
            c_pos.add(car.calculate())
            if(c_pos.issubset(next_positions) == False):
                next_positions = next_positions.union(c_pos)
                car.advance()
            
        if(self.car_notification_on):
            free_park_spaces = car.notify()
            self.notify_neighbor_cars(car, free_park_spaces)

    def notify_neighbor_cars(self, car, free_park_spaces) -> None:

        pass

    def print_city(self) -> None:
        car_position_list = []

        for car in self.cars:
            car_position_list.append(car.position)

        return self.city.print_city_with_cars(car_position_list)
        
    def print_cars(self) -> None:

        for car in self.cars:
            print(car)


