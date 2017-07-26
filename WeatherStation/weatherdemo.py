# demo to show Weather from OpenWeather on 8*8 ledmatrix
# 2017-0722 PePo, https://hackaday.io/project/20839-weather-pal
import busio
import board
import time
import urandom

from adafruit_ht16k33 import matrix

# ICON images
from weathericons import ICONS
from digiticons import DIGITS

# specify matrices 'lefteye' and 'righteye'
i2c = busio.I2C(board.SCL, board.SDA)
lefteye = matrix.Matrix8x8(i2c, address=0x70)
righteye = matrix.Matrix8x8(i2c, address=0x71)

# clear matrix 
def clear(matrix):
    matrix.fill(0)
    matrix.show()

# show 'image' on 'matrix' starting (0,0)
def show(matrix, image, dx=0, dy=0):
    ''' show(matrix, image, dx=0, dy=0)'''
    for y , row in enumerate(image):
        bit = 1
        for x in range(8):
            matrix.pixel(dx+x, dy+y, row & bit)
            bit <<= 1
    matrix.show()

# show on matrix 'text'
def show_text(matrix, text):
    x = 0
    for c in reversed(text):
        if c in '.:-':
            show(matrix, DIGITS.get(c, DIGITS[' ']), x - 1, 1)
        else:
            show(matrix, DIGITS.get(c, DIGITS[' ']), x, 1)
            x += 4

''' TODO with ESP-device with WiFi!
def get_weather():
    r = urequests.get("http://api.openweathermap.org/data/2.5/weather"
                      "?q=%s&appid=%s" % (CITY, API_KEY)).json()
    return r["weather"][0]["icon"], int(r["main"]["temp"] - 273.15)
'''
wait = 0
brightness = 1
while True:
    if wait <= 0:
        clear(lefteye)
        clear(righteye)
        #icon, temp = get_weather()
        temp = float(urandom.randrange(100))#25.3
        print('T:{0}'.format(temp))
        wait = 10 #60
    #if icon[-1] == 'd':
        brightness = 9
    else:
        brightness = 2

    lefteye.brightness(brightness)
    righteye.brightness(brightness)

    show_text(lefteye, '%2d' % temp)
    #time.sleep(4)
    #show(righteye, ICONS[icon[:2]])
    show(righteye, ICONS['fog'])

    time.sleep(1) #(4)
    wait -= 1
