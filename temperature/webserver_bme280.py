# simple webserver which displays temperature of BME280 sensor
# 2017-1105 from https://github.com/catdog2/mpy_bme280_esp8266
# PRE_CONDITION: device is connected with Wifi

html = """<!DOCTYPE html>
<html>
    <head> 
        <title>Weatherstation</title>
        <meta http-equiv="refresh" content="30">
    </head>
    <body> <h1>Room conditions</h1>
        <table border="1"> <tr><th>Temperature</th><th>Pressure</th><th>Humidity</th></tr> %s </table>
    </body>
</html>
"""

# loop: get temperature - #added 2017-1106
import machine
import bme280

# WeMOS D1 mini: scl=D1(5), sda=D2(4)
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
print('BME280 i2c-address: {}'.format(i2c.scan())) # nominal: [118]
bme = bme280.BME280(i2c=i2c)

# my get sensor data
# 2017-1106 variant of bme.values
def getBME280Data():
    t, p, h = bme.read_compensated_data()
    
    p = p // 256
    pi = p // 100
    pd = p - pi * 100
    
    hi = h // 1024
    hd = h * 100 // 1024 - hi * 100
    
    return ('<tr><td> {0} </td><td> {1}.{2:02d} </td><td> {3}.{4:02d} </td></tr>'.format(t / 100, pi, pd, hi, hd))

# alert led
# 2017-1105 WeMOS D1 mini: GPIO12
import led
led = led.setup() #default pin

# network: setup webserver
import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
rows = [] #empty rows #added 2017-1105
max_row = 12 #added 2017-1105

try:
    while True:
        led.on() #show I'm alive
        cl, addr = s.accept() #wait for client

        print('client connected from', addr)
        led.off() #client connected
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break

        #OK: rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
        #OK: rows += ['<tr><td> {0:4.1f} </td></tr>'.format(ds18b20.temperature(ds))] # DS18B20
        rows += [getBME280Data()] # BME280
        
        response = html % '\n'.join(rows)
        cl.send(response)
        cl.close()

        #added 2017-1105: maximum of 12 rows
        max_row -= 1
        if max_row < 1:
            rows=[]
            max_row = 12
except:
    print('Collecting sensor data intercepted')
    led.blink(0.2) #fast blink to get attention!
