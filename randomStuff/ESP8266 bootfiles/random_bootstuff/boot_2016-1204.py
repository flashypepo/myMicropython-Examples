# This file is executed on every boot (including wake-boot from deepsleep)
# 2016_1204 commented osdebug-statements, problems with ampy? and WEBREPL?
# 2016_0918 PePo disable debug message
#import esp
#esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()
