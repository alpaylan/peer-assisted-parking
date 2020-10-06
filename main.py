from time import sleep
from os import system
from Car import Car, IdleCar
from City import City
from Position import Position, Direction
from Simulation import CitySimulation
if __name__ == "__main__":
        
    sim = CitySimulation(
        building_size = 4,
        building_number = 4,
        number_of_cars = 0,
        car_notification_on = False,
        car_notification_range = 4,
    )

    sim.add_car(Position(5, 0), Position(5, 26))
    sim.add_car(Position(6, 26), Position(6, 0))
    sim.add_car(Position(13, 0), Position(13, 26))
    sim.add_car(Position(14, 26), Position(14, 0))
    
    sim.activate_cars()

    while True:
        system("clear")
        sim.advance()
        sleep(1)
        
