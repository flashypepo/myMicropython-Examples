# NeoPixel Matrix message scroller
# 2016-1219 PePo new
#    BUG: characters(?) and wrapping around are not displayed correctly!
#
# based upon: LED Matrix message scroller demo, which was written for
# the ESP8266 MicroPython port, a Feather HUZZAH ESP8266, and 16x8 LED Matrix FeatherWing.  
# Note this _requires_ version 1.8.6 or higher as the ticks_diff function changed!
# Author: Tony DiCola
# License: MIT (https://opensource.org/licenses/MIT)
import bitmapfont
import neopixel
import machine
import utime

# Configuration:
MESSAGE        = '12345'
DISPLAY_WIDTH  = 8      # Display width in pixels.
DISPLAY_HEIGHT = 8      # Display height in pixels.
INTENSITY      = 16    # Message pixel brightness (0-255).
SPEED          = 5      # Scroll speed in pixels per second.

def main():
    # Initialize NeoPixel 8*8 matrix.
    matrix = neopixel.NeoPixel(machine.Pin(13, machine.Pin.OUT), 64)
    matrix.fill((0,0,0)) # PePo changed
    matrix.write();
    
    # define the pixel function, which has to convert a 2-dimensional 
    # X, Y location into a 1-dimensional location in the NeoPixel array...
    def matrix_pixel(x, y, color):
        matrix[y*DISPLAY_HEIGHT + x - 1] = color
        
    with bitmapfont.BitmapFont(DISPLAY_WIDTH, DISPLAY_HEIGHT, matrix_pixel) as bf:
        # Global state:
        pos = DISPLAY_WIDTH                 # X position of the message start.
        message_width = bf.width(MESSAGE)   # Message width in pixels.
        #print('MESSAGE is {} pixels wide.'.format(message_width)) #PePo added - debugging
        last = utime.ticks_ms()             # Last frame millisecond tick time.
        speed_ms = SPEED / 1000.0           # Scroll speed in pixels/ms. WAS: 1000
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
            matrix.fill((0,0,0)) # PePo changed
            utime.sleep_ms(20) #PePo added - not much improvement
            bf.text(MESSAGE, int(pos), 0, (INTENSITY, 0, 0)) #PePo changed: added color
            # Update the matrix.
            matrix.write() #PePo changed was: matrix.show()
            # Sleep a bit to give USB mass storage some processing time (quirk
            # of SAMD21 firmware right now).
            utime.sleep_ms(20)

main()
