''' TMP36 temperature  sensor
  pin TMP36   NodeMCU  Huzzah ESP8266
  data-out    A0       ADC
  Vs          3.3V       3.3V
  GND         GND        GND
#'''

import machine, time
# using from machine import ADC is bad practice

# calculate temperature (celsius) from voltage value (mV)
def temp(value):
	#NOT_VALID?
    return (value - 500) / 10 #Huzzah
	#NodeMCU: return (value) / 10

# Celsius to Fahrenheit
def fahrenheit(celsius):
    return (celsius * 9/5) + 32

_ADC_PIN = 0
_WARNING_LED_PIN = 4
_RELAY_PIN = 5

# program
# read voltage (mV)
adc = machine.ADC(_ADC_PIN)
#TEST: print('ADC reading:', adc.read())
alert = machine.Pin(_WARNING_LED_PIN, machine.Pin.OUT)
relais = machine.Pin(_RELAY_PIN, machine.Pin.OUT)

# alert ON and OFF
def alertOn():
    alert.on()
    relais.on()

def alertOff():
    alert.off()
    relais.off()

# run readng T, Ctrl-C to abort
def run(dt=2.0):
    try:
        while True:
            reading = adc.read()
            celsius_temp = temp(reading)
            fahrenheit_temp = fahrenheit(celsius_temp)
            print('TMP36 reading {}\tDegrees Celsius {}\tDegrees Fahrenheit {}'.format(reading, celsius_temp, fahrenheit_temp))
            if celsius_temp > 26:
                alertOn()
            else:
                alertOff()
            time.sleep(dt) #wait > s, see datasheet
    except:
        print('done')

run()
