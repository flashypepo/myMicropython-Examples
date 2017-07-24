# stream_plasma.py - implementation of oldskool plasma effect
# see http://www.bidouille.org/prog/plasma
#
# 2017_0122 PePo adopted for default neopixel MicroPython library
#           and LED matrix 8*8
#
# Sources: Youtube https://www.youtube.com/watch?v=QcyuYvyvOEI&index=14&list=PLuuAy8GJr5z1WoOJAFh1adr_yjCMJQ2Yl
# Tony Dicola source: https://gist.github.com/tdicola/6fe1fbc173dcd49de3a95be5fd9594f6

import machine
import math
import neopixel
import time

# LED matrix: 8 * 8 pixels
PIXEL_WIDTH = 8
PIXEL_HEIGHT = 8
MAX_BRIGHT = 50.0  # 100.0

# create a neopixel array
# NodeMU: neopixel connected to pin GPIO13 (D7)
np = neopixel.NeoPixel(machine.Pin(13), PIXEL_WIDTH * PIXEL_HEIGHT)

# Clear all the pixels and turn them off.
np.fill((0, 0, 0))
np.write()

while True:
    np.fill((0, 0, 0))
    current = time.ticks_ms() / 1000.0
    for x in range(PIXEL_WIDTH):
        for y in range(PIXEL_HEIGHT):
            v = 0.0
            v += math.sin(x + current)
            v += math.sin(1.0 * (x * math.sin(current / 0.5) + y * math.cos(current / 0.25)) + current)
            cx = x + 0.5 * math.sin(current / 5.0)
            cy = y + 0.5 * math.cos(current / 3.0)
            v += math.sin(math.sqrt((math.pow(cx, 2.0) + math.pow(cy, 2.0)) + 1.0) + current)
            v = (v + 3.0) / 6.0
            # 2017_0122 added: color r,g,b must be always > 0
            r = math.sin(v * math.pi)
            r = (r + 1.0) / 2.0 # scale to 0..1
            g = math.sin(v * math.pi + 2.0 * math.pi / 3.0)
            g = (g + 1.0) / 2.0 # scale to 0..1
            b = math.sin(v * math.pi + 4.0 * math.pi / 3.0)
            b = (b + 1.0) / 2.0 # scale to 0..1
            np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * r),
                                       int(MAX_BRIGHT * g),
                                       int(MAX_BRIGHT * b))
            # np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * math.fabs(r)),
            #                            int(MAX_BRIGHT * math.fabs(g)),
            #                            int(MAX_BRIGHT * math.fabs(b)))
    np.write()
