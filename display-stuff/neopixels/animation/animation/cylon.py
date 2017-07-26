# ------------------------------------------------
# Name: Cylon / KnightRider Lights
# 
# History
# 2017-0529 PePo: adopted for neopixel, using generic leds and pattern()
# 2017_0514 PePo refactor sequenceCycle() and made demos cylon, knightrider and police
#   Police pattern: https://www.instructables.com/id/Police-Lights-With-Arduino/
#
# TODO: 
#   (1) 10-LEDs array,
# √ (2) adopt for Neopixel stick
# √ (3) NeoPixel with sequence-value=intensity <- argument color!
#   (4) generic class Sequence ??
#
# 2017_0513 PePo new functions processSequence() and cylon().
#                Simplified processing of the sequence.
# 2017_0511 PePo adopted for WeMOS Lolin32
#           based upon Running Lights by matt.hawkins, 2012
# http://www.raspberrypi-spy.co.uk/2012/06/knight-rider-cylon-lights-for-the-raspberry-pi/

# Leuk idee voor Open Dag / demo:
# JBF techniek: Leds aansturen door functies te maken die led-combinaties gebruiken 
#               (led[i] AAN, led[j] UIT).
# BETER: essentie van de led-rij is een rij getallen waarvan '1' betekent 'led aan', 
#        en '0' 'led uit'. Gevolg is de reeks sequences (andere patronen). 
#        Dit heet een model van de applicatie maken (abstractie).
# GEVOLG: het abstraheren van de concrete gevallen (jargon: 'modelleren', levert een 
#       flexibeler programma op. In dit geval: zelfde algorithme, andere LED-animatie.

# Import required libraries
import machine
import time
import neopixel
import json

# development board configuration
# uncomment the hardware attached to development board

# '''  ############### NEOPIXEL STICK ##############
# 2017-0529 NodeMCU: neopixels attached to pin D5 (GPIO14)
NEOPIXEL_PIN = 14
DISPLAY_HEIGHT = 8
DISPLAY_WIDTH = 1
PIXEL_PIN = machine.Pin(NEOPIXEL_PIN, machine.Pin.OUT)
leds = neopixel.NeoPixel(PIXEL_PIN, DISPLAY_HEIGHT)
# all leds off
def ledsOff(lights):
    lights.fill( (0, 0, 0) ) 
    lights.write()
    
ledsOff(leds)  # blank all neopixels

# function to color a neopixel at (x, y)
# color = (rgb, rgb, rgb)
def draw_pixel(x, y, color):
    #print('x=', x, ' y=', y, ' color=', color)
    leds[ (y * DISPLAY_HEIGHT + x) ] = color
    leds.write()

# Define some sequences for 3-lEDS
# One LED
stepCount1 = 8
seq1 = []
seq1 = list(range(0, stepCount1))
seq1[0] = [1, 0, 0, 0, 0, 0, 0, 0]
seq1[1] = [0, 1, 0, 0, 0, 0, 0, 0]
seq1[2] = [0, 0, 1, 0, 0, 0, 0, 0]
seq1[3] = [0, 0, 0, 1, 0, 0, 0, 0]
seq1[4] = [0, 0, 0, 0, 1, 0, 0, 0]
seq1[5] = [0, 0, 0, 0, 0, 1, 0, 0]
seq1[6] = [0, 0, 0, 0, 0, 0, 1, 0]
seq1[7] = [0, 0, 0, 0, 0, 0, 0, 1]


'''
# Double LEDs
stepCount2 = 4  # 11
seq2 = []
seq2 = list(range(0, stepCount2))
seq2[0] = [1, 0, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[1] = [1, 1, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[2] = [0, 1, 1]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[3] = [0, 0, 1]  # , 1, 0, 0, 0, 0, 0, 0]
'''

