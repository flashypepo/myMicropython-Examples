# Micro/CircuitPython NeoPixel Color Synthesis Experiments pt. 1
# Author: Tony DiCola
# License: Public Domain
#
# 2017_0522 PePo: downloaded and adopted to MicroPython - not tested yet.
# source: https://gist.github.com/tdicola/f4324c9ae813410182d5ed00e866c8fb
#
# This is like an ipython experiment 'notebook' but instead a raw .py file.
# There are 6 commented example blocks below, uncomment _one_ block at a time
# to run it.  You're meant to go through example by example to see the
# progression from the start to the 'final' state.  Comment out an example
# after you're done running it before moving on to uncomment and run the next
# example!
#
# You'll need a strip of NeoPixels connected to your hardware:
#  - Pixel power line connected to 5V or 3.7V lipo battery (VBAT on Feathers).
#    NOTE: If you use 5V power your pixels may or may not light up depending
#    on if your board's IO output is a high enough voltage to drive the pixels.
#    You can use a power diode to drop the pixel voltage down to a level that
#    makes them 'see' the board IO (see pixels on Raspberry Pi:
#    https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring) or a level
#    shifter to raise board IO voltage up to 5V.
#  - Pixel ground to board ground.
#  - Pixel data in to a board digital IO.
#
# In addition for CircuitPython you'll need neopixel.mpy from the latest release
# here: https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/releases
# to your board's root filesystem.
#
# MicroPython boards besides the ESP8266 will need to have neopixel support
# built in.
#
# Modify the sections below that note the board/pin specific configs and
# MicroPython / CircuitPython specific configs.

# Necessary imports:
import math
import time

# Uncomment only _one_ of the sections below:

# This section is for CircuitPython, change to your pin & NeoPixel count:
# import board
# import nativeio
# NEOPIXEL_PIN   = board.D6
# NEOPIXEL_COUNT = 12
# def seconds():
#     return time.monotonic()  # CircuitPython function for current seconds.

# This section is for MicroPython, change to your pin & NeoPixel count:
import machine
import utime
NEOPIXEL_PIN   = machine.Pin(6, machine.Pin.OUT)
NEOPIXEL_COUNT = 12
def seconds():
    return utime.ticks_ms()/1000  # MicroPython code for current seconds

# Setup NeoPixels:
import neopixel
pixels = neopixel.NeoPixel(NEOPIXEL_PIN, NEOPIXEL_COUNT)
pixels.fill((0,0,0))
pixels.write()


################################################################################
# Example 1:
# Animating red pulse with a fixed equation.
# Fast and direct but hard to modify, you need to understand all the variables
# in the sine wave equation.
################################################################################
# while True:
#     red = int(128*math.sin(2*math.pi*0.25*seconds())+128)
#     color = (red, 0, 0)
#     pixels.fill(color)
#     pixels.write()
#     print("r={}\tg={}\tb={}".format(*color))
#     time.sleep(0.1)


################################################################################
# Example 2:
# Refactor to add variables that make changing the behavior easier.
# Easier to modify behavior but hard to add more animations (you'll add lots of
# variables).
################################################################################
# amplitude = 128
# frequency = 0.25  # Increase this to speed up, decrease to slow down the pulse.
# phase     = 0
# offset    = 128
# while True:
#     red = int(amplitude*math.sin(2*math.pi*frequency*seconds()+phase)+\
#               offset)
#     color = (red, 0, 0)
#     pixels.fill(color)
#     pixels.write()
#     print("r={}\tg={}\tb={}".format(*color))
#     time.sleep(0.1)


