'''
 netwerk utilities
 TODO: JSON config-file with ssid:ww entry/entries

 2017-0818 PePo minor changes to return in passwrd
 2017_0604 WeMOS Lolin32 - first version
'''
#ORG: def connectTo(essid, password):
def connectTo(essid):
    """ connect to a personal Wifi network """
    # internal helper function
    def readPasswordFrom(filename):
        """ reads password for Wifi network from file """
        f = open(filename, 'r')
        return ( f.read().strip() )

    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network... ', essid)
        ww = readPasswordFrom('{0}.txt'.format(essid.lower()))
        wlan.connect(essid, ww)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

'''
def readPasswordFrom(filename):
    """ reads password for Wifi network from file """
    f = open(filename, 'r')
    #pw = f.read().strip()
    #return pw
    return ( f.read().strip() )
#'''

# Usage:
# pre-condition: file '<ssid>.txt' exists
# connectTo ("<ssid>")
# example: <ssid> = PePoDevNet
