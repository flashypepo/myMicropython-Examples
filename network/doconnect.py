'''
 netwerk utilities
 
 2017_0604 WeMOS Lolin32 - first version
'''

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
# 2017-0529 ssid=filename, pw contents of file
pw = readPasswordFrom('pepodevnet.txt')
doConnect ("PePoDevNet", pw)
# TODO: 
# 1. read from json file: ssid + pw
# 2. credentials from separate Python object ala Arduino ...
# myWifi = new MyWifiCredentials()
# ssid = myWifi.ssid()
# password = myWifi.password()
# doConnect (ssid, password)
