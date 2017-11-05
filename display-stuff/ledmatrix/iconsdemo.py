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
#ORG: import utime
# 2017-1028 PePo added OpenWeatherData
import json
import urequests
API_KEY = "cac77abc97ceafbe446a455019c247fe" #OpenWeather Micropython test
#ORG: CITY = "Zuirich" #TODO
CITY = "Amsterdam,NL"

# ICON images
from icons import ICONS

# specify matrices 'lefteye' and 'righteye'
lefteye = matrix.Matrix8x8(i2c, address=0x70)
#righteye = matrix.Matrix8x8(i2c, address=0x71)

# 2017-1028 PePo added
def show_text(text):
    x = 0
    for c in reversed(text):
        if c in '.:-':
            show(DIGITS.get(c, DIGITS[' ']), x - 1, 1)
        else:
            show(DIGITS.get(c, DIGITS[' ']), x, 1)
            x += 4

# webbrowser working example
# http://api.openweathermap.org/data/2.5/weather?q=Amsterdam,NL&appid=cac77abc97ceafbe446a455019c247fe
def get_weather():
    r = urequests.get("http://api.openweathermap.org/data/2.5/weather"
                      "?q=%s&appid=%s" % (CITY, API_KEY)).json()
    return r["weather"][0]["icon"], int(r["main"]["temp"] - 273.15)

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
def demo(dt=1.0, brightness=5):
    lefteye.brightness(brightness)

    show(lefteye, ICONS['01'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['02'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['03'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['04'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['09'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['10'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['11'],0,0)
    time.sleep(dt)
    show(lefteye, ICONS['13'],0,0)
    time.sleep(dt)

    show(lefteye, ICONS['50'],0,0)
    time.sleep(dt)

    # faces
    show(lefteye, ICONS['62'],0,0)
    time.sleep(dt)
    show(lefteye, ICONS['61'],0,0)
    time.sleep(dt)
    show(lefteye, ICONS['60'],0,0)

def weather():
    icon, temp = get_weather()
    print("icon:{0}, temp:{1}".format(icon, temp))
    
''' usage demo
import urandom
try:
    while True:
        # micropython
        b = urandom.getrandbits(4) # 0..8
        if b > 15:
            b = 15
        # curcuitpython
        #b = urandom.randrange(10) #pickup random value 0..9
        print('brightness:{0}'.format(b))
        demo(1.5, b)
        time.sleep(4)
except:
    print('Demo interrupted')
    clear(lefteye)

print('Demo done')
#'''