# example to download a webpage
# 2017-0812 PePo okay, URL must contain at least 3 parts
# URL: http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html

import socket

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break
    s.close()

#examples
http_get('http://micropython.org/ks/test.html')
#watch out for next one, >38664 records at 2017-0812
http_get('http://pepo.nl/ds3231/list_ds3231.php')
