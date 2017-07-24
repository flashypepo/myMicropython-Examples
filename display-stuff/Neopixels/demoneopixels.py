# demo neopixels
#
# 2016-1204 PePo pin D7
# 2016_1003 Vcc en GND op NodeMCU werkt niet
#   Vcc en GND from 5V source !!
#   Vcc en GND met breadboard voeding geeft te 
#   weinig spanning/stroom? Lage neopixel-waarden 
#   nemen (<=2), lukt soms
# 2016_1003 PePo new, based upon
#   https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/neopixel.html

import time
import machine, neopixel

# 2016-1204: configuration NodeMCU
#   neopixels (8*8) connected to pin D7 (GPIO13)
PIXEL_PIN = machine.Pin(13, machine.Pin.OUT) 
PIXEL_COUNT = 64  # number of neopixels

# function demo
def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

# 2016_1204 PePo added off() to blank neopixels
def off():
    np.fill((0,0,0))
    np.write()

# neopixel stick (8 neopixels) aangesloten op pin D5 (GPIO14)
#np = neopixel.NeoPixel(machine.Pin(14), 8)
np = neopixel.NeoPixel(PIXEL_PIN, PIXEL_COUNT)
demo(np)
