'''
main.py: blink builtin LED
2017-0604 PePo
'''
import machine
import time
# toggle HIGH/LOW value
# order is such that builtin LED ends with OFF
def togglePin(pin, maxCount, delay):
    for i in range(maxCount):
        pin.value(False)
        time.sleep(delay)
        pin.value(True)
        time.sleep(delay)

LED_BUILTIN = 5
led = machine.Pin(LED_BUILTIN, machine.Pin.OUT)
togglePin(led, 10, 0.25)
gc.collect()
