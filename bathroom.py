#Virtualisation of Sensors in bathroom


import paho.mqtt.publish as publish
import random
from random import randint
import time

def bathroom():
    
    while 1:
        randomh = randint(1, 100)
        publish.single("shlogo/S5551/", randomh, hostname="192.168.2.54")
        time.sleep(2)
        randomt = randint(-10, 50)
        publish.single("shlogo/S5552/", randomt, hostname="192.168.2.54")
        time.sleep(5)

#bathroom()
print("Bathroom Done")


