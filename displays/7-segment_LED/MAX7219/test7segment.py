# test7segment.py - tests for using the two 7-segments driven by Max7219
# 2017-0525 PePo: setting up SPI and class Max7219
#
# Note: I've changed class max7219.Matrix8x8, because a Pin in
# ESP32 micropython does not have a method low(). I used value(T|F).
# That works.
# GitHub documentatie:
#    https://github.com/adafruit/micropython-adafruit-max7219/blob/master/docs/examples.rst
# GitHub code Max7219 (originele code):
#    https://github.com/adafruit/micropython-adafruit-max7219/blob/master/max7219.py

import max7219
from machine import Pin, SPI

#LoLin32: MOSI=23, MISO=19, SCK=18, CC=15 (my selection)
spi = SPI(-1, 10000000, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
display = max7219.Matrix8x8(spi, Pin(15))
# display shows some random stuff, so it reacts on the code

display.fill(True)
display.pixel(4,4,False)
display.show()
# almost all segments are lighted, not sure I understand it.

# all segments turned off:
for x in range(8):
    for y in range(8):
        display.pixel(x, y, False)
        display.show()

# all segments turned on:
for x in range(8):
    for y in range(8):
        display.pixel(x, y, True)
        display.show()

# nice to see the order in which segments are turned off
from time import sleep
for x in range(8):
    for y in range(8):
        display.pixel(x, y, False)
        display.show()
        sleep(0.8)

# In de volgende code gaan de segmenten per 'letter' uit!
# Interesant...
for x in range(8):
    for y in range(8):
        display.pixel(y, x, False) # x verwisselt met y - per 'letter'
        display.show()
        sleep(0.8)

# brightness werkt ook:
display.brightness(1) # lage intensiteit
display.brightness(15) # hoge intensiteit

# leuke functie om segmenten aan of uit te zetten
def segmenten(on=True, wt=0.1):
     for x in range(8):
        for y in range(8):
            display.pixel(y,x,on)
            display.show()
            sleep(wt)

segmenten(True) # segmenten aan met tijdvertraging
segmenten(False, 0) # segmenten uit asap

# Wat weet ik tot nu toe?
# elke 'letter' bestaat uit 8-segmenten (x-variabele).
# Er zijn 8 'letters' (y-variabele). De telling is van rechts naar links
# Met volgende code gaan de 'letters' per stuk aan/uit
def segmenten(on=True, wt=0.1):
    # voor elke 'letter'
    for x in range(8):
        # elke segment in de 'letter'
        for y in range(8):
            display.pixel(y, x, on) # 'letter' y, 'segment' x
            display.show()
        sleep(wt)

#
# TODO: letters en getallen weergeven
# verder kijken o.a. bij Kevin Darrah - https://youtu.be/fBgvyW5t50g
# die de 7-segment matrix met de max7219 uitlegt op basis van Arduino code
# (en SPI): '7 Segment Displays & Arduino the EASY way! with MAX7219 Driver'
# by Kevin Darrah, https://youtu.be/fBgvyW5t50g
# of het 'easy' is weet ik niet ;-)
