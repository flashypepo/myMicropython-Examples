# 2017_0101 PePo http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html

from machine import Timer

tim = Timer(-1)
tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))
tim.init(period=2000, mode=Timer.PERIODIC, callback=lambda t:print(2))
