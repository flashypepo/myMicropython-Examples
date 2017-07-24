# This file is executed on every boot (including wake-boot from deepsleep)
# 2017_0425 PePo added all commands - boot.py was an empty file except line 1
#           However: esp.osdebug() and webrepl do not exist
# import esp
# esp.osdebug(None)
import gc
# import webrepl
# webrepl.start()
gc.collect()
