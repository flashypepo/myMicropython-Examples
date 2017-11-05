# main - startup to connect to Wifi network
# 2017-1028 PePo new - WeMOS D1 mini Pro
import doconnectwifi
doconnectwifi.doConnect ("ZiggoNO34", doconnectwifi.readPasswordFrom('ssid.txt'))
