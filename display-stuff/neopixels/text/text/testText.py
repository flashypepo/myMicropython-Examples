# testText.py - test fontbitmap and font5*8.bin
# 2017_0206 PePo new, it doesnot work. Font too big (5*8?) for Featherwing Neopixel
# GitHub: https://github.com/adafruit/micropython-adafruit-bitmap-font/releases

import neopixel
import machine

# 2016_0206: Featherwing NeoPixel connected to Feather Huzzah ESP8266 at GPIO15
DISPLAY_WIDTH = 8
DISPLAY_HEIGTH = 4
DIN_PIN = 15

matrix = neopixel.NeoPixel(machine.Pin(DIN_PIN, machine.Pin.OUT), DISPLAY_WIDTH * DISPLAY_HEIGTH)

# pixel function
def matrix_pixel(x, y, color):
    #matrix[y * 8 + x] = color #ERROR: index out of range
    matrix[y * 4 + x] = color #wrong character


# create bitmapfont
import bitmapfont
bf = bitmapfont.BitmapFont(8, 4, matrix_pixel)
bf.init()


# draw some text
bf.text('1', 0, 0, (50, 0, 50))
matrix.write()

