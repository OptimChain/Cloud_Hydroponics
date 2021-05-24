# High Level Diagrams:

PVC Architexture: https://drive.google.com/file/d/1YTgufwX0AAyKJ3Pin0-16YOq_oPhZE95/view?usp=sharing

App Architexture: https://drive.google.com/file/d/1RcUjOQA1PDD137VwBZKDlc1MvjlBsVaH/view?usp=sharing

Build Specs Notes:

                2.21.2021:
                        Display: HD TV off the sphere motherboard
                        Transmit all pits to sphere motherboard (host event code here too)
                        GPIO to usb chip (adafruits): As many sensors

                        procure: Pi zeros with gpio header: 
                        procure: Generic 2x13 Pin Female Stacking Header 0.1" for Raspberry Pi Gpio Extra Tall(pack of 2)

                        Build the pi enclosure 

                        Sensors: http://homelab.link/ Ph
                        







                2.13.2021:  
                
                        Deliverables:
                        Detailed Configuration Spec 3.15.2021 on MVP completion
                        Pipe Spec  3.15.2021 on MVP completion
                        Pipe Shipped for MVP

                        OptimChain Deliverables:
                        MVP Code
                        One-Sensor solution

                        Meeting topics below:

                        MVP:
                        Flow Sensor:
                        Water should never stop flowing or Fungi will grow.
                        Sensor must detect pressure drop or flow rate drop
                        Dashboarding UI + Alerting
                        Average Pump
                        Historical Pump pressure
                        Localized Alerting

                        Pump:
                        Flow Rate will drop when sensor breaks down
                        Sensor Placement will capture flow drop

                        Other Sensors:
                        Humidity
                        Temperture Sensor
                        Interface for Sensors
                        Master Hub

                        Output Stream:
                        Time Series data standardized
                        Module read Time Series

                        MVP PVC:
                        Inital Contract : Mid-March to April

                        Reporting Cadence: 
                        Weekly/bi-weekly


# GPIO Driver Module
Goal: Write the output of flow sensors with the current flow values in csv datetime stamps. Azure Event IoT will be used to read the output streams.



1. Added C++ code to read from Raspberry Pi. main.ccp contains core read/write code from GPIO pins while wiringPi.h contains libraries to access GPIO

    
2. To connect flow sensor to PI, do the following:

        * Connect the red wire to +5V, 
        * the black wire to common ground 
        * and the yellow sensor wire to pin #2

3. Come here for the PI GPIO layout:
        https://www.raspberrypi.org/documentation/usage/gpio/

4. Original Pi Drivers here:
https://github.com/adafruit/Adafruit-Flow-Meter/blob/master/Adafruit_FlowMeter.pde?fbclid=IwAR3SIUdLE5aKkmUtFKgHbSNPZg7KXZPyR9lolm_gVZimlLtZKGQ9XfKeaMI


# Python read/write Module

Goal: Python code to port csvs into the following blob string:

"HostName=Hydroponics-OptimChain.azure-devices.net;DeviceId=Pi-1;SharedAccessKey=0CSZAi+BuUbPGr0Y5sRLkyCi9LKALDSk9Nf5ZybKtlw="

Read write driver should be able to call c++ main function, clean csvs from memory, and write to the above location periodically. 
