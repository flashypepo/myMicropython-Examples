# Star Wars Asciimation
# show, if all is well, an animation of star wars in ASCII, telnet connection
# should also work on computer with Python3
# URL: http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html#star-wars-asciimation
import socket

# get addres information of site
addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
print(addr_info) #debug

# get the IP and port
addr = addr_info[0][-1]
print(addr) #debug

# connect to it via socket
s = socket.socket()
s.connect(addr)

# print content/animation in console
# use cntrl-C to interrupt
while True:
    data = s.recv(500)
    print(str(data, 'utf8'), end='')

# 2017-0812: seems not to work (anymore). Unknown.
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "starwars.py", line 23, in starwars
OSError: [Errno 104] ECONNRESET
'''
