# RTC clock with DS1307
#
# 2017-0225 various tests, since micropython 1.8.7 changes RTC interface
# Sources:
# ESP8266 - connection to RTC, I2C-connection with NodeMCU
# MicroPython class RTC: https://micropython.org/resources/docs/en/latest/wipy/library/machine.RTC.html
#     class RTC is only for WiPy board, but also works in ESP8266
#     interface/methods are changed, is more like Adafruit uRTC
# class uRTC of Adafruit is NOT used, but documentation is used!
# Adafruit uRTC: http://micropython-urtc.readthedocs.io/en/latest/urtc.html#ds1307
#

import machine

# create an RTC object
# 2017_0225 apparently no I2C address has to be given?? It works, however.
print("create RTC object...")
rtc = machine.RTC()
# initialise the RTC to a certain datetime
#
# Analyses:
# * according to Adafruit documentation datetime().
#
# * rtc.datetime(datetime): get or set the current time.
#      The datetime is an 8-tuple of the format describing the time
#      to be set:
#   (year, month, day, weekday, hour, minute, second, millisecond)
#
# * If not specified, the method returns a tuple in the same format.
# * day of the week: an integer, where Monday is 0 and Sunday is 6.

# set RTC:     (y,  m, d, wd, h,  m,  s, ms)
# rtc.datetime((2017, 2, 25, 6, 22, 48, 15, 0))

# get datetime
print("current datetime: ", rtc.datetime())

# get help about rtc
print("\nprint help about RTC object...")
help(rtc)
# object <RTC> is of type RTC
#   datetime -- <function>
#   memory -- <function>
#   alarm -- <function>
#   alarm_left -- <function>
#   irq -- <function>
#   ALARM0 -- 0

print("\ncreate an alarm which triggers off in 10 seconds...")
import time
# set alarm in 10 seconds
rtc.alarm(0, 10000)
print("print time-left of alarm...")
# get time left to alarm
time.sleep(7.0)
print(rtc.alarm_left(0))
time.sleep(1.0)
print(rtc.alarm_left(0))
time.sleep(1.0)
print(rtc.alarm_left(0))
time.sleep(1.0)
print(rtc.alarm_left(0))
print("Alarm is on, no visible cues. How todo?")

print("\n===== end-of-RTC-test ===")
