'''
connectWifi: Wifi network utilities
2017_0719 rename function, added check for connection, no actions when imported
    tested on: Lolin32 OLED
2017_0604 WeMOS Lolin32 - first version

Usage:
    import connectWifi
    connectWifi.connect ("PePoDevNet", connectWifi.readPasswordFrom('pepodevnet.txt'))

Sources:
 https://techtutorialsx.com/2017/06/06/esp32-esp8266-micropython-automatic-connection-to-wifi/
'''
# connect to essid with password
def connect(essid, password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    if not wlan.isconnected():
        print('connecting to network... ', essid)
        wlan.connect(essid, password)
        while not wlan.isconnected():
            pass
    else: # already connected
        print('{0}: already connected'.format(essid))
    
    print('network config:', wlan.ifconfig())

# read pw from file to make it not visible
def readPasswordFrom(filename):
    f = open(filename, 'r')
    pw = f.read().strip()
    #print ('length password =', len(pw))
    return pw

# TODO: 
# read credentials from json file: ssid + pw
# print status on OLED
