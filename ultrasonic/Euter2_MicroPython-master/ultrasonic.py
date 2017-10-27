"""Micropython module for HC-SR04 ultrasonic ranging module."""

''' 2017-1014 PePo adoptions for MP 1.9+, configuration Lolin32 (Rev 0)
deprecated Pin.high() and Pin.low(), replaced by .value()
Usage:
    import time
    import ultrasonic
    hc = ultrasonic.Ultrasonic(12, 14)
    while True:
        dist = hc.distance()
        print('afstand is {0:3.1f} cm'.format(dist*100))
        time.sleep(1)
#'''

from machine import Pin, time_pulse_us
from time import sleep_us

class Ultrasonic:
    """HC-SR04 ultrasonic ranging module class."""
    _dist = 0

    def __init__(self, trig_Pin, echo_Pin):
        """Initialize Input(echo) and Output(trig) Pins."""
        ''' PePO: adopted from jpedrodias:  https://forum.micropython.org/viewtopic.php?t=2436&start=20
        self._trig = trig_Pin
        self._echo = echo_Pin
        #'''
        self._trig = Pin(trig_Pin)
        self._echo = Pin(echo_Pin)
        self._trig.init(Pin.OUT)
        self._echo.init(Pin.IN)
        self._sound_speed = 340  # m/s
        self._dist = 0

    def _pulse(self):
        """Trigger ultrasonic module with 10us pulse."""
        self._trig.value(1)
        sleep_us(10)
        self._trig.value(0)

    def distance(self):
        """Measure pulse length and return calculated distance [m]."""
        self._pulse()
        #PePo: pulse_width_s = time_pulse_us(self._echo, Pin.high) / 1000000
        pulse_width_s = time_pulse_us(self._echo, 1) / 1000000
        self._dist = (pulse_width_s / 2) * self._sound_speed
        return self._dist

    def calibration(self, known_dist_m):
        """Calibrate speed of sound."""
        self._sound_speed = known_dist_m / self.distance() * self._sound_speed
        print("Speed of sound was successfully calibrated! \n" +
              "Current value: " + str(self._sound_speed) + " m/s")

    # 2017-1014 PePo added as helper
    def distance_in_cm(self):
        """return calculated distance [cm]."""
        # 2017-1022 do not measure distance again
        #dist_m = self.distance()
        return self._dist * 100

'''
2017_1014 PePo: volgend werkt in de REPL:

Usage:

import machine
from time import sleep_us

trig = machine.Pin(12)
trig.init(machine.Pin.OUT)

echo = machine.Pin(14)
echo.init(machine.Pin.IN)

def _pulse():
    trig.value(1)
    sleep_us(10)
    trig.value(0)

def distance():
    _pulse()
    pulse_width_s = machine.time_pulse_us(echo, 1) / 1000000
    dist_m = (pulse_width_s / 2) * 340
    return dist_m

# demo
while True:
    dist_cm = distance_in_cm()
    print('afstand in cm: {0:3.1f}'.format(dist_cm))
    time.sleep(1)

# resultaat:
afstand in cm: 18.9
afstand in cm: 18.9
afstand in cm: 18.9
afstand in cm: 18.8
afstand in cm: 16.8
afstand in cm: 19.2
afstand in cm: 7.9
afstand in cm: 8.4
.....

#'''
