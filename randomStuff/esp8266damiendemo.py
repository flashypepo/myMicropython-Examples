#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Micropython code from Damien on YouTube
     https://www.youtube.com/watch?v=_voIwFB4mu0&t=8s

Created on Sun May 28 17:09:11 2017
@author: pepo
"""

# define neopixel stick
# Huzzah: DIN = pin 14
import machine
pin = machine.Pin(14, machine.Pin.OUT)

import neopixel
np = neopixel.NeoPixel(pin, 8)

# first neopixel: RED, dimmed (brightness: 0..255)
np[0] = (25,0,0)
np.write()

# list colors of np
list(np)

# define pixel-write function
PIXEL_WIDTH = 8
def np_pixel(x, y, color):
    np[y*PIXEL_WIDTH + x] = color

# define blank neopixel function
def blank():
    np.fill( (0, 0, 0) )
    np.write()

# running led
import time
for i in range(8):
    np.fill((0,0,0))
    np[i] = ((0,255,0))
    np.write()
    time.sleep(0.35)
blank()

# two opposite running leds .. for ever
# np = neopixels, no = number of pixels, wt = sleep-time
def demo_pixels(np, no = 8, wt = 0.2):
    while True:
        for i in range(no):
            np.fill((0,0,0))
            np[i] = (0,25,0)
            np[7-i] = (0,0,25)
            np.write()
            time.sleep(wt)
demo_pixels(np) # for 8-pixel stick, waiting time=0.2


# demo Damien to get weather data requires a network connection and API-key

###### PRE_CONDITION: connected to netwerk, and having an API-key

# generated key for micropython test on OpenweaterData site
####### KEEP THIS SECRET ######
# API-key. After generating a new key, you must wait 10 minutes
key = 'cac77abc97ceafbe446a455019c247fe'
####### / KEEP THIS SECRET ######

import network

def connect2wifi(ssid, passcode):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network... ', ssid)
        sta_if.active(True)
        sta_if.connect(ssid, passcode)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

connect2wifi('PePoDevNet', '5t2!V99*')

######### / endof pre-condition

# connect to OpenWeatherData with socket and API-key
import socket
s = socket.socket()
addr = socket.getaddrinfo('api.openweathermap.org', 80)
addr

# connect to IP
s.connect(addr[0][4])

# send request for city, using key
#OK: s.send(b'GET http://api.openweathermap.org/data/2.5/weather?q=London&appid=%s HTTP/1.0\r\n\r\n' % key)
#117: s.send(b'GET http://api.openweathermap.org/data/2.5/weather?q=Amsterdam,nl&appid=%s HTTP/1.0\r\n\r\n' % key)
s.send(b'GET http://api.openweathermap.org/data/2.5/weather?q=Amsterdam,nl&appid=cac77abc97ceafbe446a455019c247fe')
#s.send(b'GET http://api.openweathermap.org/data/2.5/weather?q=Amsterdam,nl&appid=[0] HTTP/1.0\r\n\r\n'.format(key))
# should return '111'  ???

# show received data -- first 1000 chars
s.recv(1000)
# output...

# stange, new way, to save data in variable html, but it works...
html = _
html

# split data in dictionary
html.split(b'\r\n\r\n')

_[-1] # show last element, which is the data we want
# save in variable data
data = _
data

import json
json.loads(data)
# .... list of json-data

# save
data = _

# get the temperature ...
data['main']['temp'] # temp in Kelvin

data['main']['temp'] - 273.15     # temp in celsius
