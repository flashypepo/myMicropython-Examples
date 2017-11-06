# simple webserver which displays temperature of DS18B20 sensor
# 2017-1105 from http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html
# PRE_CONDITION: device is connected with Wifi

html = """<!DOCTYPE html>
<html>
    <head> 
        <title>Weatherstation</title>
        <meta http-equiv="refresh" content="10">
    </head>
    <body> <h1>Studyroom</h1>
        <table border="1"> <tr><th>Temperature</th></tr> %s </table>
    </body>
</html>
"""

# loop: get temperature - #added 2017-1105
import ds18b20
ds = ds18b20.setup() #get sensor

#alert led - #added 2017-1105
import led
led = led.setup() #default pin WeMOS D1 mini: GPIO12

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)
rows = [] #empty rows #added 2017-1105
max_row = 12 #added 2017-1105
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
    #rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    #OK: rows += ['<tr><td> %s </td></tr>' % str((ds18b20.temperature(ds)))]
    rows += ['<tr><td> {0:4.1f} </td></tr>'.format(ds18b20.temperature(ds))]
    response = html % '\n'.join(rows)
    cl.send(response)
    cl.close()
    #added 2017-1105
    max_row -= 1
    if max_row <1:
        #restart rows
        max_row = 12
        rows=[]
