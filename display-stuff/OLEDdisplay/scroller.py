# SSD1306 Sine Wave Message scroller
# This animates a message scrolling across a SSD1306 display in a sine wave.
# Currently written for SAMD21 MicroPython, but adjust how the I2C bus is
# defined to work with other ports.
# Updated 2016_1023 PePo: dimension WeMOS OLED shield, ESP8266
# Author: Tony DiCola
# License: Public Domain
import machine
import math
import ssd1306
import time

# Configure message that will scroll.
#MESSAGE = 'Hello world this is a fun scroller!'
#MESSAGE = 'MicroPython  funny  scroller!'
MESSAGE = 'Welkom  Peter..........'

# Other configuration:
# 2016_1023 PePo: dimension WeMOS OLED shield
#DISPLAY_WIDTH  = 128  # Width of display in pixels.
#DISPLAY_HEIGHT = 32   # Height of display in pixels.
DISPLAY_WIDTH  = 64  # Width of display in pixels.
DISPLAY_HEIGHT = 48   # Height of display in pixels.
FONT_WIDTH     = 8    # Width of font characters in pixels.
FONT_HEIGHT    = 8    # Height of the font characters in pixels.
AMPLITUDE      = 0.3*(DISPLAY_HEIGHT - FONT_HEIGHT)  # Amplitude of sine wave, in pixels.
FREQUENCY      = 5    # Sine wave frequency, how often it repeats across screen.
OFFSET_Y       = int(0.5*DISPLAY_HEIGHT)-FONT_HEIGHT #PePo: added offset in Y

def main(i2c):
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

# Run main function but first initialize I2C (with context manager to deinit).
# 2016-1023 PePo: probably only for SAM-ESP8266
#with machine.I2C(machine.Pin('SCL'), machine.Pin('SDA')) as i2c:
#    main(i2c)
# 2016-1023 PePo: ESP8266 type controllers, like WeMOS R1 Mini
i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
main(i2c)
