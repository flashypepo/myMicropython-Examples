# Connect GPIO16 to the reset pin (RST on HUZZAH). 
# Then the following code can be used to sleep, wake and check the reset cause:
# 2017_0101 PePo http://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html

import machine

# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
rtc.alarm(rtc.ALARM0, 10000)

# put the device to sleep
machine.deepsleep()
