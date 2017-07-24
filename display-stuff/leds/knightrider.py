# ------------------------------------------------
# Name: KnightRider Lights
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

# Define GPIO signals to use that are connected to LEDs
# extends tuple, if necessary
ledGPIO = (16, 26, 19)

# define a list of LEDs based upon ledGPIO
def setupLeds(ledGPIO):
    print("Setup pins... ", ledGPIO)
    leds = []
    for pinRef in ledGPIO:
        ledPin = machine.Pin(pinRef, machine.Pin.OUT)#pin is output
        leds.append(ledPin)
    print(leds) # should be: [Pin(16), Pin(26), Pin(19)]
    return leds

leds = setupLeds(ledGPIO)

# define some led functions

# all LEDS on
def ledsOn(leds):
    '''all 3-LEDS on'''
    [leds[i].value(1) for i in range(len(leds))]
    # traditional
    #for i in range(len(leds)):
    #    leds[i].value(1)

# all LEDS off
def ledsOff(leds):
    '''all 3-LEDS off'''
    [leds[i].value(0) for i in range(len(leds))]
    #traditional
    # for i in range(len(leds)):
    #     leds[i].value(0)

# Define some sequences

# One LED
stepCount1 = 3 #10
seq1 = []
seq1 = list(range(0, stepCount1))
seq1[0] = [1, 0, 0 ] #, 0, 0, 0, 0, 0, 0, 0]
seq1[1] = [0, 1, 0 ] #, 0, 0, 0, 0, 0, 0, 0]
seq1[2] = [0, 0, 1 ] #, 0, 0, 0, 0, 0, 0, 0]
#seq1[3] = [0, 0, 0 ] #, 1, 0, 0, 0, 0, 0, 0]
# Seq1[4] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# Seq1[5] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
# Seq1[6] = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
# Seq1[7] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# Seq1[8] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# Seq1[9] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Double LEDs
stepCount2 = 4 #11
seq2 = []
seq2 = list(range(0, stepCount2))
seq2[0] = [1, 0, 0] #, 0, 0, 0, 0, 0, 0, 0]
seq2[1] = [1, 1, 0] #, 0, 0, 0, 0, 0, 0, 0]
seq2[2] = [0, 1, 1] #, 0, 0, 0, 0, 0, 0, 0]
seq2[3] = [0, 0, 1] #, 1, 0, 0, 0, 0, 0, 0]
# Seq2[4] = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
# Seq2[5] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
# Seq2[6] = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
# Seq2[7] = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
# Seq2[8] = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
# Seq2[9] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
# Seq2[10] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Two LEDs from opposite ends
stepCount3 = 2 #9
seq3 = []
seq3 = list(range(0, stepCount3))
seq3[0] = [1, 0, 1]
seq3[1] = [0, 1, 0]
#seq3[2] = [0, 0, 0]
# Seq3[0] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# Seq3[1] = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
# Seq3[2] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
# Seq3[3] = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
# Seq3[4] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
# Seq3[5] = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
# Seq3[6] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
# Seq3[7] = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
# Seq3[8] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]


# Define some settings
seq = seq3
stepCount = stepCount3
stepCounter = 0
stepDir = 1
waitTime = 0.2
verbose = False

# define a cylon funtion
# uses global vars because it must be claled repeatedly
# TODO: make a self-contained function, probably a state machine.
def cylon(n):
    '''cylon light pattern'''
    global leds, seq, stepCount, stepCounter, stepDir, waitTime, verbose

    #while True:
    for i in range (n):
        if verbose:
            print("-- Step : " + str(stepCounter) + " --")

        for pinref in range(0, len(leds)):
            if verbose:
                print("-- pinRef=" , pinref)
            led = leds[pinref]  #led
            # Check if LED should be on or off
            if seq[stepCounter][pinref] != 0:
                if verbose:
                    print(" Enable " + str(led))
                led.value(True)
            else:
                if verbose:
                    print(" Disable " + str(led))
                led.value(False)

        stepCounter += stepDir

        # If we reach the end of the sequence reverse
        # the direction and step the other way
        if (stepCounter == stepCount) or (stepCounter < 0):
            stepDir = stepDir * -1
            stepCounter = stepCounter + stepDir + stepDir

        # Wait before moving on
        time.sleep(waitTime)

# define a function which sets required globals
# leds is already defined
def cylonLight(seqn, stepCnt, n, w=0.2, v=False):
    '''setup globals, except leds, and run cylon'''
    # Define some settings, global because cylon() makes use of them
    global seq, stepCount, stepCounter, stepDir, waitTime, verbose
    seq = seqn
    stepCount = stepCnt
    stepCounter = 0
    stepDir = 1
    waitTime = w
    verbose = v

    # main loop
    #while True:
    cylon(n)

# samples
def sample():
    '''sample: runs 3 sequences and then turns leds off.'''
    cylonLight(seq1, len(seq1), 50)
    cylonLight(seq2, len(seq2), 50)
    cylonLight(seq3, len(seq3), 50)
    print('Cylon gone...')
    ledsOff(leds) # light out

print("Knightrider/Cylon packages loaded")
print("usage: \nfrom knightrider import *")
print("sample()")
