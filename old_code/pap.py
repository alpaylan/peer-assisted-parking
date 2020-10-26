# -*- coding: utf-8 -*-
from grid import *
from position import *
from car import *
import copy
import os
import time

# Grid is created.
g = Grid(28, 28, 4)
g_show = copy.deepcopy(g)
c1 = Car(5, 0, 5, 1, g)
c2 = Car(6, 27, 5, 0, g)
c3 = Car(13, 0, 5, 27, g)
c4 = Car(14, 27, 5, 0, g)

car_list = [c1, c2, c3, c4]

for i in car_list:
    i.move()

while True:

    for i in car_list:
        g_show[i.pos.x, i.pos.y] = "c"
        print(i.pos, i.target)
        if i.pos == i.target:
            print("Target Reached")
            i.park()
    os.system("clear")
    print(g_show)
    time.sleep(1)

    for i in car_list:

        i.calculate()

        if i.next_out():
            print("Alarm")
            exit(0)

        g_show[i.pos.x, i.pos.y] = i.grid[i.pos.x, i.pos.y]

        i.advance()
