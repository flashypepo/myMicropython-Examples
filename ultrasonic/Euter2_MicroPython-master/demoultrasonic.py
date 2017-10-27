import ultrasonic
from time import sleep

# GPIO pins for specific development board
#gpio = {"TX":01, "RX":03, "D0": 16, "D1": 05, "D2": 04, "D3": 00, "D4": 02, "D5": 14, "D6": 12, "D7": 13, "D8": 15}

trigger = 12 #gpio[ "D6" ]
echo = 14 #gpio[ "D5" ]

#create sensor hc on pins trigger and echo
hc = ultrasonic.Ultrasonic( trigger, echo)

dist = 0  # distance value

# function to get distance for ever
def run(dt=0.5):
    while True:
        # Get reading from sensor
        dist = hc.distance() # distance in m
        #ok: print('afstand is {0:3.1f} cm'.format(dist*100))
        print('{0:3.1f}'.format(dist*100)) # distance in cm
        sleep(dt)

# doit...
try:
    run()
except:
    print(None)
