# ##########################################################
# OLED scroller
# 2017_0422 PePo adopted for ESP32 micropython
#      based upon code from Tony DiCola / Adafruit
# ##########################################################

from machine import Pin, I2C
import ssd1306
import time
import math

DISPLAY_WIDTH  = 128  # Width of display in pixels.
DISPLAY_HEIGHT = 32   # Height of display in pixels.

# make i2c
i2c = I2C(scl=Pin(21), sda=Pin(22))
#print(i2c.scan())

# make OLED-display object
oled = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2c)
# blank oled
oled.fill(0) 
oled.show()

# Configure message that will scroll.
#MESSAGE = 'Hello world this is a fun scroller!'
#MESSAGE = 'MicroPython funny  scroller!'
MESSAGE = 'MicropPython Rocks!  '

# Other configuration:
FONT_WIDTH     = 8    # Width of font characters in pixels.
FONT_HEIGHT    = 8    # Height of the font characters in pixels.
#ORG: AMPLITUDE      = 0.3*(DISPLAY_HEIGHT - FONT_HEIGHT)  # Amplitude of sine wave, in pixels.
AMPLITUDE      = 0.5*(DISPLAY_HEIGHT - FONT_HEIGHT)  # Amplitude of sine wave, in pixels.
FREQUENCY      = 2    #5 Sine wave frequency, how often it repeats across screen.
OFFSET_Y       = int(0.5*DISPLAY_HEIGHT)-FONT_HEIGHT #PePo: added offset in Y

def scroller():
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
    #while True:
    for k in range(32000):
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
    oled.fill(0)
    oled.show()

###################################################################
# Loop code goes inside the loop here, this is called repeatedly: #
###################################################################
# 3. Run scroller function
scroller()
