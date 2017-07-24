# Relay op WeMOS D1 mini
# wemos.cc Relay Shield info: https://wiki.wemos.cc/doku.php
# 2017-0618 PePo
import machine
import time

# relay connected to pin D6 = GPIO12
relay = machine.Pin(5, machine.Pin.OUT)

relayState = True

# toggle relay
# when on; red LED is turned on (alarm)
for i in range(10):
    if relayState:
        relay.on() # open - alarm/red led on
    else:
        relay.off() # close, red led off
    time.sleep(0.5)
    relayState =  not relayState
    print('relay state={0}'.format(relayState))
