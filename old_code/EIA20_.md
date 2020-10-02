#  Ericson EIA20 Idea Overview
  
  
Peer Assisted Parking(PAP) is an Advance Driver Assistance System that uses a mesh network of vehicles for Parking Assistance. Radar Sensors, Lidar Sensors and Cameras are used for detection of free parking spaces and V2V-V2I communications allows diffusion of the information.
  
##  Business Side
  
  
###  Problem
  
  
The problem, as stated in "Cruising for Parking" by Urban Planning Researcher Donald Shoup, is that roughly 30% of all traffic in metropolitan areas consists of drivers circling around blocks for free parking spaces. This has several affects such as,
  
- Waste of fuels, which means both monetary and more importantly climatic waste.
- Waste of time as people either get late to their businesses or sleep less to come in time
- Increase in the general stress level of drivers  
  
###  Solution
  
  
A system where drivers are notified of free parking spaces in streets.
  
###  Unique Value Proposition
  
  
Traffic is reduced, benefiting drivers and also helping the world in its fight against climate change and use of fossil fuels.
  
###  Target Audience
  
  
Vehicle Manufacturers.
  
##  Technical Side
  
  
The project can be examined in 2 parts, park space detection and information diffusion.
  
###  Park Space Detection
  
  
Park Space Detection depends on processing of sensor data. For the prototype and the actual project, different kinds of sensors are going to be used.
  
####  Prototype
  
  
In the prototype, HCSR-4 sonar sensors are going to be used. Free parking spaces will be further than cars in parked state, this will allow the detection free spots.
  
####  Actual Project
  
  
For autonomous vehicle applications Radar, Lidar and Camera data is going to be fused for an understanding of the 3D World around the car for driver assistance. This fused sensor data is going to be used for PAP to determine nearby parking spaces.
  
###  Information Diffusion
  
  
Each car will generate an information packet containing free parking spaces. One possibility is that also non-free areas can be distributed to notify drivers. This diffusion is going to be using a non-hierachical mesh network structure. The algorithms to be used for diffusion is not yet determined.
  
####  Prototype
  
  
For the prototype, basic wireless network structures can be used for testing of the diffusion system.
  
####  Actual Project
  
  
In the actual project, V2V, V2I, C-ITS, 802.11p communication systems will be used for the diffusion.
  
###  Simulation
  
  
I believe a simulation of the project is a software defined environment might be helpful for design of information diffusion algortihms.
  