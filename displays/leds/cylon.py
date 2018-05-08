# ------------------------------------------------
# Name: Cylon / KnightRider Lights
# 2017_0514 PePo refactor sequenceCycle() and made demos cylon, knightrider and police
#   Police pattern: https://www.instructables.com/id/Police-Lights-With-Arduino/
#   TODO: (1) 10-LEDs array,
#   TODO: (2) adopt for Neopixel stick
#   TODO: (3) NeoPixel with sequence-value=intensity
#   TODO: (4) generic class Sequence ??
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

# Define GPIO signals to use that are connected to LEDs
# extends tuple, if necessary
ledGPIO = (16, 26, 19)


# define a list of LEDs based upon ledGPIO
def setupLeds(ledGPIO):
    print("Setup pins... ", ledGPIO)
    leds = []
    for pinRef in ledGPIO:
        ledPin = machine.Pin(pinRef, machine.Pin.OUT)  # pin is output
        leds.append(ledPin)
    print(leds)  # should be: [Pin(16), Pin(26), Pin(19)]
    return leds


leds = setupLeds(ledGPIO)


# define some led functions

# all LEDS on
def ledsOn(leds):
    '''all 3-LEDS on'''
    [leds[i].value(1) for i in range(len(leds))]


# all LEDS off
def ledsOff(leds):
    '''all 3-LEDS off'''
    [leds[i].value(0) for i in range(len(leds))]


# Define some sequences

# One LED
stepCount1 = 3  # 10
seq1 = []
seq1 = list(range(0, stepCount1))
seq1[0] = [1, 0, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq1[1] = [0, 1, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq1[2] = [0, 0, 1]  # , 0, 0, 0, 0, 0, 0, 0]
# seq1[3] = [0, 0, 0 ] #, 1, 0, 0, 0, 0, 0, 0]
# Seq1[4] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
# Seq1[5] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
# Seq1[6] = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
# Seq1[7] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# Seq1[8] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
# Seq1[9] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Double LEDs
stepCount2 = 4  # 11
seq2 = []
seq2 = list(range(0, stepCount2))
seq2[0] = [1, 0, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[1] = [1, 1, 0]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[2] = [0, 1, 1]  # , 0, 0, 0, 0, 0, 0, 0]
seq2[3] = [0, 0, 1]  # , 1, 0, 0, 0, 0, 0, 0]
# Seq2[4] = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
# Seq2[5] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
# Seq2[6] = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
# Seq2[7] = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]
# Seq2[8] = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
# Seq2[9] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
# Seq2[10] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

# Two LEDs from opposite ends
stepCount3 = 2  # 9
seq3 = []
seq3 = list(range(0, stepCount3))
seq3[0] = [1, 0, 1]
seq3[1] = [0, 1, 0]
# seq3[2] = [0, 0, 0]
# Seq3[0] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# Seq3[1] = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
# Seq3[2] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
# Seq3[3] = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
# Seq3[4] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
# Seq3[5] = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
# Seq3[6] = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
# Seq3[7] = [0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
# Seq3[8] = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]


# process one sequence
def processSequence(leds, seq, waitTime=0.2, verbose=False):
    '''process one complete sequence matrix'''

    # iterate through sequence...
    for k in range(len(seq)):

        # iterate through a row to set led on or off...
        if verbose:
            print("-- Step : " + str(k) + " --")

        for pinref in range(0, len(leds)):
            if verbose:
                print("-- pinRef=", pinref)
            led = leds[pinref]  # led
            # Check if LED should be on or off
            if seq[k][pinref] != 0:
                if verbose:
                    print(" Enable " + str(led))
                led.value(True)
            else:
                if verbose:
                    print(" Disable " + str(led))
                led.value(False)

        # Wait before moving on
        # 2017-0513: except for the last step to avoid double waiting time 
        # when processSequence is executed again
        if k < len(seq):
            time.sleep(waitTime)


# example
# processSequence(leds, seq1, 0.2, True)

# process sequence and then in reverse order, to show a complete cycle
# basically, this is one cylon/knightrider-type of light pattern
def sequenceCycle(leds, seq, waitTime=0.2, verbose=False):
    # process sequence in order of sequence seq
    processSequence(leds, seq, waitTime, verbose)

    # We reach the end of the sequence, so reverse the order
    # i.e. play the sequence in the other way
    seq.reverse()
    processSequence(leds, seq, waitTime, verbose)

    # restore original order
    seq.reverse()


# example
# for k in range(10):
#    sequenceCycle(leds, seq)

# demo: cylon pattern
def cylon(waitTime=0.1, n=10, verbose=False):
    '''demo cylon pattern.'''
    for k in range(n):
        sequenceCycle(leds, seq1, waitTime, verbose)

    if verbose:
        print('Cylon gone...')

    ledsOff(leds)  # leds off

#demo knightrider pattern
def knightrider(waitTime=0.1, n=10, verbose=False):
    '''demo Knightrider pattern.'''
    for k in range(n):
        sequenceCycle(leds, seq3, waitTime, verbose)

    if verbose:
        print('Knightrider gone...')

    ledsOff(leds)  # light out


# demo police pattern: 2 by 2 LEDs on/off
# based upon:

# part 1
stepCount4 = 5  # 9
seq4 = []
seq4 = list(range(0, stepCount4))
seq4[0] = [1, 0, 0]
seq4[1] = [1, 1, 0]
seq4[2] = [0, 1, 0]
seq4[3] = [0, 1, 1]
seq4[4] = [0, 0, 1]
#part 2
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

# run all demos...
def demo(waitTime=0.1, n=10, verbose=False):
    '''demo: runs all demos.'''
    print("Cylon pattern ...")
    cylon(waitTime, n, verbose)
    ledsOff(leds)  # leds off
    time.sleep(0.2)

    print("KnightRider pattern ...")
    knightrider(waitTime, n , verbose)
    ledsOff(leds)  # leds off
    time.sleep(0.2)

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

    print('demos done...')


print("Cylon package loaded")
print("usage: \nfrom cylon import *")
print("run: police(), cylon(), knightrider() or demo()")
