# scans for WiFi networks
# 2017_0224 new, based upon network documentation of micropython
#     https://docs.micropython.org/en/latest/esp8266/library/network.html

import network

# network must be Station
nic = network.WLAN(network.STA_IF)
nic.active(True) #activate network

# wlan.scan()
# Scan for the available wireless networks.
#
# Scanning is only possible on STA interface.
# Returns list of tuples with the information about WiFi access points:
#   (ssid, bssid, channel, RSSI, authmode, hidden)
#
#   bssid is hardware address of an access point, in binary form, returned as bytes object. You can use ubinascii.hexlify() to convert it to ASCII form.
#
#   There are five values for authmode:
#             0 – open
#             1 – WEP
#             2 – WPA-PSK
#             3 – WPA2-PSK
#             4 – WPA/WPA2-PSK
#
#    and two for hidden:
#             0 – visible
#             1 – hidden
ssids = nic.scan()

# TEST: print tuples
for ssid in ssids:
    print(ssid)

# (b'Ziggo03827', b" %d\x1c'\xe0", 1, -82, 4, 0)
# (b'Ziggo', b'"%d\x1c\'\xe1', 1, -80, 5, 0)
# (b'Ziggo14433', b'\xe0i\x95\xde\xfb\xa9', 6, -89, 4, 0)
# (b'Ziggo', b'\xe2i\x95\xde\xfb\xaa', 6, -89, 5, 0)
# (b'HZN245614458', b'T\xfa>\x87\x8f\xd7', 8, -89, 3, 0)
# (b'AirPort Time Capsule', b'\x88\x1f\xa16\x03\xd8', 11, -82, 3, 0)
# (b'PePoDevNet', b'|\xd1\xc3\xcd\xb4\x1e', 11, -57, 4, 0)
# (b'Ziggo03827-2', b' %d\x1b\x11A', 1, -88, 3, 0)

# TODO:
# 1.extract from list my networks Ziggo03827, PePoDevNet, Ziggo03827-2
# 2.sort on highest RSSI
# 3.connect to top-one
