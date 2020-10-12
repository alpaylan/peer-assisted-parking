from time import sleep
from os import system
from sys import argv
import curses
import traceback

from Car import Car
from City import City, CityType
from Position import Position
from Simulation import CitySimulation

if __name__ == "__main__":
        
    sim = CitySimulation(
        building_size = 3,
        building_number = 4,
        number_of_cars = 0,
        car_notification_on = False,
        car_notification_range = 4,
        c_type = CityType.Bordered
    )
    i = 0
    try:
        stdscr = curses.initscr()   # initialize curses screen
        curses.noecho()             # turn off auto echoing of keypress on to screen
        curses.cbreak()             # enter break mode where pressing Enter key
                                    # after keystroke is not required for it to register
        stdscr.keypad(1)            # enable special Key values such as curses.KEY_LEFT etc
        stdscr.border(0)
        stdscr.addstr(6, stdscr.getmaxyx()[1]//2 - 18, 'Welcome to Keles City Simulation', curses.A_BOLD)

        # stdscr.notimeout(False)
        ch = stdscr.getch()
        # stdscr.notimeout(True)
        while True:
            stdscr.timeout(400)
            ch = stdscr.getch()
            if ch == ord('q'):
                break
            if ch == ord('a'):
                sim.add_car(Position(13, 0), Position(11, 18))
                sim.activate_cars()

            stdscr.clear()
            stdscr.addstr(0, 15, "Epoch" + str(i), curses.A_BOLD)
            stdscr.addstr(1, 0, str(sim.print_city()), curses.A_BOLD)

            sim.advance()
            i += 1            

    except:
        traceback.print_exc()     # print trace back log of the error
        

    finally:
        # --- Cleanup on exit ---
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()