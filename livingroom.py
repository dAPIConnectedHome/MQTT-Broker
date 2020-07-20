#Virtualisation of Sensors in living room


import paho.mqtt.publish as publish
import random
from random import randint
import time

def livingroom():
    while 1:
        randomh = randint(1, 100)
        publish.single("shlogo/S2221/", randomh, hostname="192.168.2.54")
        time.sleep(2)
        randomt = randint(-10, 50)
        publish.single("shlogo/S2222/", randomt, hostname="192.168.2.54")
        time.sleep(5)

#livingroom()
print("Living Room Done")
