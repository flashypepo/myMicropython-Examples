'''
 doconnectwifi - utilities to connect to Wifi network.
 credentials in external text file - see usage
 2017_1028 removed usage - must be external activated
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
    return pw

# usage to connect
# pre-condition: requires file on development board with password
# doConnect ("ZiggoNO34", readPasswordFrom('ssid.txt'))
