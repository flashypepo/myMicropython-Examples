# DHT22.py - demo temperature/humidity sensor DHT22 on GPIO15
# 2017-0927 PePo new, Huzzah

import machine,time
import dht

# create DHT22 sensor object
sensor = dht.DHT22(machine.Pin(5))

'''demo - measure T and H every dt secods, dt=2.5 default
def run(dt=2.5):
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    print('T:{0} Celsius, H:{1} %'.format(t, h ))
    time.sleep(dt)
#'''

#demo2 - led=on when H > h_threshold
led = machine.Pin(14, machine.Pin.OUT)
led.value(0)
def run(threshold = 80, dt=2.5):
    sensor.measure()
    t = sensor.temperature()
    h = sensor.humidity()
    print('T:{0} Celsius, H:{1} %'.format(t, h ))
    if h > threshold:
        led.value(1)
        print('Alert!')
    else:
        led.value(0)
    time.sleep(dt)

#execute
while True:
    run()
