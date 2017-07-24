# Example of blinking leds in micropython
# Arduino style: setup and loop
# 2016_1002 PePo - Grove-LEDs on D1 (GPIO5) and D5 (GPIO14)
# 2016-0823 PePo, based upon https://learn.adafruit.com/micropython-basics-blink-a-led/blink-led

###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import machine
import time
print('Blinking LED...')
led1 = machine.Pin(5, machine.Pin.OUT) #D1
led2 = machine.Pin(14, machine.Pin.OUT) #D5
led1.low() # init led1
led2.low() # init led2
time.sleep(1) # wait a second

while True:
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    led1.high()
    led2.low()
    time.sleep(0.5)
    led1.low()
    led2.high()
    time.sleep(0.5)
