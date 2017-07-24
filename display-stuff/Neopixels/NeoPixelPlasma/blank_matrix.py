# blank_stick.py - clear all pixels of LED-matrix on D7 / GPIO13
# 2017_0122 PePo new, for convenience

import machine
import neopixel

PIXEL_WIDTH = 8
PIXEL_HEIGHT = 8

np = neopixel.NeoPixel(machine.Pin(13), PIXEL_WIDTH * PIXEL_HEIGHT)

np.fill((0, 0, 0))
np.write()
