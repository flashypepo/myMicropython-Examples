# This file is executed on every boot (including wake-boot from deepsleep)
# 2016_0918 PePo disable debug message
import esp
esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()
