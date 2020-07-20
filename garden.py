#Virtualisation of Sensors in garden


import paho.mqtt.publish as publish
import random
from random import randint
import time

def garden():
    while 1:
        randomh = randint(1, 100)
        publish.single("shlogo/S4441/", randomh, hostname="192.168.2.54")
        time.sleep(2)
        randomt = randint(-10, 50)
        publish.single("shlogo/S4442/", randomt, hostname="192.168.2.54")
        time.sleep(2)
        randomuv = randint(1, 11)
        publish.single("shlogo/S4443/", randomuv, hostname="192.168.2.54")
        time.sleep(5)
#garden()    
print("Garden Done")
