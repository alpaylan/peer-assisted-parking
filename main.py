from time import sleep, time, ctime
from os import system
from sys import argv
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

from Car import Car
from City import City, CityType
from Position import Position
from Simulation import CitySimulation

import Logger

if(len(argv) == 3):
    b_s = argv[1]
    b_n = argv[2]
else:
    b_s = 3
    b_n = 3

def main(stdscr):

    Logger.startLog()

    sim = CitySimulation(
        building_size = int(b_s),
        building_number = int(b_n),
        number_of_cars = 0,
        car_notification_on = False,
        car_notification_range = 4,
        c_type = CityType.Bordered
    )
    
    stdscr.border(0)

    stdscr.refresh()

    stdscr.addstr(6, stdscr.getmaxyx()[1]//2 - 18, 'Welcome to Keles City Simulation', curses.A_BOLD)

    ch = stdscr.getch()

    epoch = 0
    while True:
        stdscr.timeout(400)

        ch = stdscr.getch()

        stdscr.move(0, 95)

        if ch == ord('q'):
            break

        if ch == ord('a'):
            carId = sim.add_random_car()
            sim.activate_car(carId)

        if ord('1') <= ch and ch <= ord('9'):
            for _ in range(ch - 48):
                _ = sim.add_random_car()
            sim.activate_cars()

        stdscr.clear()

        stdscr.addstr(1, stdscr.getmaxyx()[1]//2 - 3, "Epoch" + str(epoch), curses.A_BOLD)

        lines = str(sim.print_city()).split("\n")

        for i in range(len(lines)):
            stdscr.addstr(i + 5, stdscr.getmaxyx()[1]//2 - len(lines[i])//2, lines[i], curses.A_BOLD)

        sim.advance()

        Logger.logPrintln("Epoch " + str(epoch))

        if(len(sim.cars) > 0):
            Logger.logPrintln(str(sim.cars[0]))

        epoch += 1            

if __name__ == "__main__":
    wrapper(main)
