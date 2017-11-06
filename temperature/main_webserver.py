# 2017-1105 PePo send temperature via address 192.168.178.21 as webserver

print('webserver ds18b20...')

# connect to a personal Wifi network ---------
import wifinetwork as wifi
print('Wifi: connect to PePoDevNet...')
wifi.connectTo("PePoDevNet")

# setup sensor, led and webserver
import webserver_ds18b20
