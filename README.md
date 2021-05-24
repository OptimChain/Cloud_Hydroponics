### Cloud Based Hydroponics sensoring

In the current hydroponics industry, sensors are used to monitor greenhouse floor-level hydraulic systems to monitor for both water and air deviations in atmospheric conditions. The downtime of any components in this sensoring setup would cause significant damage to greenhouse plant health. Cloud Hydroponics is a cloud azure instrumentation system to complement the existing floor level greenhouse networks. Cloud instrumentation will allow alerting, monitoring, and real time storage of sensor telemetry at scale with customizability.

The system architecture is describled in Figure 1. A floor level master computer is used to control the pis while the pis upload telemetry events to the azure event-hub. (https://azure.microsoft.com/en-us/services/event-hubs/). Telemetry events are ingested and built into a stream with azure data lake storage and processed for Email and Text Alerting. Control-Charts, Rule based Alerting, and Historical Analysis is then built on the azure data lake layer. (https://azure.microsoft.com/en-us/solutions/data-lake/)

Figure 1: Cloud Azure Architecture

![image](https://user-images.githubusercontent.com/84352976/119286126-7be7bb80-bbf8-11eb-8b6b-cc7f12720f0a.png)

#### To set up the pi system:

Pi Setup:

1. Fork the code within the Hydroponics_Driver folder: 
2. Install Orchestrator.py as a python module within the Raspbian OS. To use the Raspbian OS, see: https://www.raspberrypi.org/software/ 
3. Run Orchestrator.py within the master computer to send GPIO signals within GPIO 2. The flow sensor should be connected to GPIO 2 with group and 5v connected to the relevent pins: https://www.raspberrypi.org/documentation/usage/gpio/
4. To onboard additional Pis, loop additional functions in the iothub_client_telemetry_sample_run() function or build additional DeviceIds to onboard in more raspberry pis.
  
Simulated Telemetry Setup:

1. Fork the code within the Hydroponics_Driver folder: 
2. Install Simulated_Telemetry.py within any local computer python program. When this is run, simulated pulse telemetry will flow into our system

#### To view the Cloud System:

1. Log into the Azure Portal: https://azure.microsoft.com/en-us/features/azure-portal/
2. The hydrostor account contains the root for stored telemetry (Figure 1):

Figure 1: Stored Telemetry Account
![image](https://user-images.githubusercontent.com/84352976/119286880-30cea800-bbfa-11eb-99b6-5a16a6eaa7b5.png)

3. The flowdatacontainer account contains all archived telemetry (Figure 2 and Figure 3):

Figure 2: Archived Telemetry Folders
![image](https://user-images.githubusercontent.com/84352976/119287003-712e2600-bbfa-11eb-80d0-5f72538eb08f.png)

Figure 3: Sample json file for flow data
![image](https://user-images.githubusercontent.com/84352976/119287091-9de23d80-bbfa-11eb-93f1-5ba6eaa8084e.png)

4. The HydroIoTHub eventhub (Figure 4) contains all sent events. Go here to configure new Pi devices or change the connection string for devices. The current connection string for the first device is: "HostName=HydroIoTHub.azure-devices.net;DeviceId=device1;SharedAccessKey=yEWaKoMpVmW5x67E6mdzwGkLEUv28tYEzJ1DWKkvrMw="

Figure 4: HydroIoTHub
![image](https://user-images.githubusercontent.com/84352976/119287167-c702ce00-bbfa-11eb-8de0-47991c9f576a.png)

5. comm-serv contains all the emails and text alerting services (Figure 5)

Figure 5: comm-serv
![image](https://user-images.githubusercontent.com/84352976/119289087-c5d3a000-bbfe-11eb-93c4-2459a40b9d6c.png)


#### To setup the Dashboarding System:

1. Fork the code inside the Hydroponics_Dashboard folder
2. Run app.py to build a local version of the dashboard (Figure 5)
3. If any events arrive at the event-hub, then these datapoints will show up in this dashboard

Figure 6: Graph Local Build
https://www.facebook.com/messenger_media/?thread_id=100006558996249&attachment_id=993438838069022&message_id=mid.%24cAAAABzx9RxV_YOMb9F5L521JDFeR







