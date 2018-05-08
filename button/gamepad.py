# readbuttons from gamepad (tindie.com)
# Wemos D1 mini Lite, uP 1.9.3. Tested also on Loboris uP.
# 2018-0428 PePo Wemos D1 mini (ESP8266EX)
# 2018-0427 PePo ESP32 D1 minikit
# 2018-0415 PePo WeMOS D1 mini test from https://hackaday.io/project/19371/logs

#''' if not i2c
from micropython import const
from machine import Pin, I2C
import time
#'''

# setup for I2C
''' ESP32 D1 minikit: SCL = 22, SDA = 21
SCL = const(22)
SDA = const(21)
#i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
#'''

#''' WeMOS D1 / Lite mini
SCL = const(5)
SDA = const(4)
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
#'''

i2c = I2C(scl=Pin(SCL), sda=Pin(SDA))
print('i2c.scan:', i2c.scan())   #[56]

def readbuttons():
    while True:
        print(hex(i2c.readfrom(56, 1)[0]))
        #print(hex(wemos_oled.i2c.readfrom(56, 1)[0]))
        time.sleep(1)

#help info
print("usage: {0}.readbuttons()".format(__name__))
