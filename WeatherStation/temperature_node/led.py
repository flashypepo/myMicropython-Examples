# set LED
# Configuration Temperature-node:
#        ,,     - LED attached to D6 (GPIO12)
from micropython import const
import machine, time

# default pin for external LED
__LED_PIN = const(12) # WeMOS D1 mini D6

def setup(pin = __LED_PIN):
    led = machine.Pin(pin, machine.Pin.OUT)
    led.off()
    return (led)

# blinky
def blink(dt = 1.0):
    led = setup()
    try:
        while True:
            led.on()
            time.sleep(dt)
            led.off()
            time.sleep(dt)
    except:
        print('blink() intercept')
