#new client, which connected with the broker
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)





objectID = 0
#I am an actuator, so i have an A as identifier and a defined number
defaultID = "A9876"
mytype = "actuator"
mymode = "BOOL"
mydirection = "R"
myrangemin = "0"
myrangemax = "1"

#SXXXX;actuator;R/S/T;BOOL/RANGE;0;1
#shlogo/data/


#############################################################################################

#Send my identifier to the "new" topic
publish.single("shlogo/new/", defaultID, hostname="192.168.2.54")



#Subscribe to my identifier topic
def on_connect(client, userdata, flags, rc):
    print("Connected to new-topic!")
    client.subscribe("shlogo/new/{}/#".format(defaultID))
    print ("Connected to my defaultID topic!")
    
 
 
 
 
# The callback for when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    global objectID
    print(msg.topic+" "+str(msg.payload))
    objectID = msg.payload
    print ("Meine objectID: "+objectID)
    
    print("Sende jetzt meine Infos an shlogo/data/")
    publish.single("shlogo/data/", objectID+";"+mytype+";"+mydirection+";"+mymode+";"+myrangemin+";"+myrangemax, hostname="192.168.2.54")
  
    
    client.subscribe("shlogo/{}/set/".format(objectID))
    if msg.payload == "1":
        print("Received message ON")
        GPIO.output(23, GPIO.HIGH)


    if msg.payload == "0":
        print("Received message OFF")
        GPIO.output(23, GPIO.LOW)
    

# Create an MQTT client and attach our routines to it

client = mqtt.Client()  
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.2.54")
client.loop_start()
msgsend = 1
while msgsend== 1:
    time.sleep(2)


    
