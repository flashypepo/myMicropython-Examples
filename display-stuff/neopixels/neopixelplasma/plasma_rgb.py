# plasma_rgb.py - last steps in the implementation
# of oldskool plasma effect
# see http://www.bidouille.org/prog/plasma
#
# The plasma is basically a function on 2D space created
# by adding together a few sinusoids.
#
# By combining different types of sines and adding
# a time component the illusion of motion is achieved.
#
# 2017_0122 PePo new for Open Dag WF, using default library neopixel
#
# Sources: Youtube https://www.youtube.com/watch?v=QcyuYvyvOEI&index=14&list=PLuuAy8GJr5z1WoOJAFh1adr_yjCMJQ2Yl
# Tony Dicola source: https://gist.github.com/tdicola/6fe1fbc173dcd49de3a95be5fd9594f6

# #####################################################
# setup machine configuration
import machine
import math
import neopixel
import time

# LED matrix: 8 * 8 pixels
PIXEL_WIDTH = 8
PIXEL_HEIGHT = 8
MAX_BRIGHT = 50.0 #100.0

np = neopixel.NeoPixel(machine.Pin(13), PIXEL_WIDTH*PIXEL_HEIGHT)

# Clear all the pixels and turn them off.
np.fill((0,0,0))
np.write()

# #####################################################
# stap 7: add color ....
# To preserve the organic, fluid look of the plasma,
# the color scheme should not have discontinuities.
# However after adding our sines together,
# the plasma value is not necessarily constrained
# in a nice known interval like [0, 1].
# An easy way to solve this problem is to take the
# sinus again of the value we obtained at the end
# of our plasma function, and use it to create the
# RGB components of the color.
# In the examples below r, g and b are the red, green and
# blue components of the color, with -1 being the lowest
# intensity (black), and 1 the highest (fully saturated
# color component).
# r = sin(v*pi)
# g = sin(v*pi + 2*pi/3)
# b = sin(v*pi + 4*pi/3)
def stap7():
    while True:
        np.fill((0, 0, 0))  # start met alle leds uit...
        current = time.ticks_ms() / 1000.0  # tijd in seconden
        for x in range(PIXEL_WIDTH):  # voor alle pixels langs x-as
            for y in range(PIXEL_HEIGHT):  # en alle pixels langs de y-as
                v = 0.0
                v += math.sin(x + current)
                v += math.sin(1.0 * (x * math.sin(current / 0.5) + y * math.cos(current / 3.0)) + current)
                cx = x + 5.0 * math.sin(current / 5.0)
                cy = y + 3.0 * math.cos(current / 3.0)
                v += math.sin(math.sqrt((math.pow(cx, 2.0) + math.pow(cy, 2.0)) + 1.0) + current)
                v = (v + 3.0) / 6.0  # v in range: 0..1
                # calculate color
                # let op: r,g,b hebben negatieve waarden! -> zeer heldere intensiteit (255)
                # schaling of math.fabs() maakt er een positief getal van.
                # r = math.fabs(math.sin(v * math.pi))
                # g = math.fabs(math.sin(v * math.pi + 2.0 * math.pi / 3.0))
                # b = math.fabs(math.sin(v * math.pi + 4.0 * math.pi / 3.0))
                r = math.sin(v * math.pi)
                r = (r + 1.0) / 2.0  # r in range [0..1]
                g = math.sin(v * math.pi + 2.0 * math.pi / 3.0)
                g = (g + 1.0) / 2.0  # g in range [0..1]
                b = math.sin(v * math.pi + 4.0 * math.pi / 3.0)
                b = (b + 1.0) / 2.0  # b in range [0..1]
                np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * r),
                                           int(MAX_BRIGHT * g),
                                           int(MAX_BRIGHT * b))
        np.write()
stap7()

# #####################################################
# stap 8: add color  r = g = b = sin(v*5*pi)
# B/W pattern
def stap8():
    while True:
        np.fill((0, 0, 0))  # start met alle leds uit...
        current = time.ticks_ms() / 1000.0  # tijd in seconden
        for x in range(PIXEL_WIDTH):  # voor alle pixels langs x-as
            for y in range(PIXEL_HEIGHT):  # en alle pixels langs de y-as
                v = 0.0 # start met 0
                v += math.sin(x + current)
                v += math.sin(1.0 * (x * math.sin(current / 0.5) + y * math.cos(current / 3.0)) + current)
                cx = x + 5.0 * math.sin(current / 5.0)
                cy = y + 3.0 * math.cos(current / 3.0)
                v += math.sin(math.sqrt((math.pow(cx, 2.0) + math.pow(cy, 2.0)) + 1.0) + current)
                v = (v + 3.0) / 6.0  # v in range: 0..1
                # color
                r = math.sin(v * 5.0 * math.pi)
                r = (r + 1.0) / 2.0 # r in range 0..1
                g = b = r
                np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * r),
                                           int(MAX_BRIGHT * g),
                                           int(MAX_BRIGHT * b))
        np.write()
#stap8()
