from machine import I2C, Pin
from ht16k33_matrix import Matrix8x8
import time as utime
import json
import urequests

API_KEY = "cac77abc97ceafbe446a455019c247fe" #OpenWeather Micropython test
CITY = "Amsterdam,NL"

ICONS = {
    '00': (
        0b00000000,
        0b01000010,
        0b00100100,
        0b00011000,
        0b00011000,
        0b00100100,
        0b01000010,
        0b00000000,
    ),
    '01': (
        0b00010000,
        0b01010010,
        0b00111100,
        0b00111111,
        0b11111100,
        0b00111100,
        0b01001010,
        0b00001000,
    ),
    '02': (
        0b00010000,
        0b01010100,
        0b00111000,
        0b11111110,
        0b01000100,
        0b10000010,
        0b10000001,
        0b01111110,
    ),
    '03': (
        0b00000000,
        0b00000000,
        0b00000000,
        0b00111000,
        0b01000100,
        0b10000010,
        0b10000001,
        0b01111110,
    ),
    '04': (
        0b01100000,
        0b10011000,
        0b10000100,
        0b01111000,
        0b01000100,
        0b10000010,
        0b10000001,
        0b01111110,
    ),
    '09': (
        0b00111100,
        0b01111110,
        0b11111111,
        0b11111111,
        0b10001001,
        0b00001000,
        0b00101000,
        0b00111000,
    ),
    '10': (
        0b00101010,
        0b00011100,
        0b01111111,
        0b00011100,
        0b01111010,
        0b11111100,
        0b00010000,
        0b00110000,
    ),
    '11': (
        0b00001111,
        0b00011110,
        0b00111100,
        0b01111111,
        0b11111110,
        0b00000100,
        0b00001000,
        0b00010000,
    ),
    '13': (
        0b01010010,
        0b11010011,
        0b00111100,
        0b00100111,
        0b11100100,
        0b00111100,
        0b11001011,
        0b01001010,
    ),
    '50': (
        0b11111111,
        0b00000000,
        0b11111111,
        0b00000000,
        0b11111111,
        0b00000000,
        0b11111111,
        0b00000000,
    ),
}
DIGITS = {
    ' ': (
        0b0000,
        0b0000,
        0b0000,
        0b0000,
        0b0000,
    ),
    '0': (
        0b0111,
        0b0101,
        0b0101,
        0b0101,
        0b0111,
    ),
    '1': (
        0b0010,
        0b0010,
        0b0010,
        0b0010,
        0b0010,
    ),
    '2': (
        0b0111,
        0b0001,
        0b0111,
        0b0100,
        0b0111,
    ),
    '3': (
        0b0111,
        0b0001,
        0b0111,
        0b0001,
        0b0111,
    ),
    '4': (
        0b0101,
        0b0101,
        0b0111,
        0b0001,
        0b0001,
    ),
    '5': (
        0b0111,
        0b0100,
        0b0111,
        0b0001,
        0b0111,
    ),
    '6': (
        0b0111,
        0b0100,
        0b0111,
        0b0101,
        0b0111,
    ),
    '7': (
        0b0111,
        0b0001,
        0b0001,
        0b0001,
        0b0001,
    ),
    '8': (
        0b0111,
        0b0101,
        0b0111,
        0b0101,
        0b0111,
    ),
    '9': (
        0b0111,
        0b0101,
        0b0111,
        0b0001,
        0b0001,
    ),
    ':': (
        0b0000,
        0b0001,
        0b0000,
        0b0001,
        0b0000,
    ),
    '.': (
        0b0000,
        0b0000,
        0b0000,
        0b0000,
        0b0001,
    ),
    '-': (
        0b0000,
        0b0000,
        0b0001,
        0b0000,
        0b0000,
    ),
}

i2c = I2C(scl = Pin(5), sda = Pin(4)) #PP changed 2017-1028
matrix = Matrix8x8(i2c, address=0x70) #PP changed 2017-1028
#using default address 8x8 led-matrix

wait = 0

# PePO: show 'image' on 'matrix' starting (0,0)
#OK: def show(matrix, image, dx=0, dy=0):     #PP changed 2017-1028
def show(image, dx=0, dy=0):     #ORG
    global matrix
    for y, row in enumerate(image):
        bit = 1
        for x in range(8):
            matrix.pixel(dx + x, dy + y, row & bit)
            bit <<= 1
    matrix.show()


#'''
# 2017-1028 PePo: funny thing - numbers mirrored
def show_text(text):
    x = 0
    for c in reversed(text):
        if c in '.:-':
            #OK: show(matrix, DIGITS.get(c, DIGITS[' ']), x - 1, 1)  #PP changed 2017-1028
            show(DIGITS.get(c, DIGITS[' ']), x - 1, 1)  #ORG
        else:
            #OK: show(matrix, DIGITS.get(c, DIGITS[' ']), x, 1)  #PP changed 2017-1028
            show(DIGITS.get(c, DIGITS[' ']), x, 1)  #ORG
            x += 4
#'''


def get_weather():
    r = urequests.get("http://api.openweathermap.org/data/2.5/weather"
                      "?q=%s&appid=%s" % (CITY, API_KEY)).json()
    return r["weather"][0]["icon"], int(r["main"]["temp"] - 273.15)


def run():
    wait = 0 #PP added 2017-1028, strange, but it prevents exception

    while True:
        if wait <= 0:
            icon, temp = get_weather()
            wait = 60

        print('wait:', wait)

        if icon[-1] == 'd':
            matrix.brightness(9)
        else:
            matrix.brightness(2)

        matrix.fill(0)
        show_text('%2d' % temp)
        utime.sleep(4)

        show(matrix, ICONS[icon[:2]])
        utime.sleep(4)
        wait -= 1

def runtrycatch():
    try:
        wait = 0 #PP added 2017-1028, strange, but it prevents exception

        while True:
            print('wait:', wait)

            if wait <= 0:
                icon, temp = get_weather()
                wait = 60

            if icon[-1] == 'd':
                matrix.brightness(9)
            else:
                matrix.brightness(2)

            matrix.fill(0)
            show_text('%2d' % temp)
            utime.sleep(4)

            show(ICONS[icon[:2]])
            utime.sleep(4)
            wait -= 1
    except OSError:
        print('OSErrorException')
        pass
        runtrycatch()
    except KeyboardInterrupt:
        print('KeyboardInterrupt...')
        matrix.fill(0)
        show_text(' ')
        print('demo done')
     
