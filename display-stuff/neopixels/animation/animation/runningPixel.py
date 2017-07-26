# runningPixel.py - a neopixel iteration
# 2017_0204 PePo Feather NeoPixel matrix, 8*4, GPIO15

import machine
import neopixel
import time

PIXEL_WIDTH = 24+8 # length or width of Neopixel device
PIXEL_HEIGHT =1 #4 height of Neopixel device
MAX_BRIGHT = 50.0 # 0 .. 255.0
PIXEL_PIN = 15 #Neopixel DIN

np = neopixel.NeoPixel(machine.Pin(PIXEL_PIN), PIXEL_WIDTH*PIXEL_HEIGHT)

# Clear all the pixels and turn them off.
np.fill((0,0,0))
np.write()

# pixel function
def np_pixel(x, y, color):
    np[y*PIXEL_WIDTH + x] = color

# #####################################################
# stap 1:  individuele pixel
# # <editor-fold desc="Individuel Pixels">
#def stap1():
#    np[0] = (255, 0, 0)  # red
#    np[1] = (0, 255, 0)  # green
#    np[2] = (0, 0, 255)  # blue
#    np[3] = (255, 255, 255) # white
#    np.write()
# </editor-fold>
#stap1()

# #####################################################
# stap 2: eenvoudige animatie - a moving pixel ...
# <editor-fold desc="Running neopixel">
def stap2():
    while True:
        for i in range(PIXEL_WIDTH*PIXEL_HEIGHT):  #ga alle pixels langs
            np.fill((0, 0, 0))  # start met alle leds uit...
            np[i] = ((255,0,0)) # zet pixel op 'red'
            np.write() # update display, ofwel laat maar zien!
            time.sleep(0.35) #even wachten... / student in mijn tijd
            #time.sleep(0.1) #speed it up / moderne student...
#stap2()
# </editor-fold>

def stap3():
    while True:
        for y in range(PIXEL_HEIGHT):
            for x in range (PIXEL_WIDTH):
                np.fill((0, 0, 0))  # start met alle leds uit...
                np_pixel(x, y, (int(MAX_BRIGHT), 0, 0))
                np.write()
                time.sleep(0.1)
#stap3()

# fancier demo: up- and down running lights - cool
# <editor-fold desc="Running UP and DOWN">
def stap4():
    while True:
        for y in range(PIXEL_HEIGHT):
            for x in range(PIXEL_WIDTH):
                np.fill((0, 0, 0))
                np_pixel(x, y, (0, int(MAX_BRIGHT), 0)) #going up
                np_pixel(PIXEL_WIDTH - 1 - x, PIXEL_HEIGHT - 1 - y, (int(MAX_BRIGHT), 0, 0)) #going down
                if ( x == y):
                    np_pixel(x, y, (255, 255, 255))
                np.write()
                time.sleep(0.1) #fast
        np.fill((0,0,0))
        np.write()
stap4()
# </editor-fold>
