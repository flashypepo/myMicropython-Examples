# This file is executed on every boot (including wake-boot from deepsleep)
# TODO: send timestamp and temperature (Celsius) to web...
# 2017-1105 PePo add _isLocal: sensor data to serial port (False) of stored in file (True)
# 2017-0819 PePo add sensor, led and print to serial port
# 2017-0811 PePo updated: no debug, disable webrepl,
# source: https://youtu.be/yGKZOwzGePY - Tony D! MP ESP8266 HTTP examples

print('main.py executing...')

# connect to a personal Wifi network ---------
import wifinetwork as wifi
# TODO: JSON config-file with ssid:ww entry/entries
#wifi.connectTo("PePoDevNet", wifi.readPasswordFrom('pepodevnet.txt'))
print('Wifi: connect to PePoDevNet...')
wifi.connectTo("PePoDevNet")

# set the time from nptime ---------
#print('TODO: get current time from the web...')

print('getting time from the web...')
import nptime
print('... UTC time:', nptime.settime())
#print('\tTODO -local time')
# --- SUMMERTIME or not (=WINTERTIME) ---------------
_isSummerTime = False
print('... Summertime:', _isSummerTime)

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

# --- SERIAL PORT or STORAGE of temperature -----
_isLocal = False # or True, when temperature is te be stored in local file

# helper function: returns temperature-record as string
def temp_record(timestamp, temp):
    # timestamp[3] correction for Summertime or not
    def _tc(t):
        correction = 1
        if _isSummerTime:
            correction = 2
        return t + correction
    
    data = '{0},{1},{2},{3},{4},{5},{6},{7:0.2f}\n'.format(_LOCATION, timestamp[0],timestamp[1],timestamp[2],_tc(timestamp[3]),timestamp[4],timestamp[5],temp)
    return data


print('... collect sensor data')

#''' print data to serial port
# print sensor data to serial port')
def serialDisplay(dt=2.0):
    import time
    import utime
    while True:
        led.on()
        
        temp = ds18b20.temperature(ds)
        timestamp = utime.localtime()
        #print('{0},{1},{2},{3},{4},{5},{6},{7:0.2f}'.format(_LOCATION, timestamp[0],timestamp[1],timestamp[2],_tc(timestamp[3]),timestamp[4],timestamp[5],temp))
        print( temp_record(timestamp, temp) )
        
        led.off()
        time.sleep(dt)

''' run 
try:
    serialDisplay(10.0)
    
except:
    print('temperature collecting intercepted')
    pass
    
#'''

#''' store data in file temperature.txt
def temperatureStore(dt=2.0):
    import time
    import utime
    
    # helper function to add sensor data record to file
    def write_record(timestamp, temp):
        f = open('temperature.txt', 'a') #append mode
        #data = '{0},{1},{2},{3},{4},{5},{6},{7:0.2f}\n'.format(_LOCATION, timestamp[0],timestamp[1],timestamp[2],_tc(timestamp[3]),timestamp[4],timestamp[5],temp)
        f.write( temp_record(timestamp, temp) )
        f.close()

    while True:
        led.on()
        
        temp = ds18b20.temperature(ds)
        timestamp = utime.localtime()
        write_record(timestamp, temp)
        
        led.off()
        time.sleep(dt)

#main run
def run():
    try:
        if _isLocal:
            # collect and store sensor data in file
            # watch out: can be very large overtime
            temperatureStore(60.0) # 1 measurement per minute
        else:
            # collect and print sensor data to serial port
            serialDisplay(10.0)
    
    except:
        print('collecting temperature data intercepted')
        pass
#'''

#''' TODO print data in webpage
print('TODO - send sensor data to my webpage')
