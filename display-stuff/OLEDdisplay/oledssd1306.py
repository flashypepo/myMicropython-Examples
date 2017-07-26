# oledssd1326.py - test 128*32 I2C-OLED
# Pre-conditions
#    * micropython v1.8.5+ - het moet module importeren ondersteunen
#    * ssd1306.mpy op de ESP8266
# Bronnen:
#  https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display/
#  Micropython workshop op WeMOS R1 Mini ESP8266 
#     http://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/setup.html
#
# 2017-0723 PePo some tweaks, Amica-NodeMCU + test OLD-displays
#  after connecting a (new) OLED: reset-board (Cntrl-D)
#  >>> import oledssd1306
#  >>> oledssd1306.demo()
# 2017-0101 PePo - updated I2C constructor (version 1.8.6 - 2017-0101)
# 2016-1022 PePo - het werkt op een WeMOS R1 mini (v1) met OLED shield
# ----------------------
from machine import Pin, I2C
import ssd1306
import time

# 2017_01010 updated I2C constructor
# DEPRECATED: i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
print('i2c.scan: ', i2c.scan())   #[60]
__WIDTH = 128 # screen dimensions
__HEIGHT = 32
oled = ssd1306.SSD1306_I2C(__WIDTH, __HEIGHT, i2c)

# several examples ..
def whiteScreen():
    oled.fill(1)
    oled.show()

def clearScreen():
    oled.fill(0)
    oled.show()

# 4 pixels ON in the corners
def pixelsInCorner(w=__WIDTH, h=__HEIGHT):
    oled.pixel(0,0,1)
    oled.pixel(w-1,h-1,1)
    oled.pixel(w-1,0,1)
    oled.pixel(0,h-1,1)
    oled.show()

def display(msg):
    oled.text(msg, 0, 0)
    oled.show()

def displayT(t):
    oled.text('Temperature: {0}'.format(t),0,10)
    oled.show()

# start demo
def demo(dt=1.5):
    whiteScreen()
    time.sleep(dt)
    clearScreen()

    display('Hello world!')
    time.sleep(dt)
    clearScreen()

    pixelsInCorner()
    time.sleep(dt)
    clearScreen()

    #while(True):
    for i in range(20, 26):
        clearScreen()
        displayT(i)
        time.sleep(1)

    time.sleep(dt)

    #cleanup display
    clearScreen()
    display("Demo done!")
    print('Demo done!')

demo()