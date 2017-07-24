# running light on LED-matrix - Adafruit Huzzah ESP8266
# 2017_0703 Feather Wing Neopixel 8*4 LED matrix
# pre-condition: neopixelmatrix.py present on Huzzah
from neopixelmatrix import *
import time
# define
def run(d, color):
    for i in  range(32):
        np[i] = (color)
        if i > 0:
            np[i-1] = ((0,0,0))
        np.write()
        time.sleep(d)
    off()

#run
import urandom
#import ubinascii
MAX_BRIGHT = 255
for i in range(5):
    r = min ((urandom.getrandbits(6)) % 255, MAX_BRIGHT)
    g = min ((urandom.getrandbits(8)) % 255, MAX_BRIGHT)
    b = min ((urandom.getrandbits(6)) % 255, MAX_BRIGHT) 
    '''
    r = ubinascii.hexlify(uos.urandom(2))
    g = ubinascii.hexlify(uos.urandom(2))
    b = ubinascii.hexlify(uos.urandom(2))
    '''
    print('Color = ({0}, {1}, {2})'.format(r, g, b))
    run(0.1, (r,g,b))
