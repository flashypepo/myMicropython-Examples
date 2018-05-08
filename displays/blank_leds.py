# blank_leds.py
# - clear all pixels of LED-matrix (8*8 pizels) on D7 / GPIO13
# - clear all pixels of LEDstick (8 pixels) on D7 / GPIO13
# 2017_0122 PePo new, for convenience

import machine
import neopixel

def blank(np):
    np.fill((0, 0, 0))
    np.write()

blank(neopixel.NeoPixel(machine.Pin(13), 8 * 8))
blank(neopixel.NeoPixel(machine.Pin(15), 1 * 8))
