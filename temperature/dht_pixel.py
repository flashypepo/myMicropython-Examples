# demo of humidity-controlled neopixel ring
# 2017-0813 PePo - extracted from tutorial Tony D!, youtube
#  typed code from screenshot, some adaptions, NOT-TESTED!
#
# Configuration:
# DHT22 is direct connected to port 13 of Huzzah
# 16-neopixelring is direct connected to pin 16 of Huzzah
# both devices are powered from USB-port (which is 5V?!)

# 2017-0813 Pepo NOT WORKING: crashed with TIMEOUT after sensor.measure()

from micropython import const
import dht
import machine
import neopixel
import time

# h/w configuration
__NEOPIXEL_PIN = const(15)
__NUMBER_OF_PIXELS = const(8) #neopixel-stick
__DHT_PIN = const(13)
__MAX_BRIGHTNESS = const(255)

np = neopixel.NeoPixel(machine.Pin(__NEOPIXEL_PIN, machine.Pin.OUT), __NUMBER_OF_PIXELS)
# test the pixels
np.fill((0,10,0))
np.write()
time.sleep(1.0)
# blank the pixels
np.fill((0,0,0))
np.write()

#DHT22 sensor
sensor = dht.DHT22(machine.Pin(__DHT_PIN))

while True:
    try:
        sensor.measure()
        humidity = sensor.humidity()
        #TODO: temperature = sensor.temperature()
        print('Humidity: {0:0.2f}'.format(humidity))
        # convert humidity to color
        red = (humidity/100.0) * __MAX_BRIGHTNESS
        blue = ((100.0-humidity)/100.0) * __MAX_BRIGHTNESS
        np.fill((int(red), 0, int(blue)))
        np.write()
        time.sleep(1.0)
    except OSError:
        pass
