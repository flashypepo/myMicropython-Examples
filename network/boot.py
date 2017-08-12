# This file is executed on every boot (including wake-boot from deepsleep)
# 2017-0811 PePo updated: no debug, disable webrepl,
# source: https://youtu.be/yGKZOwzGePY - Tony D! MP ESP8266 HTTP examples
import esp
esp.osdebug(None)
import gc

def doConnect(essid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network... ', essid)
        wlan.connect(essid, password)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

def readPasswordFrom(filename):
    f = open(filename, 'r')
    pw = f.read().strip()
    #print ('length password =', len(pw))
    return pw

# connect
# requires file on development board with password
#pw = readPasswordFrom('pepodevnet.txt')
doConnect ("PePoDevNet", readPasswordFrom('pepodevnet.txt'))

#import webrepl
#webrepl.start()
gc.collect()
