# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import RPi.GPIO as GPIO
import time

FLOW_SENSOR = 2

GPIO.setmode(GPIO.BCM)

GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)



# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=HydroIoTHub.azure-devices.net;DeviceId=device1;SharedAccessKey=yEWaKoMpVmW5x67E6mdzwGkLEUv28tYEzJ1DWKkvrMw="
# Define the JSON message to send to IoT Hub.
TIMESTAMP = time.time() 
PULSE = 1


MSG_TXT = '{{"timestamp": {timestamp},"pulse": {pulse}}}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    client.connect()
    return client

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            pulse =  0

            timeout = time.time() + 3

            while time.time() < timeout:
                if GPIO.input(FLOW_SENSOR):
                     pulse += 1

            print(pulse)

            # Build the message with simulated telemetry values.
            timestamp = TIMESTAMP 
            msg_txt_formatted = MSG_TXT.format(timestamp=timestamp, pulse=pulse)
            message = Message(msg_txt_formatted)
            message.custom_properties['Important Sensor'] = "yes"
            message.content_encoding = "utf-8"
            message.content_type = "application/json"
   

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )
        GPIO.cleanup()

iothub_client_init()
iothub_client_telemetry_sample_run()
