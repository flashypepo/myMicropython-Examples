# demo of temperature-controlled neopixel ring
# 2017-0813 PePo - extracted from tutorial Tony D!, youtube
#  TMP36 instead of humidity
#
# Configuration:
# TMP36 is direct connected to ADC-port of Huzzah
# 8-neopixel stick is direct connected to pin 16 of Huzzah
# neopixelstick is powered from USB-port (which is 5V?!)
# TMP36 is powered from 3.3V (Huzzah)

from micropython import const
#import dht
import machine
import neopixel
import time

# h/w configuration
__NEOPIXEL_PIN = const(15)
__NUMBER_OF_PIXELS = const(8) #neopixel-stick
__TMP_PIN = const(0) # ADC ESP8266 must be 0
#__DHT_PIN = const(13)
__MAX_BRIGHTNESS = const(50)

np = neopixel.NeoPixel(machine.Pin(__NEOPIXEL_PIN, machine.Pin.OUT), __NUMBER_OF_PIXELS)
# test the pixels
np.fill((0,10,0))
np.write()
time.sleep(1.0)
# blank the pixels
np.fill((0,0,0))
np.write()

#TMP36 sensor
tmp = machine.ADC(__TMP_PIN)
def temp(value):
    return (value - 500)/10.0

# read temperature, map it on scale to 40 i.e. enlarge the differences to see color differences
# 15 < t < 35: t - 15 -> scale 0 - 20
try:
    while True:
        temp_celsius = temp(tmp.read())
        t = temp_celsius - 15.0 #scale down
        print('T= {0:0.2f} C, t={1:0.2f}'.format(temp_celsius, t))
        # convert humidity to color
        red = (t/20.0) * __MAX_BRIGHTNESS
        blue = ((20.0 - temp_celsius)/100.0) * __MAX_BRIGHTNESS
        np.fill((int(red), 0, int(blue)))
        np.write()
        time.sleep(2.0)
except OSError:
    pass
except:
    print('done')
