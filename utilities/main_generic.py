# main - select which programma should startup
# 2017-0904 generic main
print('processing main...')

import sys
print(sys.implementation) # MP version

import gc
gc.collect() #cleanup
print('free memory:', gc.mem_free())
