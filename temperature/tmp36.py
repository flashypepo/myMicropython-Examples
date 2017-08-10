'''
class TMP36 temperature  sensor
2017_0810 PePo first version
#'''
from micropython import const
import machine, time

class TMP36:
    #resistor value in voltage divider
    _RESISTOR_REF = const(10)
    # attributes:
    # _value - the raw temperature value from sensor in mV
    # _adc: ADC object corresponding with ADC/A0 pin
    # _threshold: temperature value for warnings

    def __init__(self, adc_pin=0):
        #2017_0810 needed? self._adc_pin = adc__pin
        self._adc = machine.ADC(adc_pin)
        # make sure there is always a temperature value read
        self.read()

    # set threshold for temperature warning
    def threshold(self, threshold=None):
        # no parameter: act as getter
        if threshold is None:
            return self._threshold
        # parameter: act as setter
        self._threshold = threshold

    # returns temperature value in Fahrenheit
    # pre-condition: self_value is not None
    def fahrenheit(self):
        #celsius = temp(self.value)
        return (self.celsius() * 9/5) + 32

    # returns temperature value in Celsius
    # pre-condition: self_value is not None
    def celsius(self):
        return ( self._temp() )

    # returns temperature value in Kelvin
    # Celsius to Kelvin: T(k) = T(c) + 273.15
    # http://www.rapidtables.com/convert/temperature/how-celsius-to-kelvin.htm
    # pre-condition: self_value is not None
    def kelvin(self):
        return self.celsius() + 273.15

    # get the raw sensor value
    def read(self):
        self._value = self._adc.read()
        return self._value

    # calculate temperature (celsius) from voltage value (mV)
    def _temp(self):
        return (self._value - 500) / _RESISTOR_REF #Huzzah
        #NodeMCU: return (self.value) / _RESISTOR_REF

    # demo run reading T, Ctrl-C to abort
    def demo(self, threshold=30.0, dt=2.0):
        try:
            self.threshold(threshold) # for temperature warnings
            print('class TMP36 demo, threshold={0:0.1f}'.format(self._threshold))
            # start reading and displaying temperature
            while True:
                #self.read() must be called everytime to get a temperature
                reading = self.read()
                celsius_temp = self.celsius()
                fahrenheit_temp = self.fahrenheit()
                kelvin_temp = self.kelvin()
                print('TMP36 reading {0:0.1f}\tCelsius {1:0.1f}\tFahrenheit {2:0.1f}\tKelvin {3:0.1f}'.format(reading, celsius_temp, fahrenheit_temp, kelvin_temp))
                if celsius_temp > self._threshold:
                    print('T>{0:0.1f}: alert on'.format(self._threshold))
                time.sleep(dt) #wait > s, see datasheet
        except:
            print('Interrupted, done!')

'''
# demo of TMP36
try:
    sensor = tmp36.TMP36(adc_pin=0)
    sensor.demo()
except:
    print('Interrupted, done!')

# usage of class tmp36
import tmp36
try:
    print('class TMP36 demo')
    sensor = tmp36.TMP36(adc_pin=0)
    sensor.threshold(26.0)
    while True:
        #sensor.read() must be called everytime to get a temperature
        reading = sensor.read()
        celsius_temp = sensor.celsius()
        fahrenheit_temp = sensor.fahrenheit()
        print('TMP36 reading {}\tDegrees Celsius {}\tDegrees Fahrenheit {}'.format(reading, celsius_temp, fahrenheit_temp))
        if celsius_temp > sensor.threshold():
            print('T>{0:0.1f}: alert on'.format(sensor.threshold())
        time.sleep(2.5) #wait > s, see datasheet: dt > 2 sec
except:
    print('Interrupted, done!')

'''
