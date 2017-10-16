# demo HC04 ulrasonic distance sensor
# 2017-1016 PePo new, using bitmapfont font5*8

from micropython import const
import machine
from time import sleep

import ultrasonic
#import ssd1306
import myssd1306 as ssd1306  #includes draw_bitmap

# GPIO pins for specific development board
#gpio = {"TX":01, "RX":03, "D0": 16, "D1": 05, "D2": 04, "D3": 00, "D4": 02, "D5": 14, "D6": 12, "D7": 13, "D8": 15}

# HSR04 GPIO pins
trigger = 12 #gpio[ "D6" ]
echo = 14 #gpio[ "D5" ]

# WeMOS-LoLin32-OLED i2c pins
_SCL = const(4)
_SDA = const(5)
_DISPLAY_WIDTH  = const(128)  # Width of display in pixels.
_DISPLAY_HEIGHT = const(64)   # LoLin-ESP32-OLED height of display.

#create sensor hc on pins trigger and echo
hc = ultrasonic.Ultrasonic( trigger, echo)

# create i2c and OLED-i2c objects
i2c = machine.I2C(scl=machine.Pin(_SCL), sda=machine.Pin(_SDA))
#i2c = I2C(scl=Pin(SCL), sda=Pin(SDA), freq=100000)
i2c.scan()   #[60]
oled = ssd1306.SSD1306_I2C(_DISPLAY_WIDTH, _DISPLAY_HEIGHT, i2c)


# OLED helper: blank oled screen
def eraseOled():
    oled.fill(0)
    oled.show()

# OLED helper: specify display_pixel function including oled.show()
def display_pixel(x, y, color):
    oled.pixel(x, y, color)
    oled.show()

# generate bitmap font from font5x8.bin
import bitmapfont
# 128 and 64 are the OLED dimensions!
bf = bitmapfont.BitmapFont(_DISPLAY_WIDTH, _DISPLAY_HEIGHT, display_pixel)
bf.init()

# distance value
dist = 0

# main program:
# 1. measure distance
# 2. show on OLED
# 3. dump on serial to other systems
def run():
    while True:
        eraseOled()
        # Get reading from sensor
        #PePo TODO: dist = hc.distance_in_cm()
        dist = hc.distance()
        #print('afstand is {0:3.1f} cm'.format(dist*100))
        #oled.text('afstand: {0:3.1f} cm'.format(dist*100), 0, 0)
        #oled.show()
        bf.text('afstand: {0:3.1f} cm'.format(dist*100), 0, 30, 1)
        sleep(0.4)

# run
try:
    run()
except:
    eraseOled()
    print ('done')
