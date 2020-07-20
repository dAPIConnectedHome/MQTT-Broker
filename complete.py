import threading
import random
from random import randint
import time

import bathroom
import livingroom
import kitchen
import garden
import terrace


thread_bathroom = threading.Thread(target=bathroom.bathroom)
thread_livingroom = threading.Thread(target=livingroom.livingroom)
thread_kitchen = threading.Thread(target=kitchen.kitchen)
thread_garden = threading.Thread(target=garden.garden)
thread_terrace = threading.Thread(target=terrace.terrace)

a = 45
t1 = thread_bathroom.start()
t2 = thread_livingroom.start()
t3 = thread_kitchen.start()
t4 = thread_garden.start()
t5 = thread_terrace.start()