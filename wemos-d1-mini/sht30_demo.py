'''
SHT30 shield - temperature and humidity sensor
2017-0729 PePo new, based upon https://github.com/rsc1975/micropython-sht30
'''

import sht30
import time

_WAITIME = 10.0 # waiting time between measurements
sensor = sht30.SHT30()

try:
    if not sensor.is_present():
        print('SHT30 shield is not connected')
        pass
    print('Start measurements...')

    while True:
        t, h = sensor.measure()
        #print('Temperature:', t, 'ºC, RH:', h, '%')
        #TODO: 
        print('Temperature: {0:0.2f} ºC, humidity: {1:0.2f} %'.format(t, h))
        time.sleep(_WAITIME)

except sht30.SHT30Error as ex:
    print('Error:', ex)
except:
    print('done')

