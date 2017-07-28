# This file is executed on every boot (including wake-boot from deepsleep)
# 2017-0604 PePo: emergency buffer, debug off(?), gc collect
import micropython
micropython.alloc_emergency_exception_buf(100)
# import esp
# exists? esp.osdebug(None)
import gc
gc.collect()
