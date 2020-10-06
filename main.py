from time import sleep
from os import system
from sys import argv

from Car import Car
from City import City
from Position import Position
from Simulation import CitySimulation

if __name__ == "__main__":
        
    sim = CitySimulation(
        building_size = 4,
        building_number = 4,
        number_of_cars = 0,
        car_notification_on = False,
        car_notification_range = 4,
    )

    # sim.add_car(Position(13, 0), Position(11, 15))
    # sim.add_car(Position(0, 6), Position(26, 6))
    
    
    # for j in range(5):
    #     sim.add_car(Position(13, j), Position(11, 15))
    
    # sim.activate_cars()


    i = 0
    while True:
        system("clear")
        print("Epoch", i)
        
        # sim.print("cars")
        sim.print("")

        sim.advance()
        sleep(0.5)
        # input()
        if i < 17:
            sim.add_car(Position(13, 0), Position(11, 18))
            sim.activate_cars()
        i +=1
