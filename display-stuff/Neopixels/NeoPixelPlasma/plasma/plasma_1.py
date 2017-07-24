# plasma_1.py - implementation of oldskool plasma effect
# see http://www.bidouille.org/prog/plasma
#
# Building the plasma
# The plasma is basically a function on 2D space created
# by adding together a few sinusoids.
# By combining different types of sines and adding
# a time component the illusion of motion is achieved.
# Below are some examples of different types of sinusoids
# that we can use, and an illustration with and without
# the time component.
#
# 2017_0122 PePo new for Open Dag WF, using default library neopixel
#
# Sources: Youtube https://www.youtube.com/watch?v=QcyuYvyvOEI&index=14&list=PLuuAy8GJr5z1WoOJAFh1adr_yjCMJQ2Yl
# Tony Dicola source: https://gist.github.com/tdicola/6fe1fbc173dcd49de3a95be5fd9594f6

import machine
import math
import neopixel
import time

# 2017_0122 LED matrix: 8 * 8 pixels
PIXEL_WIDTH = 8
PIXEL_HEIGHT = 8
MAX_BRIGHT = 50.0 #100.0

np = neopixel.NeoPixel(machine.Pin(13), PIXEL_WIDTH*PIXEL_HEIGHT)

# Clear all the pixels and turn them off.
np.fill((0,0,0))
np.write()

# #####################################################
# stap 1:  individuele pixel
def stap1():
    np[0] = (255, 0, 0)  # red
    np[1] = (0, 255, 0)  # green
    np[2] = (0, 0, 255)  # blue
    np[3] = (255, 255, 255) # white
    np.write()
#stap1()

# #####################################################
# stap 2: eenvoudige animatie - a moving pixel ...
def stap2():
    while True:
        for i in range(PIXEL_WIDTH*PIXEL_HEIGHT):  #ga alle pixels langs
            np.fill((0, 0, 0))  # start met alle leds uit...
            np[i] = ((255,0,0)) # zet pixel op 'red'
            np.write() # update display, ofwel laat maar zien!
            time.sleep(0.35) #even wachten... / student in mijn tijd
            #time.sleep(0.1) #speed it up / moderne student...
#stap2()

# #####################################################
# stap 3: 1ste formule:  v = sin (x*10 + time)
# nodig: (x,y) en een tijd
def stap3():
    while True:
        np.fill((0, 0, 0))  # start met alle leds uit...
        current = time.ticks_ms() / 1000.0  # tijd in seconden
        for x in range(PIXEL_WIDTH):  # voor alle pixels langs x-as
            for y in range(PIXEL_HEIGHT):   # en alle pixels langs de y-as
                # bereken v (=intensity) voor elke pixel
                # eerst de formule, daarna ermee spelen, ofwel fine-tunen.
                #   website ernaast houden...
                #   10 -> 50: bredere band in de animatie
                #   10 -> 1: smallere band, meer overeenkomend met grootte matrix
                # v = math.sin(x * 10.0 + current)
                # v = math.sin(x * 50.0 + current) # brede band
                v = math.sin(x + current) # smalle band, andere richting
                # v = math.sin(x * 0.05 + current) # zeer brede witte band
                # calculate index in an array of pixels
                #   rij= y*PIXEL_WIDTH
                #   kolom = x
                #   index = rij * kolom (alle achter elkaar)
                # en intensiteit > 0, < 1
                #   sin: -1 .. 1 ==> 0 .. 2,
                #   dan schalen terug naar 0 .. 1
                v = (v + 1.0) / 2.0  # range: 0..1
                # alle kleuren dezelfde intensiteit v (als geheel getal)
                np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * v),
                                           int(MAX_BRIGHT * v),
                                           int(MAX_BRIGHT * v))
        np.write()
#stap3()

