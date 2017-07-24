# LED Matrix message scroller demo.
# 2017_0206 PePo adopted for NeoPixel featherwing (GPIO15)
#  ERROR: characters are not displayed correctly (garbage). 
#         WIDTH/HEIGHT mixed up????
#
# This is currently written for the ESP8266 MicroPython port, a Feather HUZZAH ESP8266, and 16x8 LED Matrix FeatherWing.  Adjust the I2C initialization at the bottom if you are using
# a different ESP8266 board with alternate wiring.
# Note this _requires_ version 1.8.6 or higher as the ticks_diff function changed!
# Author: Tony DiCola
# License: MIT (https://opensource.org/licenses/MIT)
import bitmapfont
import neopixel #ht16k33_matrix
import machine
import utime


# Configuration:
#MESSAGE        = 'micropython rocks!'
#MESSAGE        = '1 2 3 4 5 6 7 8 9 0'
MESSAGE        = 'Ada! 1234567890'
DISPLAY_WIDTH  = 8      # Display width in pixels.
DISPLAY_HEIGHT = 4      # Display height in pixels.
SPEED          = 700.0 #25.0    # Scroll speed in pixels per second.
MAX_BRIGHT     = 15 # added maximum brightness
DIN_PIN        = 15 # added GPIO15

#def main(i2c):
def main():
    # Initialize LED matrix.
    matrix = neopixel.NeoPixel(machine.Pin(DIN_PIN, machine.Pin.OUT), DISPLAY_WIDTH * DISPLAY_HEIGHT)
    
    # Initialize font renderer using a helper function to 
    # calculate the index in the neopixel-array
    def matrix_pixel(x, y, color):
        #matrix[y * DISPLAY_WIDTH + x] = color
        matrix[y * DISPLAY_HEIGHT + x] = color
        
    with bitmapfont.BitmapFont(DISPLAY_HEIGHT, DISPLAY_WIDTH, matrix_pixel) as bf:
        bf.init()
        # Global state:
        pos = DISPLAY_WIDTH     # X position of the message start.
        message_width = bf.width(MESSAGE)   # Message width in pixels.
        last = utime.ticks_ms()             # Last frame millisecond tick time.
        speed_ms = SPEED / 1000.0           # Scroll speed in pixels/ms.

        # Main loop:
        while True:
            # Compute the time delta in milliseconds since the last frame.
            current = utime.ticks_ms()
            delta_ms = utime.ticks_diff(current, last)
            last = current
            # Compute position using speed and time delta.
            pos -= speed_ms*delta_ms
            if pos < -message_width:
                pos = DISPLAY_WIDTH
            # Clear the matrix and draw the text at the current position.
            matrix.fill((0,0,0))
            bf.text(MESSAGE, int(pos), 0, 
                    (MAX_BRIGHT, 0, MAX_BRIGHT)) # added color
            # Update the matrix LEDs.
            matrix.write()
            # Sleep a bit to give USB mass storage some processing time (quirk
            # of SAMD21 firmware right now).
            utime.sleep_ms(20)


main()
#i2c = machine.I2C(machine.Pin(5), machine.Pin(4))
#main(i2c)
