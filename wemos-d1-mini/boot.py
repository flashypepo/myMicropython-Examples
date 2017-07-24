# This file is executed on every boot (including wake-boot from deepsleep)
# 2017_0601 updated by PePo: debug None, emergency-buffer
# reference: http://docs.micropython.org/en/v1.8.7/esp8266/library/micropython.html
import esp
esp.osdebug(None)
import micropython
micropython.alloc_emergency_exception_buf(100)
import gc
#import webrepl
#webrepl.start()
gc.collect()
