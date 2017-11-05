# main - startup to connect to Wifi network
# 2017-1028 PePo added iconsdemo WeMOS D1 mini Pro
import doconnectwifi
doconnectwifi.doConnect ("ZiggoNO34", doconnectwifi.readPasswordFrom('ssid.txt'))

''' ICONS demo on LED 8x8 matrix
# 2017-1028 work-in-progress
import iconsdemo
import urandom
import time
try:
    while True:
        # micropython
        b = urandom.getrandbits(4) # 0..15
        if b > 15:
            b = 15
        # curcuitpython
        #b = urandom.randrange(10) #pickup random value 0..9
        print('brightness:{0}'.format(b))
        iconsdemo.demo(0.8, b)
        time.sleep(2)
except:
    iconsdemo.clear(iconsdemo.lefteye)
    print('Demo done')
#'''

#''' Weatherpal demo
# 2017-1028 work-in-progress - numbers mirrored on matrix???
import weatherpal
weatherpal.runtrycatch()
#'''
