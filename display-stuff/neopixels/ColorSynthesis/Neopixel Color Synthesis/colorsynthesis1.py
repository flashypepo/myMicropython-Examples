# Micro/CircuitPython NeoPixel Color Synthesis Experiments pt. 1
import machine
import time
import math
import neopixel

NEOPIXEL_PIN   = machine.Pin(15, machine.Pin.OUT)
NEOPIXEL_COUNT = 8 * 4 #12

def seconds():
    return time.ticks_ms()/1000  # MicroPython code for current seconds

# Setup NeoPixels
pixels = neopixel.NeoPixel(NEOPIXEL_PIN, NEOPIXEL_COUNT)

def blank():
    pixels.fill((0,0,0))
    pixels.write()
blank()

''' Example 2:
amplitude = 128
frequency = 0.25  # Increase this to speed up, decrease to slow down the pulse.
phase     = 0
offset    = 128
try:
    while True:
        red = int(amplitude*math.sin(2*math.pi*frequency*seconds()+phase)+\
              offset)
        color = (red, 0, 0)
        pixels.fill(color)
        pixels.write()
        print("r={}\tg={}\tb={}".format(*color))
        time.sleep(0.1)
except:
    blank()
    print('done')
#'''

################################################################################
# Example 3:
# Refactor to a functional style.  Create a sine wave function on the fly
# so it's easy to add more animations (just make more sine wave functions).
################################################################################
def sine_wave(amplitude, frequency, phase, offset):
    return lambda t: amplitude*math.sin(2*math.pi*frequency*t+phase)+offset

red_wave = sine_wave(128, 0.25, 0, 128)
green_wave = sine_wave(128, 0.25, math.pi, 128)
try:
    while True:
        current = seconds()
        red = int(red_wave(current))
        green = int(green_wave(current))
        color = (red, green, 0)
        pixels.fill(color)
        pixels.write()
        print("r={}\tg={}\tb={}".format(*color))
        time.sleep(0.1)
except:
    blank()
    print('done')
