# Examples of smileys on a LED matrix display.
# This example and library is meant to work with Adafruit CircuitPython API.
# 2017-0522 PePo - MicroPython
# source: https://learn.adafruit.com/micropython-hardware-led-backpacks-and-featherwings?view=all
# 2017-0520 PePo - first version, CircuitPython
# License: Public Domain

# Import all board pins and create i2c
######## CircuitPython (CP) #######
#from board import *
#import busio
# ?: import busio as io
#i2c = busio.I2C(SCL, SDA)

######## MicroPython (MP) #######
import machine
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))

# optional: print I2C devices
#i2c.scan()

import time

# Import the HT16K33 LED matrix module.
#from adafruit_ht16k33 import matrix #CP
import ht16k33_matrix as matrix #MP

# Creates a 8x8 matrix:
lefteye = matrix.Matrix8x8(i2c, address=0x70) # default I2C address = 0x70
righteye = matrix.Matrix8x8(i2c, address=0x71)
# Finally you can optionally specify a custom I2C address of the HT16k33 like:
# matrix = matrix.Matrix16x8(i2c, address=0x70)

# clear matrix m
def clear(m):
    '''clears matrix m'''
    m.fill(0)
    m.show()

# clear matrices
clear(lefteye)
clear(righteye)
time.sleep(0.5) #wait a little time

MATRIX_WIDTH = 8
MATRIX_HEIGTH = 8

# display pattern p on LED-matrix m
def dp(m, p):
    '''show pattern p on matrix m: 0=LED off, 1=LED on'''
    # iterate through pattern...
    for x in range(0, MATRIX_WIDTH):
        # iterate through a row to set led on or off...
        for y in range(0, MATRIX_HEIGTH):
            m.pixel(x, y, p[y][x])
    # show pattern
    m.show()

# TODO: more efficient to use a bitpattern 0b00111100, and so on
smile = []
smile = list(range(0, MATRIX_WIDTH))
#column     1  2  3  4  5  6  7  8
smile[0] = [0, 0, 1, 1, 1, 1, 0, 0]  # row 1 - top
smile[1] = [0, 1, 0, 0, 0, 0, 1, 0]  # row 2
smile[2] = [1, 0, 1, 0, 0, 1, 0, 1]  # row 3
smile[3] = [1, 0, 0, 0, 0, 0, 0, 1]  # row 4
smile[4] = [1, 0, 1, 0, 0, 1, 0, 1]  # row 5
smile[5] = [1, 0, 0, 1, 1, 0, 0, 1]  # row 6
smile[6] = [0, 1, 0, 0, 0, 0, 1, 0]  # row 7
smile[7] = [0, 0, 1, 1, 1, 1, 0, 0]  # row 8 - bottom

happy = []
happy = list(range(0, MATRIX_WIDTH))
#column   1  2  3  4  5  6  7  8
happy[0] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 1 - top
happy[1] = [0, 0, 1, 0, 0, 1, 0, 0]  # row 2
happy[2] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 3
happy[3] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 4
happy[4] = [0, 1, 0, 0, 0, 0, 1, 0]  # row 5
happy[5] = [0, 0, 1, 0, 0, 1, 0, 0]  # row 6
happy[6] = [0, 0, 0, 1, 1, 0, 0, 0]  # row 7
happy[7] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 8 - bottom

sad = []
sad = list(range(0, MATRIX_WIDTH))
#column   1  2  3  4  5  6  7  8
sad[0] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 1 - top
sad[1] = [0, 0, 1, 0, 0, 1, 0, 0]  # row 2
sad[2] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 3
sad[3] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 4
sad[4] = [0, 0, 1, 1, 1, 1, 0, 0]  # row 5
sad[5] = [0, 1, 0, 0, 0, 0, 1, 0]  # row 6
sad[6] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 7
sad[7] = [0, 0, 0, 0, 0, 0, 0, 0]  # row 8 - bottom

# demos
lefteye.brightness(1) # low intensity (0..15)
righteye.brightness(1)
dp(lefteye, smile)
dp(righteye, sad)

# demo smileys
def demo_smileys():
    for i in range(0, 15):
        lefteye.brightness(i)
        righteye.brightness(15-i)
        #print('.')
        time.sleep(0.5)

    time.sleep(2.0)

    lefteye.brightness(1) # low intensity (0..15)
    righteye.brightness(1)

    lefteye.blink_rate(2) # blink rate 0..3
    righteye.blink_rate(2) # blink rate 0..3
    time.sleep(2)

    lefteye.blink_rate(0) # blink rate 0..3
    righteye.blink_rate(0) # blink rate 0..3
