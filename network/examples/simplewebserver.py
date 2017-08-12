# simple webserver example
# shows the state of GPIO-pins
# 2017-0812 PePo added ESP32 pins (tried),
#           increased listeners from 1 to 3
# URL: http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html#simple-http-server
# ESP32-pins: http://www.pighixxx.com/test/portfolio-items/esp32/?portfolioID=360#prettyPhoto

import machine

#ESP8266 pins
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

#ESP32 pins
#2017-0812 crashed ESP32, probably because some port should not be set to IN
# TODO which ESP32-pins can be quered?
#pins = [machine.Pin(i, machine.Pin.IN) for i in (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,32,33,34,35,36,39)]

html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Pins</title> </head>
    <body> <h1>ESP8266 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""
import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
# allows for number of accepted clients
#ORG: s.listen(1)
s.listen(3)
''' socket.listen([backlog])
Enable a server to accept connections.
If backlog is specified, it must be at least 0
(if it’s lower, it will be set to 0);
and specifies the number of unaccepted
connections that the system will allow
before refusing new connections.
If not specified, a default reasonable
value is chosen. '''
print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send(response)
    cl.close()
