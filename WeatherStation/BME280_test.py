# BME280 sensor test
#
# source: https://github.com/catdog2/mpy_bme280_esp8266
# 2017_0225 Python code forked, cloned and created this example
# bme280.py must be present on the ESP8266

import machine
import bme280

i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
bme = bme280.BME280(i2c=i2c)

# print tuple: temperature, pressure and humidity
print(bme.values)
# result: ('19.48C', '1010.56hPa', '40.33%')

# print separate values from BME280
print ("temperature: ", bme.read_compensated_data()[0] / 100, "C")
# temperature:  19.6 C
print ("pressure: ", bme.read_compensated_data()[1] / 256 / 100, "hPa")
# pressure:  1010.51 hPa
print ("humidity: ", bme.read_compensated_data()[2] / 1024, "%RH")
# humidity:  39.71289 %RH
