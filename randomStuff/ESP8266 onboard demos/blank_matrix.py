# blank_matrix.py - clear all pixels of a NeoPoixel matrix
# 2017_0204 PePo added PIXEL_PIN, Feather NeoPixel (8*4)
# 2017_0122 PePo new, for convenience, LED_matrix (8*8)

import machine
import neopixel

PIXEL_WIDTH = 8
PIXEL_HEIGHT = 4 #8
PIXEL_PIN = 15 # Feather NeoPixel
#PIXEL_PIN = 13 # NodeMCU

np = neopixel.NeoPixel(machine.Pin(PIXEL_PIN), PIXEL_WIDTH * PIXEL_HEIGHT)

np.fill((0, 0, 0))
np.write()
