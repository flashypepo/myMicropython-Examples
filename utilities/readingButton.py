# readingButton - when button pressed LED is on.
# 
# 2016-0903 PePo new, based upon Tony DiCola MicroPython serie. 
#     https://learn.adafruit.com/micropython-hardware-digital-i-slash-o

###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import machine
import time

# LED on D8 (NodeMCU: GPIO15)
led = machine.Pin(15, machine.Pin.OUT)

# Button on D6 (NodeMCU: GPIO12)
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
#Push button on my Grove LED/pushbutton prototype
#button = machine.Pin(4, machine.Pin.IN) #werkt niet!

while True:
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        print('Button pressed!')
        led.high()
    elif not first and second:
        print('Button released!')
        led.low()
