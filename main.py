# -*- coding: utf-8 -*-
from sys import argv
import curses
from curses import wrapper

from City import CityType
from Simulation import CitySimulation

import Logger

RANDOM_SEED = None

if len(argv) >= 3:
    b_s = int(argv[1])
    b_n = int(argv[2])
else:
    b_s = 3
    b_n = 3

if len(argv) == 4:
    RANDOM_SEED = int(argv[3])


def cursesGreet(stdscr):

    stdscr.border(0)

    stdscr.refresh()

    stdscr.addstr(
        6,
        stdscr.getmaxyx()[1] // 2 - 18,
        "Welcome to Keles City Simulation",
        curses.A_BOLD,
    )

    _ = stdscr.getch()


def cursesPrint(stdscr, sim, epoch):
    stdscr.clear()

    stdscr.addstr(1, stdscr.getmaxyx()[1] // 2 - 3, "Epoch" + str(epoch), curses.A_BOLD)

    lines = str(sim.print_city()).split("\n")

    for i in range(len(lines)):
        stdscr.addstr(
            i + 5,
            stdscr.getmaxyx()[1] // 2 - len(lines[i]) // 2,
            lines[i],
            curses.A_BOLD,
        )


def main(stdscr):

    Logger.startLog()

    sim = CitySimulation(
        building_size=b_s,
        building_number=b_n,
        number_of_cars=0,
        car_notification_on=False,
        car_notification_range=4,
        c_type=CityType.Bordered,
        random_seed=RANDOM_SEED,
    )

    use_curses = True

    if use_curses:
        cursesGreet(stdscr)
    else:
        curses.endwin()

    epoch = 0
    while True:
        stdscr.timeout(400)

        ch = stdscr.getch()

        if ch == ord("q"):
            break

        if ch == ord("a"):
            carId = sim.add_random_car()
            sim.activate_car(carId)

        if ord("1") <= ch and ch <= ord("9"):
            for _ in range(ch - 48):
                _ = sim.add_random_car()
            sim.activate_cars()

        if use_curses:
            cursesPrint(stdscr, sim, epoch)

        sim.advance()

        epoch += 1

    for car in sim.cars:
        if car.waited_epochs != 0:
            Logger.logResult(str(car.carId) + ":" + str(car.waited_epochs))
            Logger.logResult("\n")


if __name__ == "__main__":
    wrapper(main)
