# test_stickneopixel.py - test LED-stick
# 2017_0122 PePo new
# Source:
# Tony Dicola source: https://gist.github.com/tdicola/6fe1fbc173dcd49de3a95be5fd9594f6

import machine
import math
import neopixel
import time

# 2017_0122 LED stick:  GPIO15 / D8, 1 * 8 pixels
PIXEL_WIDTH = 8
PIXEL_HEIGHT = 1
MAX_BRIGHT = 50 # 0 .. 255

np = neopixel.NeoPixel(machine.Pin(15), PIXEL_WIDTH*PIXEL_HEIGHT)

# Clear all the pixels and turn them off.
np.fill((0,0,0))
np.write()

while True:
    # RED
    np.fill((MAX_BRIGHT, 0, 0))
    np.write()
    time.sleep(1.0)

    # GREEN
    np.fill((0, MAX_BRIGHT, 0))
    np.write()
    time.sleep(1.0)

    # BLUE
    np.fill((0, 0, MAX_BRIGHT))
    np.write()
    time.sleep(1.0)

    # PINK
    np.fill((MAX_BRIGHT, 0, MAX_BRIGHT))
    np.write()
    time.sleep(1.0)

    # WHITE
    np.fill((MAX_BRIGHT, MAX_BRIGHT, MAX_BRIGHT))
    np.write()
    time.sleep(1.0)

    # blank pixels
    np.fill((0, 0, 0))
    np.write()
    time.sleep(1.0)
