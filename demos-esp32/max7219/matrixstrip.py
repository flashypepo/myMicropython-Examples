# interessante functies
# 2017-0522 PePo initial setup

import max7219
from machine import Pin, SPI
from time import sleep

# setup:

#LoLin32: MOSI=23, MISO=19, SCK=18, CC=15 (my selection)
spi = SPI(-1, 10000000, miso=Pin(19), mosi=Pin(23), sck=Pin(18))
display = max7219.Matrix8x8(spi, Pin(15))

# function segmenten(): zet de 'letters' per stuk aan/uit
# elke 'letter' bestaat uit 8-segmenten (x-variabele).
# Er zijn 8 'letters' (y-variabele). De telling is van rechts naar links
def segmenten(on=True, wt=0.1):
    # voor elke 'letter'
    for x in range(8):
        # elke segment in de 'letter'
        for y in range(8):
            display.pixel(y, x, on) # 'letter' y, 'segment' x
            display.show()
        sleep(wt)

# show some things with the whole strip
segmenten(False, 0) #immediately
segmenten(True, 0)
segmenten(False,0.4) # slow motion
segmenten(True, 0.4)

display.brightness(15)
sleep(1.0)
display.brightness(3)
segmenten(False, 0) #immediately
