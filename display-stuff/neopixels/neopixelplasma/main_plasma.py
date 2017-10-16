# main - select which programma should startup
import sys
print(sys.implementation) # MP version

import stream_plasma #2017-0728

import gc
gc.collect() #cleanup
print('mem_free: ', gc.mem_free())
