# stream_plasma.py - implementation of oldskool plasma effect
# see http://www.bidouille.org/prog/plasma
#
# 2017_0204 PePo adopted for Feather NeoPoixel 8*4 on GPIO15
# 2017_0122 PePo adopted for default neopixel MicroPython Library
#           and LED matrix 8*8
#
# Sources: Youtube https://www.youtube.com/watch?v=QcyuYvyvOEI&index=14&list=PLuuAy8GJr5z1WoOJAFh1adr_yjCMJQ2Yl
# Tony Dicola source: https://gist.github.com/tdicola/6fe1fbc173dcd49de3a95be5fd9594f6

import machine
import math
import neopixel
import time

#''' 2017_0204 Feather Neopixel matrix: 8 * 4 pixels, GPIO15
PIXEL_WIDTH = 8
PIXEL_HEIGHT = 4
PIXEL_PIN = 15
#'''
''' 2017_0726 Lolin32 met neopixel ring (12 pixels) op GPIO15
# LED matrix: 8 * 8 pixels
PIXEL_WIDTH = 12
PIXEL_HEIGHT = 1
PIXEL_PIN = 15
#'''
#PIXEL_PIN = 13 #NodeMU: neopixel connected to pin GPIO13 (D7)
MAX_BRIGHT = 10 #50.0  # 100.0

# create a neopixel array
#DEPRECATED: np = neopixel.NeoPixel(machine.Pin(13), PIXEL_WIDTH * PIXEL_HEIGHT)
np = neopixel.NeoPixel(machine.Pin(PIXEL_PIN), PIXEL_WIDTH * PIXEL_HEIGHT)

# Clear all the pixels and turn them off.
def blank():
    np.fill((0, 0, 0))
    np.write()

def demo():
    while True:
        np.fill((0, 0, 0))
        current = time.ticks_ms() / 1000.0
        for x in range(PIXEL_WIDTH):
            for y in range(PIXEL_HEIGHT):
                v = 0.0
                #1. ORG: v += math.sin(x * 10.0 + current)
                v += math.sin(x + current)

                #2. ORG: v += math.sin(10.0 * (x * math.sin(current / 2) + y * math.cos(current / 3)) + current)
                v += math.sin(1.0 * (x * math.sin(current / 0.5) + y * math.cos(current / 0.25)) + current)

                #3
                cx = x + 0.5 * math.sin(current / 5.0)
                cy = y + 0.5 * math.cos(current / 3.0)
                #3. ORG: v += math.sin(math.sqrt(100.0 * (math.pow(cx, 2.0) + math.pow(cy, 2.0)) + 1.0) + current)
                v += math.sin(math.sqrt((math.pow(cx, 2.0) + math.pow(cy, 2.0)) + 1.0) + current)

                v = (v + 3.0) / 6.0

                # add color r,g,b must be always > 0
                r = math.sin(v * math.pi)
                g = math.sin(v * math.pi + 2.0 * math.pi / 3.0)
                b = math.sin(v * math.pi + 4.0 * math.pi / 3.0)

                # scale r,g,b to range 0..1
                r = (r + 1.0) / 2.0
                g = (g + 1.0) / 2.0
                b = (b + 1.0) / 2.0
                np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * r),
                                        int(MAX_BRIGHT * g),
                                        int(MAX_BRIGHT * b))
                # np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * math.fabs(r)),
                #                            int(MAX_BRIGHT * math.fabs(g)),
                #                            int(MAX_BRIGHT * math.fabs(b)))
        np.write()

#run
try:
    blank()
    demo()
except:
    blank()
    print('done')
