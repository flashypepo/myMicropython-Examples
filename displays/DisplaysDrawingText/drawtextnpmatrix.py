# 2016-1219 draw text on neopixel matrix
# https://learn.adafruit.com/micropython-displays-drawing-text/software

import neopixel
import machine

matrix = neopixel.NeoPixel(machine.Pin(13, machine.Pin.OUT), 64)

# define the pixel function, which has to convert a 2-dimensional 
# X, Y location into a 1-dimensional location in the NeoPixel array...
def matrix_pixel(x, y, color):
    matrix[y*8 + x] = color

# Finally create the font class and pass it the pixel function created above...
import bitmapfont
bf = bitmapfont.BitmapFont(8, 8, matrix_pixel)
bf.init()

# Then draw some text! 
# tuple-color is passed to the pixel function
bf.text('A', 0, 0, (64, 0, 64))
# Peter: I must write the text-buffer to the neopixel matrix!
matrix.write()

width = bf.width('A')
print('A is {} pixels wide.'.format(width))

