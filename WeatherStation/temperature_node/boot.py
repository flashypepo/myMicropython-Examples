# This file is executed on every boot (including wake-boot from deepsleep)
# 2017-0811 PePo updated: no debug, disable webrepl,
import esp
esp.osdebug(None)
import gc
#import webrepl
#webrepl.start()
gc.collect()
print('boot.py processed')
