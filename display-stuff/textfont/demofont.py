# demo font5x8
# learning guide: https://learn.adafruit.com/micropython-displays-drawing-text?view=all
# github: https://github.com/adafruit/micropython-adafruit-bitmap-font
# 2017-1016 PePo new

from micropython import const
import machine
import myssd1306 as ssd1306  #includes draw_bitmap
#import ssd1306  #excludes draw_bitmap

# OLED dimensions
_DISPLAY_WIDTH  = const(128)  # Width of display in pixels.
_DISPLAY_HEIGHT = const(64)   # LoLin-ESP32-OLED height of display.

# generate OLED object
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
#test: i2c.scan()
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# helper: specify display_pixel function including oled.show()
def display_pixel(x, y, color):
    oled.pixel(x, y, color)
    oled.show()

# generate bitmap font from font5x8.bin
import bitmapfont
# 128 and 64 are the OLED dimensions!
bf = bitmapfont.BitmapFont(128, 64, display_pixel)
bf.init()

# text on screen with font5*8
bf.text('Dat is een hele kluif!!', 0, 30, 1)
