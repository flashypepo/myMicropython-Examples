# CircuitPython demo from https://www.youtube.com/watch?v=gfQBhe-1t8M
# 2017-0821 PePo not tested yet
import board
import time
import neopixel

__PIXELS = 10
npix = neopixel.NeoPixel(board.NEOPIXEL, __PIXELS)

def lightAll(col):
    for pix in range(0, __PIXELS):
        npix[pix] = col
    npix.write()
    return

while True:
    for i in range(0,255,5):
        lightAll((0,i,0))
        time.sleep(0.02)

    for i in range(255, -1, -5):
        lightAll((0,i,0))
        time.sleep(0.02)

    for i in range(0,255,5):
        lightAll((0,0,1))
        time.sleep(0.02)

    for i in range(255,-1. -5):
        lightAll((0,0,i))
        time.sleep(0.02)
