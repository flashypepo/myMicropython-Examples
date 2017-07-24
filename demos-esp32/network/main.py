# 2017-0919 automtically connect to home-wifi
import connectWifi
connectWifi.connect ("PePoDevNet", connectWifi.readPasswordFrom('pepodevnet.txt'))
# run oled demo
import oledDemo
