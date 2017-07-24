#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:08:30 2017

@author: pepo
"""

#from neopixelstrip import *

def runner(delay = 0.3):
    i = 0
    while True:
        np.fill((0,0,0))
        np[i] = (0,0,128)
        np.write()
        time.sleep(delay)
        i = i+1
        if i == numpixels+1:
            i = 0
print('runner(#pixels) is ready...')

def runner(numpixels, delay = 0.3):
    for i in range(numpixels):
        np.fill((0,0,0))
        np[i] = (0,30,30)
        np.write()
        utime.sleep(delay)

def runnerdemo():
    try:
        while True:
            runner(24, 0.2)
    except:
        off()

runnerdemo()
