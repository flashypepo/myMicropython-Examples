# LED Matrix message scroller demo.
# confirued for LED matrix mini 8*8
# 2017-0522 based upon example of Tony DiCola
#
# Author: Tony DiCola
# License: MIT (https://opensource.org/licenses/MIT)
import bitmapfont
import ht16k33_matrix
import machine
import utime


# Configuration:
MESSAGE        = 'MicroPython rocks!'
DISPLAY_WIDTH  = 8       # Display width in pixels.
DISPLAY_HEIGHT = 8       # Display height in pixels.
SPEED          = 8.0 #25.0    # Scroll speed in pixels per second.


def main(i2c):
    # Initialize LED matrix.
    # 2017_0522 updated by PePo: Matrix8x8
    matrix = ht16k33_matrix.Matrix8x8(i2c)
    # Initialize font renderer using a helper function to flip the Y axis
    # when rendering so the origin is in the upper left.
    def matrix_pixel(x, y):
        matrix.pixel(x, DISPLAY_HEIGHT-1-y, 1)
    with bitmapfont.BitmapFont(DISPLAY_WIDTH, DISPLAY_HEIGHT, matrix_pixel) as bf:
        # Global state:
        pos = DISPLAY_WIDTH                 # X position of the message start.
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
            matrix.fill(0)
            bf.text(MESSAGE, int(pos), 0)
            # Update the matrix LEDs.
            matrix.show()
            # Sleep a bit to give USB mass storage some processing time (quirk
            # of SAMD21 firmware right now).
            utime.sleep_ms(20)


i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4)) # 2017-0522 updated PeP
main(i2c)
