# Car-Seat-Alarm-uC-OS

As of September 2019, 838 children under the age of fifteen have died from Pediatric Vehicular Heatstroke (PHV) since 1998. 
In 2018, there were 53 deaths attributed to PHV which is the most ever recorded in a single year [1]. If children are our future, 
then we need to stop losing them to preventable deaths and that's why we are working on the µC/OS Car Seat Alarm or CSA.
The objective of the µC/OS Car Seat Alarm project is to build software that will notify drivers if they leave a child in the car 
seat after exiting the vehicle. 
This project is a proof of concept project.

The UC_Controller.py program is the microcontroller program. It is signaled that the vehicle it is housed in has been turned off. Upon
receiving this signal the microcontroller uses socket programming to connect to the server.py program that is a simulated car seat that we
ran on a Raspberry Pi Mini Zero W. Its only function is to return a true or false value to indicate that the car seat is occupied (True)
or unoccupied (False). If a false value is returned then the system shuts down because the car seat is unoccupied. If this initial value
is true then the microcontroller has a time that counts down and stops after about 30 seconds. The microcontroller then connects with the
server again and if a value of true is returned then the simulated horn is triggered and the the timmer again counts down from 30 upon its
expiration the horn will terminate. If this project is to be taken to its completion the car seat would either sense if object in the car
seat is within a specific weight range or if the car seats buckle is still latched. 
