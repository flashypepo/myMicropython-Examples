# demo of light-controlled neopixel ring
# 2017-0813 PePo - extracted from tutorial Tony D!, youtube
#  LDR instead of humidity
#
# Configuration:
# LDR is connected via voltage-divider to ADC-port of Huzzah
# 8-neopixel stick is direct connected to pin 16 of Huzzah
# neopixelstick is powered from USB-port (which is 5V?!)
# LDR is powered from 3.3V (Huzzah)

from micropython import const
import machine
import neopixel
import time

# h/w configuration
__NEOPIXEL_PIN = const(15)
__NUMBER_OF_PIXELS = const(8) #neopixel-stick
__ADC_CHANNEL = const(0) # ADC ESP8266 must be 0
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
ldr = machine.ADC(__ADC_CHANNEL)
def light(value):
    return (value - 500)/10.0

# read LDR, map it on scale to 40 i.e. enlarge the differences to see color differences
# 15 < t < 35: t - 15 -> scale 0 - 20
_SCALE = 10.0
_MAX_SCALE = 40.0

try:
    while True:
        light_value = light(ldr.read())
        l = max((light_value - _SCALE), 0) #scale down
        print('L= {0:0.2f}, l={1:0.2f}'.format(light_value, l))
        # convert humidity to color
        red = (l/_MAX_SCALE) * __MAX_BRIGHTNESS
        blue = ((_MAX_SCALE - l)/100.0) * __MAX_BRIGHTNESS
        np.fill((int(red), 0, int(blue)))
        np.write()
        time.sleep(2.0)
except OSError:
    pass
except:
    print('done')
