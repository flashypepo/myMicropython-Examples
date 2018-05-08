"""
main.py - startup various programs
2017-1229 get bitcoin price on OLED
2017-1227 connect to wifi, heartbeat
2017-0726 add display of MP-version
2017-0604 PePo blinking BUILTIN LED
"""
#2017-1227 connect to PePoDevNet wifi...
import wifimanager
wifimanager.doconnect("PePoDevNet", wifimanager.readpasswordfrom('ssid.txt'))

#import blinky
#import pulseledbar #2017-1204
#import heartbeat #2017-1204
#heartbeat.run()
#2017-1227 eyes ala Zoomer (setup)
#import demoeyes
#2017-1229 get bitcoin price
print("Read bitcoin price from cryptocompare.com")
import getbitcoinprice
#'''

# cleanup garbage...
import gc
gc.collect()
print('gc.mem_free:', gc.mem_free())
