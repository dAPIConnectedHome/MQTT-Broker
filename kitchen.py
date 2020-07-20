#Virtualisation of Sensors in kitchen


import paho.mqtt.publish as publish
import random
from random import randint
import time

def kitchen():
    while 1:
        randomh = randint(1, 100)
        publish.single("shlogo/S3331/", randomh, hostname="192.168.2.54")
        time.sleep(2)
        randomt = randint(-10, 50)
        publish.single("shlogo/S3332/", randomt, hostname="192.168.2.54")
        time.sleep(5)


print("Kitchen Done")
