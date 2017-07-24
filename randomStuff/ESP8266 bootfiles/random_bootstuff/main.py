# main.py
# 2017-0425 test various things

# blink LED on Pin D13 several times...
from machine import Pin
from time import sleep

# TEST 1 - blinking LED on Pin 13
def blinking(pin, maxCount, delay):
    for i in range(maxCount):
        pin.value(True)      # pin HIGH
        sleep(delay)         # wait
        pin.value(False)     # pin LOW
        sleep(delay)         # wait

led = Pin(13, Pin.OUT)
blinking(led, 10, 0.25)
print("blinking LED done")

# TEST 2 - scan I2C
# define i2c on the ESP32: GPIO21 (SCL) and GPIO22 (SDA)
from machine import I2C
i2c = I2C(scl=Pin(21), sda=Pin(22))
print("I2C addresses = ", i2c.scan())

# TEST 3 - OLED display on I2C
# 2017-0425: ssd1306 driver is baked into micropython
import ssd1306

DISPLAY_WIDTH  = 128  # Width of display in pixels.
DISPLAY_HEIGHT = 32   # Height of display in pixels.

#oled = SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)
oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)

# white-screen
def white_screen():
    oled.fill(1)
    oled.show()

# black sccreen
def black_screen():
    oled.fill(0)
    oled.show()

import time

black_screen()
time.sleep(1.0)
white_screen()
time.sleep(1.0)

def showMaxLines():
    n = DISPLAY_HEIGHT // 8
    for i in range(n):
        oled.text('regel: {0}'.format(i+1),0,i*8)
        oled.show()

black_screen() # restart with blank oleD
showMaxLines()
time.sleep(3.0)

def showMessage(msg):
    oled.text(msg[0], 10, 10) #text
    oled.text(msg[1], 10, 20) #text
    oled.pixel(0,0,1) # 4 pixels in corners
    oled.pixel(DISPLAY_WIDTH-1,DISPLAY_HEIGHT-1,1)
    oled.pixel(DISPLAY_WIDTH-1,0,1)
    oled.pixel(0,DISPLAY_HEIGHT-1,1)
    oled.show() # display all

black_screen() # restart with blank oled
showMessage(["Hello", "Peter"])
time.sleep(3.0)

# TEST 4 - ticket scroller on OLED display
# ticket-text scroller
# pre-condition: oled-object is created and several constants are defined 

import math

# Other configuration:
FONT_WIDTH     = 8    # Width of font characters in pixels.
FONT_HEIGHT    = 8    # Height of the font characters in pixels.
#ORG: AMPLITUDE = 0.3*(DISPLAY_HEIGHT - FONT_HEIGHT)  # Amplitude of sine wave, in pixels.
AMPLITUDE      = 0.5*(DISPLAY_HEIGHT - FONT_HEIGHT)  # Amplitude of sine wave, in pixels.
FREQUENCY      = 2    #5 Sine wave frequency, how often it repeats across screen.
OFFSET_Y       = int(0.5*DISPLAY_HEIGHT)-FONT_HEIGHT #PePo: added offset in Y

def scroller(message="Hello Peter!"):
    pos = DISPLAY_WIDTH  # X position of the starting character in the message.
    message_len_px = len(message) * FONT_WIDTH  # Pixel width of the message.
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
    #while True: # 2017_0423 seems to crash ???
    for k in range(290):
        # Clear the screen.
        oled.fill(0)
        # Move left a bit, then check if the entire message has scrolled past
        # and start over from far right.
        pos -= 1
        if pos <= -message_len_px:
            pos = DISPLAY_WIDTH
        # Go through each character in the message.
        for i in range(len(message)):
            char = message[i]
            char_x = pos + (i * FONT_WIDTH)  # Character's X position on the screen.
            if -FONT_WIDTH <= char_x < DISPLAY_WIDTH:
                # Character is visible, draw it.
                # Look up the Y position in the previously computed lookup table.
                # Remember the lookup table spans from all visible pixels and
                # an extra FONT_WIDTH number of pixels on the left (so offset
                # a bit when indexing into the table).
                oled.text(char, char_x, OFFSET_Y + lookup_y[char_x+FONT_WIDTH])
        oled.show() 

# Run scroller function

# Configure message that will scroll.
MESSAGE = 'MicropPython Rocks!  '

for k in range(5):
    scroller(MESSAGE)
#    scroller() # default message
# scroller(MESSAGE) # message
# time.sleep(1.0)
# clear the screen
# black_screen()
