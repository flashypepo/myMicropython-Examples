# oledstest.py - OLED utility functions
# Pre-conditions
#   * OLED: I2C, 128*32 pixels
#    * micropython v1.8.5+ - het moet module importeren ondersteunen
#    * ssd1306.mpy op de ESP8266
#  2017-1027 PePo new for My FeatherWing shield - works!
# ----------------------
from micropython import const
from machine import Pin, I2C
import ssd1306
import time

# 2017_01010 updated I2C constructor
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
i2c = I2C(scl=Pin(5), sda=Pin(4))
print('i2c.scan: ', i2c.scan())   #[60]
__WIDTH = const(128) # screen dimensions
__HEIGHT = const(32)
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

WHITESCREEN = const(0)
HELLOWORLD = const(1)
PIXELSINCORNER = const(2)
TEMPERATURE = const(3)


# start demo
# 2017-1027 state machine
tempCount = 0
MAX_TIME_IN_STATE = const(100)
timeCount = MAX_TIME_IN_STATE

state = WHITESCREEN
def demo():
    global tempCount, state, timeCount

    # check if it's time for state activation or just counting down
    if timeCount < MAX_TIME_IN_STATE:
        timeCount = timeCount - 1
        if timeCount == 0:
            timeCount = MAX_TIME_IN_STATE
        return

    # time to activate a state
    clearScreen()
    timeCount = timeCount - 1
    
    if state == WHITESCREEN:
        whiteScreen()
        state  = HELLOWORLD
        return

    if state == HELLOWORLD:
        #clearScreen()
        display('Hello world!')
        state  = PIXELSINCORNER
        return

    if state == PIXELSINCORNER:
        #clearScreen()
        pixelsInCorner()
        state  = TEMPERATURE
        return

    if state == TEMPERATURE:
        #clearScreen()
        displayT(tempCount + 20)
        tempCount = tempCount + 1
        if tempCount > 4:
            tempCount = 0
            state  = WHITESCREEN
        return

#print("Usage: oledtest.demo()")
''' usage:
try:
    while True:
        demo()
        time.sleep(5.0)
except:
    clearScreen()
    display("Demo done!")
    print('Demo done!')
#'''
