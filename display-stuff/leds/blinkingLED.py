# Example of a blinking led in micropython
# Arduino style: setup and loop
# 2016-1022 PePo builtin LED is GPIO 2, which has pull-up to Vcc
# 2016-0903 PePo, based upon
#  https://learn.adafruit.com/micropython-basics-blink-a-led/blink-led

###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import machine
import time
print('Blinking LED...')
led = machine.Pin(2, machine.Pin.OUT) #D8
led.high() # init led OFF
time.sleep(0.1) # wait 

while True:
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    led.low()  #on
    time.sleep(0.5)
    led.high() #off
    time.sleep(0.5)
