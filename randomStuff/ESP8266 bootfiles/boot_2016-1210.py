# This file is executed on every boot (including wake-boot from deepsleep)
# 2016-1210 PePo turn off debug-messages (uncomment line 3 and 4)
import esp
esp.osdebug(None)
import gc

# 2016-1210 PePo connect to to Wifi... WORKS at home
def do_connect(ssid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect('PePoMilkyWay', 'HNFFfcYj6EKN')
# lateron: do_connect('devices', 'devices2') # ?? WF

#import webrepl
#webrepl.start()
gc.collect()