# Two LEDs from opposite ends
stepCount3 = 4
seq3 = []
seq3 = list(range(0, stepCount3))
seq3[0] = [1, 0, 0, 0, 0, 0, 0, 1]
seq3[1] = [0, 1, 0, 0, 0, 0, 1, 0]
seq3[2] = [0, 0, 1, 0, 0, 1, 0, 0]
seq3[3] = [0, 0, 0, 1, 1, 0, 0, 0]
   
############### / NEOPIXEL STICK ############## 
# '''

''' ############## array of Leds attached to pins #############
# Define GPIO signals to use that are connected to LEDs
# extends tuple, if necessary
ledGPIO = (16, 26, 19)
DISPLAY_HEIGHT = 3
DISPLAY_WIDTH = 1

# define a list of LEDs based upon ledGPIO
print("Setup pins... ", ledGPIO)
leds = []
for pinRef in ledGPIO:
    ledPin = machine.Pin(pinRef, machine.Pin.OUT)  # pin is output
    leds.append(ledPin)
print(leds)  # should be: [Pin(16), Pin(26), Pin(19)]

# function to color a LED at (x, y)
# color = (0,0,0) for OFF, (1,1,1) for ON
def draw_pixel(x, y, color):
    if color == (0, 0, 0):
        on = FALSE
    else:
        on = True
    leds[y * DISPLAY_HEIGHT + x, DISPLAY_WIDTH].value(on)

# define some led functions
# all LEDS on
def ledsOn(leds):
    # all 3-LEDS on
    [leds[i].value(1) for i in range(len(leds))]


# all LEDS off
def ledsOff(leds):
    # all 3-LEDS off
    [leds[i].value(0) for i in range(len(leds))]

# Define some sequences for 3-lEDS

# One LED
stepCount1 = 3
seq1 = []
seq1 = list(range(0, stepCount1))
seq1[0] = [1, 0, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq1[1] = [0, 1, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq1[2] = [0, 0, 1]  # , 0, 0, 0, 0, 0, 0, 0]

# Double LEDs
stepCount2 = 4
seq2 = []
seq2 = list(range(0, stepCount2))
seq2[0] = [1, 0, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[1] = [1, 1, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[2] = [0, 1, 1]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[3] = [0, 0, 1]  # , 1, 0, 0, 0, 0, 0, 0]

# Two LEDs from opposite ends
stepCount3 = 2
seq3 = []
seq3 = list(range(0, stepCount3))
seq3[0] = [1, 0, 1]
seq3[1] = [0, 1, 0]

############## / array of Leds attached to pins ############# 
'''

# process one sequence
color = (25, 25, 25) # default color
def processSequence(leds, seq, c, waitTime=0.2, verbose=False):
    '''process one complete sequence matrix'''

    # iterate through sequence...
    for step in range(len(seq)):

        # iterate through a row to set led on or off...
        if verbose:
            print("-- Step : " + str(step) + " --")

        #for pinref in range(0, len(leds)):
        for pinref in range(0, len(seq[step])):
            if verbose:
                print("-- pinRef=", pinref)
            #led = leds[pinref]  # led
            # Check if LED should be on or off
            if seq[step][pinref] != 0:
                if verbose:
                    print(" Enable " + str(step*pinref))
                #led.value(True)
                draw_pixel(pinref, 0, c)
            else:
                if verbose:
                    print(" Disable " + str(step*pinref))
                draw_pixel(pinref, 0, (0, 0, 0))
                #led.value(False)

        # Wait before moving on
        # 2017-0513: except for the last step to avoid double waiting time 
        # when processSequence is executed again
        if step < len(seq):
            time.sleep(waitTime)


# example
# processSequence(leds, seq1, 0.2, True)

# process sequence and then in reverse order, to show a complete cycle
# basically, this is one cylon/knightrider-type of light pattern
def sequenceCycle(leds, seq, c, waitTime=0.2, verbose=False):
    # process sequence in order of sequence seq
    processSequence(leds, seq, c, waitTime, verbose)

    # We reach the end of the sequence, so reverse the order
    # i.e. play the sequence in the other way
    seq.reverse()
    processSequence(leds, seq, c, waitTime, verbose)

    # restore original order
    seq.reverse()


