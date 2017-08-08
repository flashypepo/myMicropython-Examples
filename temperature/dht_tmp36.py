# temperature reading from DHT22 and TMP36
# Huzzah:
# DHT22: data -> pin ?, Ucc = 3.3V
# TMP36 data -> A0 (ADC), Ucc = 3.3V
#
# NodeMCU:
# DHT22: data -> pin 0, Ucc = 3.3V (=5V no difference)
# TMP36 data -> A0 (ADC), Ucc = 3.3V
#
# 2017-0808 PePo initial setup

import machine, time
import dht

__DHT_PIN = const(0) # NodeMCU: pin D3
#__DHT_PIN = const(x) # Huzzah: pin GPIO??
__ADC_PIN = const(0) # ESP8266 must be always 0 (pin A0/ADC)

__DELTA = const(17) # empirical difference between TMP36 and DHT22
def temp(value):
    #return (value - 500) / 10 #Huzzah
	return (value - __DELTA) / 10 #NodeMCU

# Celsius to Fahrenheit
def fahrenheit(celsius):
    return (celsius * 9/5) + 32

# create ADC-object
adc = machine.ADC(__ADC_PIN)
# creae DHT22-object
d = dht.DHT22(machine.Pin(__DHT_PIN))

#define demo
# time between measurements DHT: >= 2 seconds
def run(dt=2.5):
    while True:
        reading = adc.read() # read A0 - TMP36
        d.measure() # read DHT22 T & H
        celsius_temp = temp(reading)
        fahrenheit_temp = fahrenheit(celsius_temp)
        print('TMP36 temperature:{0:0.1f}C\t{1:0.1f}F\treading:{2}'.format(celsius_temp, fahrenheit_temp,reading))
        print('DHT22 temperature:{0:0.1f}C\thumidity {1:0.1f}%'.format(d.temperature(), d.humidity()))
        time.sleep(dt)

#run demo
try:
    print('Temperature demo')
    run(10.0) #measure temp and humidity every 10 seonds
except:
    print('interrupted - done')
