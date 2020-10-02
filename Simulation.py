from City import City
from Car import Car
from Position import Position, Direction

class CitySimulation:
    def __init__(self, **kwargs):
        self.city = City(kwargs["building_size"], kwargs["building_number"])
        self.car_num = kwargs["number_of_cars"]
        self.cars = []
        self.CAR_NOTIFICATION_RANGE = kwargs["car_notification_range"]

    def advance(self) -> None:
        self.calculation_phase()
        self.print_phase()

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

    def find_car_with_id(self, carID) -> Car:
        for i in self.cars:
            if(i.state.props.carID == carID):
                return i
        return None

    def calculation_phase(self) -> None:
        for car in self.cars:
            car.advance()
        free_park_spaces = car.notify()
        self.notify_neighbor_cars(car, free_park_spaces)

    def notify_neighbor_cars(self, car, free_park_spaces) -> None:

        pass

    def print_phase(self) -> None:
        car_position_list = []

        for car in self.cars:
            car_position_list.append(car.state.props.position)

        print(self.city.print_city_with_cars(car_position_list))
        