# #####################################################
# stap 4: 2de formule:
#     v = sin (10*(x*sin(time/2) + y*cos(time/3)) + time)
# nodig: wederom (x,y) en een tijd
def stap4():
    while True:
        np.fill((0, 0, 0))  # start met alle leds uit...
        current = time.ticks_ms() / 1000.0  # tijd in seconden
        for x in range(PIXEL_WIDTH):  # voor alle pixels langs x-as
            for y in range(PIXEL_HEIGHT):  # en alle pixels langs de y-as
                #v = math.sin(x + current)
                # value 10.0 -> 1.0: roteren duidelijker te zien
                # value 2.0 -> 20.0: langzamere rotatie
                # ORG: v = math.sin(10.0 * (x * math.sin(current / 2.0) + y * math.cos(current / 3.0)) + current)
                v = math.sin(1.0 * (x * math.sin(current / 0.5) + y * math.cos(current / 3.0)) + current)
                #v += math.sin(1.0 * (x * math.sin(current / 0.5) + y * math.cos(current / 0.25)) + current)
                v = (v + 1.0) / 2.0  # v in range: 0..1
                np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * v),
                                           int(MAX_BRIGHT * v),
                                           int(MAX_BRIGHT * v))
                # experimenten: alleen blauw / paars(red=MAX_BRIGHT) ...
                #np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT),
                #                           0,
                #                           int(MAX_BRIGHT * v))
        np.write()
#stap4()

# #####################################################
# stap 5: The last type of sinusoid we can use is a
# concentric sinusoid starting from a point,
# here we can also animate it and move the center point
# around in a Lissajous figure:
# cx = x + 0.5*sin(time/5)
# cy = y + 0.5*cos(time/3)
# v = sin(sqrt(100*(cx**2 + cy**2) + 1) + time)
def stap5():
    while True:
        np.fill((0, 0, 0))  # start met alle leds uit...
        current = time.ticks_ms() / 1000.0  # tijd in seconden
        for x in range(PIXEL_WIDTH):  # voor alle pixels langs x-as
            for y in range(PIXEL_HEIGHT):  # en alle pixels langs de y-as
                # v = math.sin(x + current)
                # v = math.sin(1.0 * (x * math.sin(current / 0.5) + y * math.cos(current / 3.0)) + current)
                # 0.5->1.5 - reversed(?) direction
                # 0.5 >waarden: hogere snelheid en meer wobbelen
                cx = x + 5.0 * math.sin(current / 5.0)
                cy = y + 3.0 * math.cos(current / 3.0)
                #ORG: v = math.sin(math.sqrt(100.0 * (math.pow(cx, 2.0) + math.pow(cy, 2.0)) + 1.0) + current)
                # scale factor 100.0 (larger pixel-displays) -> 1.0 (small displays)
                v = math.sin(math.sqrt((math.pow(cx, 2.0) + math.pow(cy, 2.0)) + 1.0) + current)
                # v += math.sin(math.sqrt((math.pow(cx, 2.0)+math.pow(cy, 2.0))+1.0)+current)

                v = (v + 1.0) / 2.0  # v in range: 0..1
                np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * v),
                                           int(MAX_BRIGHT * v),
                                           int(MAX_BRIGHT * v))
        np.write()
#stap5()

# #####################################################
# stap 6: We can then mix and match these functions
# and hopefully we get a nice plasma effect.
# Here I'm simply adding the 3 together....
def stap6():
    while True:
        np.fill((0, 0, 0))  # start met alle leds uit...
        current = time.ticks_ms() / 1000.0  # tijd in seconden
        for x in range(PIXEL_WIDTH):  # voor alle pixels langs x-as
            for y in range(PIXEL_HEIGHT):  # en alle pixels langs de y-as
                v = 0.0 # start met 0
                # tel erbij op alle stappen voor berekeningen van v..
                # moving + rotation + circular-thing
                v += math.sin(x + current)
                v += math.sin(1.0 * (x * math.sin(current / 0.5) + y * math.cos(current / 3.0)) + current)
                cx = x + 5.0 * math.sin(current / 5.0)
                cy = y + 3.0 * math.cos(current / 3.0)
                v += math.sin(math.sqrt((math.pow(cx, 2.0) + math.pow(cy, 2.0)) + 1.0) + current)
                # aanpassen de schaling want v nu tussen -3 en +3
                v = (v + 3.0) / 6.0  # v in range: 0..1
                np[y * PIXEL_WIDTH + x] = (int(MAX_BRIGHT * v),
                                           int(MAX_BRIGHT * v),
                                           int(MAX_BRIGHT * v))
        np.write()
#stap6()