################################################################################
# Example 3:
# Refactor to a functional style.  Create a sine wave function on the fly
# so it's easy to add more animations (just make more sine wave functions).
################################################################################
# def sine_wave(amplitude, frequency, phase, offset):
#     return lambda t: amplitude*math.sin(2*math.pi*frequency*t+phase)+offset
#
# red_wave = sine_wave(128, 0.25, 0, 128)
# green_wave = sine_wave(128, 0.25, math.pi, 128)
# while True:
#     current = seconds()
#     red = int(red_wave(current))
#     green = int(green_wave(current))
#     color = (red, green, 0)
#     pixels.fill(color)
#     pixels.write()
#     print("r={}\tg={}\tb={}".format(*color))
#     time.sleep(0.1)


################################################################################
# Example 4:
# Refactor to a signal class that can convert between the domain of two signals.
# This makes the color changing logic more clear, the sine wave doesn't need to
# know about the range and expected values of a color (0...255).  Instead the
# sine wave signal can be transformed into any required range so it can animate
# color or anything else.
################################################################################
# class Signal:
#
#     def __init__(self, _range=None):
#         self.range = _range
#
#     def __call__(self):
#         raise NotImplementedError('Signal must have a callable implementation!')
#
#     def transform(self, y0, y1):
#         # Transform the current value of this signal to a new value inside the # specified target range (y0...y1).
#         x = self()
#         return y0 + (x-self.range[0])*((y1-y0)/(self.range[1]-self.range[0]))
#
#     def discrete_transform(self, y0, y1):
#         # Transform assuming discrete integer values instead of floats.
#         return int(self.transform(y0, y1))
#
# class SineWave(Signal):
#
#     def __init__(self, time=0.0, amplitude=1.0, frequency=1.0, phase=0.0):
#         super().__init__((-amplitude, amplitude))
#         self.time = time
#         self.amplitude = amplitude
#         self.frequency = frequency
#         self.phase = phase
#
#     def __call__(self):
#         return self.amplitude*math.sin(2*math.pi*self.frequency*self.time + \
#                                        self.phase)
#
# red_wave   = SineWave(frequency=0.25)
# green_wave = SineWave(frequency=0.25, phase=math.pi)
# while True:
#     current = seconds()
#     red_wave.time = current
#     green_wave.time = current
#     red = red_wave.discrete_transform(0, 255)
#     green = green_wave.discrete_transform(0, 255)
#     color = (red, green, 0)
#     pixels.fill(color)
#     pixels.write()
#     print("r={}\tg={}\tb={}".format(*color))
#     time.sleep(0.1)


