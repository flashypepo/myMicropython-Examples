# blinking LED - the hello world of embedded software
import machine
import time

# green LED on pin D6 = GPIO12
led = machine.Pin(12, machine.Pin.OUT)

# blink the led X time
for i in range(10):
    led.on() # on
    time.sleep(0.5) # wait..
    led.off() # off
    time.sleep(0.5)
