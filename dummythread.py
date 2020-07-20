import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import random
from random import randint
################################################################################################################

objectlist = []
#comp = [0]

################################################################################################################

def on_connect_new(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))  
    client.subscribe("shlogo/new/")
    
#################################################################################################################    
def on_message_new(client, userdata, msg):
    global msgsend
    global defaultID
    global objectID
    print("Message received-> " + msg.topic + " " + str(msg.payload))
    defaultID = msg.payload
    print(defaultID)
    
    comp = str(randint(1000, 9999))
    
    ##compare to objectlist##
    for i in objectlist:
        if comp in i:
            comp = randint (1000, 9999)
    #####
    if defaultID.find("A") >= 0:
        comp = "A"+comp
    else:
        comp = "S"+comp
    objectID = comp
   #####################
    objectlist.append(objectID)
    print("connect to ID")
    
    print("Connected with ID Topic")
    client.subscribe("shlogo/new/{}/#".format(defaultID))
    print("Ich publishe jetzt die objectID "+str(objectID))
    publish.single("shlogo/new/{}/{}".format(defaultID, objectID), objectID, hostname="192.168.2.54")
    
    client.connect("192.168.2.54")
    

##################################################################################################################    
 




client = mqtt.Client()
client.connect("192.168.2.54")
client.on_connect = on_connect_new
client.loop_start()
msgsend = 0
objectID = 0
while 1:
    client.on_message = on_message_new
    time.sleep(1)
    print("Waiting for new client...")
    


    


    

    



