# This file is executed on every boot (including wake-boot from deepsleep)
# TODO: send timestamp and temperature (Celsius) to web...
# 2017-0819 PePo add sensor, led and print to serial port
# 2017-0811 PePo updated: no debug, disable webrepl,
# source: https://youtu.be/yGKZOwzGePY - Tony D! MP ESP8266 HTTP examples

print('main.py executing...')

# connect to a personal Wifi network ---------
import wifinetwork as wifi
# TODO: JSON config-file with ssid:ww entry/entries
#wifi.connectTo("PePoDevNet", wifi.readPasswordFrom('pepodevnet.txt'))
wifi.connectTo("PePoDevNet")

# set the time from nptime ---------
#print('TODO: get current time from the web...')
print('... setting time from the web')
import nptime
print('UTC time:', nptime.settime())
#print('\tTODO -local time')

''' test loop: get temperature ---------
import test_ds18b20
test_ds18b20.run(5.0)
#'''


# loop: get temperature ---------
import ds18b20
ds = ds18b20.setup() #get sensor

import led
led = led.setup() #default pin
#TEST: led.blink()

# --- location ---------------
_LOCATION = 'studyroom'

''' print data to serial port
print('... print sensor data to serial port')
def serialDisplay(dt=2.0):
    import time
    import utime
    while True:
        led.on()
        temp = ds18b20.temperature(ds)
        timestamp = utime.localtime()
        print('{0},{1},{2},{3},{4},{5},{6},{7:0.2f}'.format(_LOCATION,timestamp[0],timestamp[1],timestamp[2],timestamp[3]+2,timestamp[4],timestamp[5],temp))
        led.off()
        time.sleep(dt)
try:
    serialDisplay(10.0)
except:
    pass
#'''

#''' store data in file
print('... print sensor data to file temperature.txt')
def temperatureStore(dt=2.0):
    import time
    import utime

    def write_record(timestamp, temp):
        f = open('temperature.txt', 'a') #append mode
        data = '{0},{1},{2},{3},{4},{5},{6},{7:0.2f}\n'.format(_LOCATION,timestamp[0],timestamp[1],timestamp[2],timestamp[3]+2,timestamp[4],timestamp[5],temp)
        f.write(data)
        f.close()

    while True:
        led.on()
        temp = ds18b20.temperature(ds)
        timestamp = utime.localtime()
        print('{0},{1},{2},{3},{4},{5},{6},{7:0.2f}'.format(_LOCATION,timestamp[0],timestamp[1],timestamp[2],timestamp[3]+2,timestamp[4],timestamp[5],temp))
        write_record(timestamp, temp)
        #f = open('temperature.txt', 'a') #append mode
        #data = '{0},{1},{2},{3},{4},{5},{6},{7:0.2f}\n'.format(_LOCATION,timestamp[0],timestamp[1],timestamp[2],timestamp[3]+2,timestamp[4],timestamp[5],temp)
        #f.write(data)
        #f.close()
        led.off()
        time.sleep(dt)
#run
try:
    temperatureStore(60.0) # 1 measurement per minute
except:
    print('temperatureStore() intercepted')
    pass
#'''

#''' TODO print data in webpage
print('... TODO - send sensor data to my webpage')
