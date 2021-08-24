#### High Level Diagrams:


App Architexture: https://drive.google.com/file/d/1RcUjOQA1PDD137VwBZKDlc1MvjlBsVaH/view?usp=sharing


#### GPIO Driver Module
The GPIO Driver Module: 

Writes the output of flow sensors with the current flow values in csv datetime stamps. Azure Event IoT will be used to read the output streams.

1. Added C++ code to read from Raspberry Pi. main.ccp contains core read/write code from GPIO pins while wiringPi.h contains libraries to access GPIO

    
2. To connect flow sensor to PI, do the following:

        * Connect the red wire to +5V, 
        * the black wire to common ground 
        * and the yellow sensor wire to pin #2

3. Come here for the PI GPIO layout:
        https://www.raspberrypi.org/documentation/usage/gpio/

4. Original Pi Drivers here:
https://github.com/adafruit/Adafruit-Flow-Meter/blob/master/Adafruit_FlowMeter.pde?fbclid=IwAR3SIUdLE5aKkmUtFKgHbSNPZg7KXZPyR9lolm_gVZimlLtZKGQ9XfKeaMI


#### Python read/write Module

Goal: Python code to port csvs into the following blob string:

CONNECTION_STRING = [Redacted]

Read write driver should be able to call c++ main function, clean csvs from memory, and write to the above location periodically. 