################################################################################
# Example 5:
# Refactor to allow the sine wave signal to be built from other signals (i.e.
# changing time, frequency, etc. with other signals!).
################################################################################
# class Signal:
#
#     @property
#     def range(self):
#         return None
#
#     def __call__(self):
#         raise NotImplementedError('Signal must have a callable implementation!')
#
#     def transform(self, y0, y1):
#         # Transform the current value of this signal to a new value inside the
#         # specified target range (y0...y1).  If this signal has no bounds/range
#         # then the value is just clamped to the specified range.
#         x = self()
#         if self.range is not None:
#             # This signal has a known range so we can interpolate between it
#             # and the desired target range (y0...y1).
#             return y0 + (x-self.range[0]) * \
#                         ((y1-y0)/(self.range[1]-self.range[0]))
#         else:
#             # No range of values for this signal, can't interpolate so just
#             # clamp to a value inside desired target range.
#             return max(y0, min(y1, x))
#
#     def discrete_transform(self, y0, y1):
#         # Transform assuming discrete integer values instead of floats.
#         return int(self.transform(y0, y1))
#
# class SignalSource:
#
#     def __init__(self, source=None):
#         self.set_source(source)
#
#     def __call__(self):
#         # Get the source signal value and return it when reading this signal
#         # source's value.
#         return self._source()
#
#     def set_source(self, source):
#         # Allow setting this signal source to either another signal (anything
#         # callable) or a static value (for convenience when something is a
#         # fixed value that never changes).
#         if callable(source):
#             # Callable source, save it directly.
#             self._source = source
#         else:
#             # Not callable, assume it's a static value and make a lambda
#             # that's callable to capture and always return it.
#             self._source = lambda: source
#
# class SineWave(Signal):
#
#     def __init__(self, time=0.0, amplitude=1.0, frequency=1.0, phase=0.0):
#         self.time = SignalSource(time)
#         self.amplitude = SignalSource(amplitude)
#         self.frequency = SignalSource(frequency)
#         self.phase = SignalSource(phase)
#
#     @property
#     def range(self):
#         # Since amplitude might be a changing signal, the range of this signal
#         # changes too and must be computed on the fly!  This might not really
#         # be necessary in practice and could be switched back to a
#         # non-SignalSource static value set once at initialization like before.
#         amplitude = self.amplitude()
#         return (-amplitude, amplitude)
#
#     def __call__(self):
#         return self.amplitude() * \
#                math.sin(2*math.pi*self.frequency()*self.time() + self.phase())
#
# class FrameClock(Signal):
#
#     def __init__(self):
#         self.update()
#
#     def update(self):
#         self._current_s = seconds()
#
#     def __call__(self):
#         return self._current_s
#
# clock = FrameClock()
# red_wave   = SineWave(time=clock, frequency=0.25)
# green_wave = SineWave(time=clock, frequency=0.25, phase=math.pi)
# while True:
#     clock.update()
#     red = red_wave.discrete_transform(0, 255)
#     green = green_wave.discrete_transform(0, 255)
#     color = (red, green, 0)
#     pixels.fill(color)
#     pixels.write()
#     print("r={}\tg={}\tb={}".format(*color))
#     time.sleep(0.1)


