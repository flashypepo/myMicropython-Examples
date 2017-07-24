# blank_stick.py - clear all pixels of LED-stick
# 2017_0122 PePo new, for convenience

import machine
import neopixel

# 2017_0122 LED stick:  GPIO15 / D8, 1 * 8 pixels
PIXEL_WIDTH = 8
PIXEL_HEIGHT = 1

# create neopixel array
np = neopixel.NeoPixel(machine.Pin(15), PIXEL_WIDTH * PIXEL_HEIGHT)

# Clear all the pixels and turn them off.
np.fill((0, 0, 0))
np.write()
