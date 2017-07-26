# blank_leds.py
# - clear all pixels of LED-matrix (8*8 pizels) on D7 / GPIO13
# - clear all pixels of LEDstick (8 pixels) on D7 / GPIO13
# 2017_0206 PePo added DIN_PIN, Featherwing Neopixel
# 2017_0122 PePo new, for convenience

import machine
import neopixel

def blank(np):
    np.fill((0, 0, 0))
    np.write()

# Neopixel Data Input Pin...
#TODO: input argument
#DIN_PIN = 13 # NodeMCU - neopixel-stick 8*1
DIN_PIN = 15  # Feather / NodeMCU LED-matrix
#blank(neopixel.NeoPixel(machine.Pin(DIN_PIN), 8 * 8)) # LED matrix 8*8
blank(neopixel.NeoPixel(machine.Pin(DIN_PIN), 8 * 4)) # Featherwing Neopixel
