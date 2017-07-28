# Example of OLED demo in MicroPython
# History:
# 2017-0522 PePo combined from demo_oled.py and smileys.py
# License: Public Domain

########################################################################
# Setup code goes below, this is called once at the start of the program: #
########################################################################
from machine import Pin, I2C
# Import OLED SSD1306 driver
import ssd1306
# Import the HT16K33 LED matrix module.
import ht16k33_matrix as matrix
import time
import math

# 2017_0422 PePo: dimension I2C OLED shield
DISPLAY_WIDTH  = 128  # Width of display in pixels.
DISPLAY_HEIGHT = 32   # Height of display in pixels.

# I2C construction...
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

# demo smileys
def demo_smileys(p1, p2):
    # show faces
    dp(lefteye, p1)
    dp(righteye, p2)
    # play with it...
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

# demos mini 8x8 matrices
lefteye.brightness(1) # low intensity (0..15)
righteye.brightness(1)
dp(lefteye, smile)
dp(righteye, sad)

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
#print('usage: demo_smileys(happy, smile)')
#print('usage: scroller(i2c)')
#showmessage(['usage:', 'scroller(i2c)'])

demo_smileys(happy, smile)
scroller(i2c)
