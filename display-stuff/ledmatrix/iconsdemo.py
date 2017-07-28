# demo to show icons in 8*8 ledmatrix
# 2017-0721 PePo, https://hackaday.io/project/20839-weather-pal

''' circuitpython
import busio
import board
i2c = busio.I2C(board.SCL, board.SDA)
from adafruit_ht16k33 import matrix
#'''
#''' micropython
import machine as busio
import machine
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
import ht16k33_matrix as matrix
#'''
import time

# ICON images
from icons import ICONS

# specify matrices 'lefteye' and 'righteye'
lefteye = matrix.Matrix8x8(i2c, address=0x70)
righteye = matrix.Matrix8x8(i2c, address=0x71)

# show 'image' on 'matrix' starting (0,0)
def show(matrix, image, dx=0, dy=0):
    ''' show(matrix, image, dx=0, dy=0)'''
    for y , row in enumerate(image):
        bit = 1
        for x in range(8):
            matrix.pixel(dx+x, dy+y, row & bit)
            bit <<= 1
    matrix.show()

# clear matrix 
def clear(matrix):
    matrix.fill(0)
    matrix.show()

# show icons
# pre-condition: ICONS
def demo(dt=1.0, brightness=1):
    lefteye.brightness(brightness)
    righteye.brightness(brightness)

    show(lefteye, ICONS['01'],0,0)
    show(righteye, ICONS['02'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['03'],0,0)
    show(righteye, ICONS['04'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['09'],0,0)
    show(righteye, ICONS['10'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['11'],0,0)
    show(righteye, ICONS['13'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['50'],0,0)
    clear(righteye)
    time.sleep(dt)

    # faces
    show(lefteye, ICONS['60'],0,0)
    show(righteye, ICONS['61'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['62'],0,0)
    clear(righteye)
    time.sleep(dt)

    #cleanup
    clear(lefteye)
    clear(righteye)

# run demo
import urandom
try:
    while True:
        # micropython
        b = urandom.getrandbits(3) # 0..8
        # curcuitpython
        #b = urandom.randrange(10) #pickup random value 0..9
        print('brightness:{0}'.format(b))
        demo(1.5, b)
        time.sleep(4)
except:
    print('Demo interrupted')
    clear(lefteye)
    clear(righteye)

print('Demo done')
