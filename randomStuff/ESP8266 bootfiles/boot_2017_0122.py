# This file is executed on every boot (including wake-boot from deepsleep)
# 2017_0122 disabled debug message
import esp
esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()