################################################################################
# Example 6:
# Add a physical control signal, the value of a potentiometer!  Twist a knob
# to change the frequency of one of the color waves.  Notice how little the
# main code has to change, only the addition of a new signal for the ADC value
# and setting the frequency to it instead of a fixed value--everything
# 'just works' as far as the main loops knows!
#
# You'll need a potentiometer wired to your board as follows:
#  - One of the outer (left or right) three pins connected to board ground.
#  - The opposite outer pin connect to board 3.3V or ADC max reference voltage.
#  - The middle pin connected to an analog input.
################################################################################
# class Signal:
#
#     @property
#     def range(self):
#         return None
#
#     def __call__(self):
#         raise NotImplementedError('Signal must have a callable implementation!')
#
#     def transform(self, y0, y1):
#         # Transform the current value of this signal to a new value inside the
#         # specified target range (y0...y1).  If this signal has no bounds/range
#         # then the value is just clamped to the specified range.
#         x = self()
#         if self.range is not None:
#             # This signal has a known range so we can interpolate between it
#             # and the desired target range (y0...y1).
#             return y0 + (x-self.range[0]) * \
#                         ((y1-y0)/(self.range[1]-self.range[0]))
#         else:
#             # No range of values for this signal, can't interpolate so just
#             # clamp to a value inside desired target range.
#             return max(y0, min(y1, x))
#
#     def discrete_transform(self, y0, y1):
#         # Transform assuming discrete integer values instead of floats.
#         return int(self.transform(y0, y1))
#
# class SignalSource:
#
#     def __init__(self, source=None):
#         self.set_source(source)
#
#     def __call__(self):
#         # Get the source signal value and return it when reading this signal
#         # source's value.
#         return self._source()
#
#     def set_source(self, source):
#         # Allow setting this signal source to either another signal (anything
#         # callable) or a static value (for convenience when something is a
#         # fixed value that never changes).
#         if callable(source):
#             # Callable source, save it directly.
#             self._source = source
#         else:
#             # Not callable, assume it's a static value and make a lambda
#             # that's callable to capture and always return it.
#             self._source = lambda: source
#
# class SineWave(Signal):
#
#     def __init__(self, time=0.0, amplitude=1.0, frequency=1.0, phase=0.0):
#         self.time = SignalSource(time)
#         self.amplitude = SignalSource(amplitude)
#         self.frequency = SignalSource(frequency)
#         self.phase = SignalSource(phase)
#
#     @property
#     def range(self):
#         # Since amplitude might be a changing signal, the range of this signal
#         # changes too and must be computed on the fly!  This might not really
#         # be necessary in practice and could be switched back to a
#         # non-SignalSource static value set once at initialization.
#         amplitude = self.amplitude()
#         return (-amplitude, amplitude)
#
#     def __call__(self):
#         return self.amplitude() * \
#                math.sin(2*math.pi*self.frequency()*self.time() + self.phase())
#
# class FrameClock(Signal):
#
#     def __init__(self):
#         self.update()
#
#     def update(self):
#         # Hack below to reduce the impact noisey ADC frequency.  When time
#         # values build up to large number then small frequency variations (like
#         # noise from the ADC/potentiometer) are greatly magnified.  By running
#         # the current seconds through a modulo 60 it will prevent the frame
#         # clock from getting large values while still increasing and wrapping
#         # at the same rate. This will only work for driving repeating signals
#         # like sine waves, etc.
#         self._current_s = seconds() % 60
#
#     def __call__(self):
#         return self._current_s
#
# class ADC(Signal):
#
#     ADC_MAX = 4095   # Set to max value of your board's ADC.
#     ADC_MIN = 0      # Set to min value of your board's ADC.
#
#     def __init__(self, pin, _range=(ADC_MIN, ADC_MAX), readings=3, avg_size=10):
#         self._range = _range
#         # CircuitPython ADC creation:
#         self._analogin = nativeio.AnalogIn(pin)
#         # MicroPython ESP8266 ADC creation:
#         # self._analogin = machine.ADC(pin)
#         self._readings = readings
#         self._avg_size = avg_size
#         self._avg = 0
#
#     @property
#     def range(self):
#         return self._range
#
#     def __call__(self):
#         # Take a number of readings and average them together to smooth out
#         # small local ADC variations.
#         accumulated = 0
#         for i in range(self._readings):
#             # CircuitPython ADC reading:
#             accumulated += (self._analogin.value >> 4)
#             # MicroPython ESP8266 ADC reading:
#             # accumulated += self._analogin.read()
#         reading = accumulated // self._readings
#         # Compute running average to smooth out larger ADC variations (i.e.
#         # low pass filter).
#         self._avg -= self._avg / self._avg_size
#         self._avg += reading / self._avg_size
#         return int(self._avg)
#
# class TransformedSignal(Signal):
#
#     def __init__(self, source_signal, y0, y1, discrete=False):
#         self.source = source_signal
#         self.y0 = y0
#         self.y1 = y1
#         if not discrete:
#             self._transform = self.source.transform
#         else:
#             self._transform = self.source.discrete_transform
#
#     @property
#     def range(self):
#         return (y0, y1)
#
#     def __call__(self):
#         return self._transform(self.y0, self.y1)
#
#
# # CircuitPython ADC selection:
# ADC_PIN = board.A0
# # MicroPython ESP8266 ADC selection:
# # ADC_PIN = 0
# clock = FrameClock()
# frequency = TransformedSignal(ADC(ADC_PIN),
#                               0.1,
#                               0.5)
# red_wave   = TransformedSignal(SineWave(time=clock,
#                                         frequency=frequency),
#                                0,
#                                255,
#                                discrete=True)
# green_wave = TransformedSignal(SineWave(time=clock,
#                                         frequency=frequency,
#                                         phase=math.pi),
#                                0,
#                                255,
#                                discrete=True)
# while True:
#     clock.update()
#     color = (red_wave(), green_wave(), 0)
#     pixels.fill(color)
#     pixels.write()
#     print("freq={}\tr={}\tg={}\tb={}".format(frequency(), *color))
#     time.sleep(0.1)

