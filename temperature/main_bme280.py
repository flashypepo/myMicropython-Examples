# Send temperature via address 192.168.178.21 as webserver# 2017-1106 PePo bme280-i2c, temperture, pressure and humidity# 2017-1105 PePo ds18b20 - only temperature#_SENSOR = 'DS18B20'_SENSOR = 'BME280'print('webserver for {}'.format(_SENSOR))# connect to a personal Wifi network ---------import wifinetwork as wifi_SSID = 'PePoDevNet'print('Wifi: connecting to {}'.format(_SSID))wifi.connectTo(_SSID)# setup sensor, led and webserver#import webserver_ds18b20import webserver_bme280