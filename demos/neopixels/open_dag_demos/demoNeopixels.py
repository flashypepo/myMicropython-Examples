# demoNeopixels - demo of neopixels
# accoriding to
# https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/neopixel.html
# 2017_0125 PePo new

import machine, neopixel

# LED matrix: 8 * 8 pixels
PIXEL_WIDTH = 8
PIXEL_HEIGHT = 8

#This configures a NeoPixel LED-matrix on GPIO13 with 8*8 pixels.
np = neopixel.NeoPixel(machine.Pin(13), PIXEL_WIDTH*PIXEL_HEIGHT)

#To set the colour of pixels use:
np[0] = (255, 0, 0) # set to red, full brightness
np[1] = (0, 128, 0) # set to green, half brightness
np[2] = (0, 0, 64)  # set to blue, quarter brightness

#Then use the write() method to output the colours to the LEDs:
np.write()

#The following demo function makes a fancy show on the LEDs:
import time
time.sleep_ms(1000) # wacht even ...

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

# Execute it using:
demo(np)
