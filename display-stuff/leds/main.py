'''
main.py - startup various programs
2017-0726 add display of MP-version
2017-0604 PePo blinking BUILTIN LED
'''
import machine
import time
import sys
print(sys.implementation) #display MP-version

#import blinky  #2017-0728 WeMOS D1 R2
#import breathingLED
#import knightrider
import pulseLED  #2017-0728 - finite time
#import blinkled #2017-0726

gc.collect()
print('gc.mem_free:', gc.mem_free())