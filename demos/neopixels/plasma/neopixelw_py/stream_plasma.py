# 2017_0122 PePo changed some led-matrix parameters
#           negative numbers for r,g,b, will give maximum brighness!
import machine
import math
import neopixelw
import time

PIXEL_WIDTH = 8
PIXEL_HEIGHT = 8 #5
MAX_BRIGHT = 100.0

#np = neopixelw.NeoPixelRGBW(machine.Pin(15), PIXEL_WIDTH*PIXEL_HEIGHT)
np = neopixelw.NeoPixelRGBW(machine.Pin(13), PIXEL_WIDTH*PIXEL_HEIGHT)

# Clear all the pixels and turn them off.
np.fill((0,0,0,0))
np.write()

while True:
    np.fill((0,0,0,0))
    current = time.ticks_ms() / 1000.0
    for x in range(PIXEL_WIDTH):
        for y in range(PIXEL_HEIGHT):
            v = 0.0
            v += math.sin(x+current)
            v += math.sin(1.0*(x*math.sin(current/0.5)+y*math.cos(current/0.25))+current)
            cx = x + 0.5*math.sin(current/5.0)
            cy = y + 0.5*math.cos(current/3.0)
            v += math.sin(math.sqrt((math.pow(cx, 2.0)+math.pow(cy, 2.0))+1.0)+current)
            v = (v+3.0)/6.0
            r = math.sin(v*math.pi)
            g = math.sin(v*math.pi+2.0*math.pi/3.0)
            b = math.sin(v*math.pi+4.0*math.pi/3.0)
            #w = math.sin(v*math.pi+6.0*math.pi/3.0)
            np[y*PIXEL_WIDTH+x] = (int(MAX_BRIGHT*r),int(MAX_BRIGHT*g),int(MAX_BRIGHT*b),0)
    np.write()
