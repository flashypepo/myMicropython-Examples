# demo of reading a button on Huzzah
# 2017-0808 PePo initial setup
# Adafruit article:
# https://learn.adafruit.com/micropython-hardware-digital-i-slash-o/digital-inputs

import machine, time

# define button on pin 12, PULL_UP for proper state
# see Adafruit article!
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

#define LED on pin 14 to be set on / off by button
led = machine.Pin(14, machine.Pin.OUT)
led.off()

# helper functions
def ledOn():
    led.value(1)

def ledOff():
    led.value(0)

while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        print('Button pressed!')
        ledOn()
    elif not first and second:
        print('Button released!')
        ledOff()
