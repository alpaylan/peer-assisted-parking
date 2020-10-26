# Peer Assisted Parking(PAP)

## About Project

PAP is a project designed for the Ericson Innovation Awards 2020.

PAP aims to lower the congestion levels and CO2 emissions originating from on-street parking problem.

In PAP, we create a mesh network of vehicles communicating each other through V2V and C-ITS communications to notify the network of free parking spots.

We believe that this optimisation has the potential to affect metropolitan area traffic congestions in great manner.

A rough roadmap of the project is given in eia20.md file.

## Working Demo

Currently, the code adds random cars with random building as targets and the cars move one unit each epoch.

City grid is given as a command line argument such that:

'''python main.py 4 3''' generates a city of 3x3 with buildings of size 4x4.

'''a''' command adds 1 car.

Number keys from 1 to 9 generate that amount of car when hit.

q, ctrl+c or ctrl+d command ends the simulation.

Before entering the command, please get a full sized bash window.

Project works in python versions >= 3.7
