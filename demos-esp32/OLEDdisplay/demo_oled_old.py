# Example of WeMOS Mini + OLED startup file in MicroPython
# Arduino style: setup and loop
#
# History:
# 2017-0101 PePo I2C constructor is changed (MicroPython v1.8.6-273-g5efd650 on 2017-01-01)
# 2016-1023 PePo added scroller()
# 2016-1022 PePo new
#
# Pre-conditions
# * micropython v1.8.5 en hoger, het moet module importeren ondersteunen
# * ssd1306.mpy op de ESP8266
# Bron: https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display/

# function scroller(i2c): SSD1306 Sine Wave Message scroller
# This animates a message scrolling across a SSD1306 display in a sine wave.
# Updated 2016_1023 PePo: dimension WeMOS OLED shield, ESP8266
# Author: Tony DiCola
# License: Public Domain

########################################################################
# Setup code goes below, this is called once at the start of the program: #
########################################################################
#2017_0101: import machine
from machine import Pin, I2C
import ssd1306
import time
import math

# 2017_0422 PePo: dimension I2C OLED shield
DISPLAY_WIDTH  = 128  # Width of display in pixels.
DISPLAY_HEIGHT = 32   # Height of display in pixels.
# 2016_1023 PePo: dimension WeMOS OLED shield
#DISPLAY_WIDTH  = 64  # Width of display in pixels.
#DISPLAY_HEIGHT = 48   # Height of display in pixels.

# setup WeMOS OLED shield for I2C
# 2017_0101 micropython v1.8.6 version 2017_0101
#    apparently, I2C constructor is changed.
#i2c = machine.I2C(machine.Pin(5), machine.Pin(4))

''' 2017-0522: SCL/SDA port on NodeMCU:
SCL = 5
SDA = 4
'''
#''' SCL/SDA port on LoLin32:
SCL = 22
SDA = 21
#'''
i2c = I2C(scl=Pin(SCL), sda=Pin(SDA), freq=100000)
#i2c.scan()   #[60]
oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)
oled.fill(0) # blank oled
oled.show()

def runingcount():
    n = DISPLAY_HEIGHT // 8
    for i in range(n):
        oled.text('regel: {0}'.format(i),0,i*8)
        oled.show()
    time.sleep(1) # wait 1 sec
    oled.fill(0) # restart with blank oled
    oled.show()

def showmessage(msg):
    oled.text(msg[0], 10, 10) #text
    oled.text(msg[1], 10, 20) #text
    oled.pixel(0,0,1) # 4 pixels in corners
    oled.pixel(DISPLAY_WIDTH-1,DISPLAY_HEIGHT-1,1)
    oled.pixel(DISPLAY_WIDTH-1,0,1)
    oled.pixel(0,DISPLAY_HEIGHT-1,1)
    oled.show() # display all

# Configure message that will scroll.
MESSAGE = 'MicropPython Rocks!  '

# Other configuration:
FONT_WIDTH     = 8    # Width of font characters in pixels.
FONT_HEIGHT    = 8    # Height of the font characters in pixels.
#ORG: AMPLITUDE      = 0.3*(DISPLAY_HEIGHT - FONT_HEIGHT)  # Amplitude of sine wave, in pixels.
AMPLITUDE      = 0.5*(DISPLAY_HEIGHT - FONT_HEIGHT)  # Amplitude of sine wave, in pixels.
FREQUENCY      = 2    #5 Sine wave frequency, how often it repeats across screen.
OFFSET_Y       = int(0.5*DISPLAY_HEIGHT)-FONT_HEIGHT #PePo: added offset in Y

def scroller(i2c):
    # Global state:
    oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)
    pos = DISPLAY_WIDTH  # X position of the starting character in the message.
    message_len_px = len(MESSAGE) * FONT_WIDTH  # Pixel width of the message.
    # Build a lookup table of wavy Y positions for each column.  This will speed
    # up the main loop by not constantly computing Y positions.  Remember characters
    # can be drawn off screen to the left so increase the lookup table a bit to
    # compute their Y positions too.
    lookup_y = [0] * (DISPLAY_WIDTH+FONT_WIDTH)
    for i in range(len(lookup_y)):
        t = i / (DISPLAY_WIDTH-1)  # Compute current 'time' as position along
                                   # lookup table in 0 to 1 range.
        # Use a sine wave that's offset to the range 0 to AMPLITUDE to compute
        # each character Y position at a given X.
        lookup_y[i] = int(((AMPLITUDE/2.0) * math.sin(2.0*math.pi*FREQUENCY*t)) + (AMPLITUDE/2.0))
    # Main loop:
    while True:
        # Clear the screen.
        oled.fill(0)
        # Move left a bit, then check if the entire message has scrolled past
        # and start over from far right.
        pos -= 1
        if pos <= -message_len_px:
            pos = DISPLAY_WIDTH
        # Go through each character in the message.
        for i in range(len(MESSAGE)):
            char = MESSAGE[i]
            char_x = pos + (i * FONT_WIDTH)  # Character's X position on the screen.
            if -FONT_WIDTH <= char_x < DISPLAY_WIDTH:
                # Character is visible, draw it.
                # Look up the Y position in the previously computed lookup table.
                # Remember the lookup table spans from all visible pixels and
                # an extra FONT_WIDTH number of pixels on the left (so offset
                # a bit when indexing into the table).
                oled.text(char, char_x, OFFSET_Y + lookup_y[char_x+FONT_WIDTH])
        oled.show()

# 1. show static text with pixels in corners
showmessage(["Welkom", "Peter"])
time.sleep(2) # wait
oled.fill(0) # blank screen

# 2. show static text with pixels in corners
runingcount()
time.sleep(1) # wait

###################################################################
# Loop code goes inside the loop here, this is called repeatedly: #
###################################################################
# 3. Run scroller function
#scroller(i2c)')
print('usage: scroller(i2c)')
showmessage(['usage:', 'scroller(i2c)'])
