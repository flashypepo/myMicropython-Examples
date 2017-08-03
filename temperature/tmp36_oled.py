''' TMP36 temperature  sensor
Let op: verwissel Vs en GND niet van de TMP36!
  pin TMP36   NodeMCU  Huzzah ESP8266
  data-out    A0       ADC
  Vs          3.3V       3.3V
  GND         GND        GND
#'''

import machine, time
import ssd1306

# using from machine import ADC is bad practice

# calculate temperature (celsius) from voltage value (mV)
def temp(value):
    _OFFSET = const(20) #calibration factor, should be 0
    return (value - 500 - _OFFSET) / 10 #Huzzah
	#NodeMCU: return (value) / 10

# Celsius to Fahrenheit
def fahrenheit(celsius):
    return (celsius * 9/5) + 32

_ADC_PIN = 0
_WARNING_LED_PIN = 14

# create i2c for display
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=100000)
print('i2c.scan: ', i2c.scan())   #[60]
# OLED screen dimensions
__WIDTH = const(128) 
__HEIGHT = const(32)
oled = ssd1306.SSD1306_I2C(__WIDTH, __HEIGHT, i2c)

# program
# read voltage (mV)
adc = machine.ADC(_ADC_PIN)
#TEST: print('ADC reading:', adc.read())
alert = machine.Pin(_WARNING_LED_PIN, machine.Pin.OUT)

# alert ON and OFF
def alertOn():
    alert.on()

def alertOff():
    alert.off()

# run readng T, Ctrl-C to abort
_TRESHOLD = const(30)
def run(dt=2.0):
    print('TMP36 demo on OLED')
    try:
        while True:
            oled.fill(0)  # clear screen
            reading = adc.read()
            celsius_temp = temp(reading)
            fahrenheit_temp = fahrenheit(celsius_temp)
            print('TMP36 reading {}\tDegrees Celsius {}\tDegrees Fahrenheit {}'.format(reading, celsius_temp, fahrenheit_temp))
            oled.text('TMP36 {0} '.format(reading),0,0)
            oled.text('Celsius {0:0.1f}'.format(celsius_temp),0,10)
            oled.text('Fahrenheit {0:0.1f}'.format(fahrenheit_temp),0,20)
            if celsius_temp > _TRESHOLD:
                alertOn()
            else:
                alertOff()
            oled.show()
            time.sleep(dt) #wait > s, see datasheet
    except:
        print('Exception! Done')

run(5.0)