# example
# for k in range(10):
#    sequenceCycle(leds, seq)

# generic pattern
# color = color
def pattern(leds, seq, c=color, n=10, waitTime=0.1, verbose=False):
    '''demo cylon pattern.'''
    for k in range(n):
        sequenceCycle(leds, seq, c, waitTime, verbose)

    if verbose:
        print('Cylon gone...')

    ledsOff(leds)  # leds off

# knightrider pattern
def knightrider(leds, c=color, n=10, waitTime=0.1, verbose=False):
    pattern(leds, seq3, c, n, waitTime, verbose)

# cylon pattern
def cylon(leds, c=color, n=10, waitTime=0.1, verbose=False):
    pattern(leds, seq1, c, n, waitTime, verbose)

# demo police pattern: 2 by 2 LEDs on/off
# based upon:

# part 1
stepCount4 = 9
seq4 = []
seq4 = list(range(0, stepCount4))
seq4[0] = [1, 0, 0, 0, 0, 0, 0, 0]
seq4[1] = [1, 1, 0, 0, 0, 0, 0, 0]
seq4[2] = [0, 1, 1, 0, 0, 0, 0, 0]
seq4[3] = [0, 0, 1, 1, 0, 0, 0, 0]
seq4[4] = [0, 0, 0, 1, 1, 0, 0, 0]
seq4[5] = [0, 0, 0, 0, 1, 1, 0, 0]
seq4[6] = [0, 0, 0, 0, 0, 1, 1, 0]
seq4[7] = [0, 0, 0, 0, 0, 0, 1, 1]
seq4[8] = [0, 0, 0, 0, 0, 0, 0, 1]
#part 2
''' TODO - police pattern
stepCount5 = 3
seq5 = []
seq5 = list(range(0, stepCount5))
seq5[0] = [1, 1, 0]
seq5[1] = [0, 0, 0]
seq5[2] = [0, 1, 1]

def police(n1=15, n2=30, n3=50, verbose=False):
    for k in range(n1):
        sequenceCycle(leds, seq4, 0.05, verbose)
    time.sleep(0.1)

    for k in range(n2):
        sequenceCycle(leds, seq4, 0.02, verbose)
    time.sleep(0.1)

    for k in range(n3):
        sequenceCycle(leds, seq5, 0.04, verbose)

    if verbose:
        print('Police gone...')

    ledsOff(leds)  # light out
'''
# run all demos...
# pre-conditions: leds is not empty
def demo(c=color, n=10, waitTime=0.1, verbose=False):
    '''demo: runs all demos.'''
    print("Cylon pattern ...")
    cylon(leds, c, n, waitTime, verbose)
    ledsOff(leds)  # leds off
    time.sleep(0.2)

    print("KnightRider pattern ...")
    knightrider(leds, c, n, waitTime, verbose)
    ledsOff(leds)  # leds off
    time.sleep(0.2)
    ''' TODO
    print("Police pattern ...")
    #police(n1=15, n2=30, n3=50, verbose=False)
    police()  # mhh, different arguments than the other demos
    ledsOff(leds)  # leds off
    time.sleep(0.2)

    print("pattern #1 ...")
    for k in range(n):
        sequenceCycle(leds, seq1, waitTime, verbose)
    ledsOff(leds)  # leds off
    time.sleep(0.2)

    print("pattern #2 ...")
    for k in range(n):
        sequenceCycle(leds, seq2, waitTime, verbose)
    ledsOff(leds)  # leds off
    time.sleep(0.2)
    '''
    print('demos done...')


print("Cylon package loaded")
print("usage: \nfrom cylon import *")
print("run: police(), cylon(), knightrider() or demo()")
