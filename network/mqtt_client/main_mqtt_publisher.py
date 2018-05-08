# This file is executed on every boot (including wake-boot from deepsleep)
# 2017-1210 PePo send timestamp and temperature (Celsius) to MQTT-server on BBB
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

# temperature  ---------
import class_ds18b20
#get sensor at GPIO14
ds = class_ds18b20.DS18B20(14)

# --- location ---------------
_LOCATION = 'studyroom'

#7-segment display
import tm1637
from machine import Pin
import math
# create tm
tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
#print('tm: ', tm)

def display_tm1637(t):
    #debug: print('display: temp=', t)
    tm.temperature( math.floor(t) )

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

#''' store data in file temperature.txt
# default: 1 measuremtn per 30 seconds
def saveT2File(dt=30.0):
    import time
    import utime

    print('saveT2File({0}) entered...'.format(dt))
    
    # helper function to add sensor data record to file
    def write_record(timestamp, temp):
        f = open('temperature.txt', 'a') #append mode
        #data = '{0},{1},{2},{3},{4},{5},{6},{7:0.2f}\n'.format(_LOCATION, timestamp[0],timestamp[1],timestamp[2],_tc(timestamp[3]),timestamp[4],timestamp[5],temp)
        f.write( temp_record(timestamp, temp) )
        f.close()

    while True:
        #FUTURE: led.on()
        timestamp = utime.localtime()
        temp = ds.celsius
        display_tm1637(temp) #display
        write_record(timestamp, temp) #write in file
        #FUTURE: led.off()
        time.sleep(dt)

# send data to MQTT-server
def send2Server(dt=30.0):
    import time
    import utime
    from umqtt.simple import MQTTClient

    #print('send2server({0}) entered...'.format(dt))
    #MQTT configuration -----------------
    mqtt_server = '192.168.178.40' #ip-address of MQTT-server
    TOPIC_TEST = b'topic/test'     # topic: debug message
    TOPIC_VALUE = b'topic/value'   # topic: temperature value
    TOPIC = b'topic/temperature'   # topic: temp-record

    #helper: sends data to MTQQ-server: connect-send payload-disconnet
    def sendMQTT(payload, topic=TOPIC, server= mqtt_server):
        #print('sendMQTT():', payload)
        c = MQTTClient("umqtt_client", server)
        c.connect()  #success: returns 0
        #debug: conn = c.connect()
        #print('MQTT connection:', conn)
        c.publish(topic, payload)
        c.disconnect()

    #broadcasting via topic:test
    payload = b'MQTT-server: {0},\nTOPIC: {1},\nCollecting temperatures...'.format(mqtt_server, TOPIC) #debug
    sendMQTT(payload, TOPIC_TEST)
    print(payload)
    
    while True:
        timestamp = utime.localtime()
        temp = ds.celsius

        #print('temperature on display')
        display_tm1637(temp) 
        
        #print('broadcast temp-record')
        payload = temp_record(timestamp, temp)
        sendMQTT(payload)
        
        #print('broadcast temp-value')
        payload = b'{0}'.format(temp)
        sendMQTT(payload, TOPIC_VALUE)
        
        time.sleep(dt)

#main run() - by-default 1 measurement per 30 seconds
def run(dt=30.0):
    #store data local (True) or send to server (False)
    _isLocal = False; 
    try:
        if _isLocal:
            # watch out: file can be very large overtime
            saveT2File(dt)
        else:
            send2Server(dt)
    
    except:
        print('collecting temperature data intercepted')
        pass

# go ahead and start getting, sending/storing the sensor data
if __name__ == "__main__":
	run(60.0) # 1 measurement per minute
