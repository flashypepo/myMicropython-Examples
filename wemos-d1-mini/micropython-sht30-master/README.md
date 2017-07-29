#SHT30 Sensor driver in micropython

Micropython driver for [SHT30 Shield](https://www.wemos.cc/product/sht30-shield.html) for [Wemos D1 Mini (and PRO)](https://www.wemos.cc/product/d1-mini-pro.html).

The driver has been tested on Wemos D1 mini PRO, but It should work on whatever other micropython board, if anyone find problems in other boards, please open an issue and We'll see.

##Motivation
The SHT30 shield for ESP8266 board Wemos D1 Mini has an Arduino driver but not a micropython one.

##References:

* [Sensor Datasheet](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital.pdf)
* [Arduino driver](https://github.com/wemos/WEMOS_SHT3x_Arduino_Library)
* [SHT30 C Code Examples](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/11_Sample_Codes_Software/Humidity_Sensors/Sensirion_Humidity_Sensors_SHT3x_Sample_Code_V2.pdf) from sensor manufacturer

##Examples of use:

###How to get the temperature and relative humidity:

The `measure()` method returns a tuple with the temperature in celsius grades and the relative humidity in percentage. 
If the measurement cannot be performed then an exception is raised (`SHT30Error`)

```python
from sht30 import SHT30

sensor = SHT30()

temperature, humidity = sensor.measure()

print('Temperature:', temperature, 'ºC, RH:', humidity, '%')
```

There is another method, `measure_int()`, that returns 4 integer values, **no floating point operation is done**, designed 
for environments that doesn't support floating point operations, the four values are: 

Temperature (integer part), Temperature (decimal part), RH (integer part), RH (decimal part)

For intance, if the `measure()` method returns `(21.5623, 32.0712)` the `measure_int()` method would return: `(24, 56, 32, 7)` The decimal 
part is limited to 2 decimal digits.

```python
t_int, t_dec, h_int, h_dec = sensor.measure_int()

print('Temperature: %i.%02i °C, RH: %i.%02i %%' % (t_int, t_dec, h_int, h_dec))
```

Both methods allow a `raw` param that when It's `True` returns the sensor measurement as-is, It's a `bytearray(6)` with the format defined in the sensor datasheet document.

```python
raw_measure = sensor.measure(raw=True)

print('Sensor measurement', raw_measure)
```

###Check if shield is connected

```python
from sht30 import SHT30

sensor = SHT30()

print('Is connected:', sensor.is_present())

```

###Read sensor status

Check the [Sensor Datasheet](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/Sensirion_Humidity_Sensors_SHT3x_Datasheet_digital.pdf) for further info about sensor status register
```python
from sht30 import SHT30

sensor = SHT30()

print('Status register:', bin(sensor.status()))
print('Single bit check, HEATER_MASK:', bool(sensor.status() & SHT30.HEATER_MASK))

#The status register can be cleared with
sensor.clear_status()

```


###Reset the sensor

The driver allows a soft reset of the sensor

```python
from sht30 import SHT30

sensor = SHT30()
sensor.reset()

```



###Error management

When the driver cannot access to the measurement an exception `SHT30Error` is raised

```python
from sht30 import SHT30

sensor = SHT30()

try:
    t, h = sensor.measure()
except SHT30Error as ex:
    print('Error:', ex)


```
