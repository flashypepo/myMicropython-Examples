# oledssd1326.py - test OLED I2C shield op een WeMOS R1 Mini met MicroPython
# based upon  Tony DiCola's artikel over MicroPython Hardware - SSD1306 OLED display
#
# Pre-conditions
#    * micropython v1.8.5 en hoger, het moet module importeren ondersteunen
#    * ssd1306.mpy op de ESP8266
# Bron: https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display/
#
# NB. Micropython workshop op WeMOS R1 Mini ESP8266 
#     http://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/setup.html
#
# 2017-0101 PePo - updated I2C constructor (version 1.8.6 - 2017-0101)
# 2016-1022 PePo - het werkt op een WeMOS R1 mini (v1) met OLED shield
# ----------------------
#2017_0101: import machine
from machine import Pin, I2C
import ssd1306
import time

# 2017_01010 updated I2C constructor
# i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2c.scan()   #[60]
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# several examples ..
def whiteScreen():
    oled.fill(1)
    oled.show()

def blackScreen():
    oled.fill(0)
    oled.show()

# 4 pixels ON in the corners
def pixelsInCorner():
    oled.pixel(0,0,1)
    oled.pixel(63,47,1)
    oled.pixel(63,0,1)
    oled.pixel(0,47,1)
    oled.show()
#pixelsInCorner()

def HelloWorld():
    oled.text('Hello', 0, 0)
    oled.text('World', 0, 10)
    oled.show()

def displayT(t):
    oled.text('T: {0}'.format(t),0,20)
    oled.show()
try:
    while(True):
        for i in range(100):
            blankScreen()
            displayT(t)
            time.sleep(1)
except:
    oled.text("done!", 7,0)


