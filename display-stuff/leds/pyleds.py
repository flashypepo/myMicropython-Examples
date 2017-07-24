# device= WeMOS Lolin32 v1.0.0
# 2017-0511 PePo new, some led experiments Grove 3-LEDS prototype
#

#the 3-LEDS attached pins
ledPins = [16,26,19]

# generate LED list
leds = []
for i in range(2):
    leds[i] = machine.Pin(ledPins[i], machine.Pin.OUT)
print(leds) # should be: [Pin(16), Pin(26), Pin(19)]

# all LEDS on
def ledsOn(leds):
    '''all 3-LEDS on'''
    [leds[i].value(1) for i in range(len(leds))]

    # traditional
    #for i in range(len(leds)):
    #    leds[i].value(1)

# all LEDS on
def ledsOff(leds):
    '''all 3-LEDS off'''
    [leds[i].value(0) for i in range(len(leds))]

    #traditional
    # for i in range(len(leds)):
    #     leds[i].value(0)

import time

# blinky for 3-LEDS
def blinky (leds, n, d):
    '''blinks 3-LEDS at the same time'''
    for i in range(n):
        ledsOn(leds)
        time.sleep(d)
        ledsOff(leds)
        time.sleep(d)

blinky(leds, 10, 0.1)

# set LED n on, others cleared
def ledOnAt(leds, p):
    '''set LED n on, others cleared'''
    if (p<0) or (p>(len(leds)-1)):
        print("LED doesn't exists. Abort")
        return
    ledsOff(leds) # clear all leds
    leds[p].value(1) # led p on

# set LED n off, others cleared
def ledOffAt(leds, p):
    '''set LED n off, others cleared'''
    if (p<0) or (p>(len(leds)-1)):
        print("LED doesn't exists. Abort")
        return
    ledsOff(leds) # clear all leds
    leds[p].value(0)


# turn led on from 0 to #leds
def ledsUp(leds, d=0.5):
    '''turn led on from 0 to #leds'''
    for i in range(len(leds)):
        ledOnAt(leds, i)
        time.sleep(d)


# turn led on from #leds to 0
def ledsDown(leds, d=0.5):
    '''turn led on from #leds to 0'''
    leds.reverse() # reverse array
    for i in range(len(leds)):
        ledOnAt(leds, i)
        time.sleep(d)
    leds.reverse() # restore original leds-list

# Knightrider lighting
# also known as Cylon lighting
def knightRider(leds, n=10, d=0.1):
    '''KnightRider / Ceylon lighting'''
    for i in range(n):
        ledsUp(leds,d)
        ledsDown(leds,d)
    ledsOff(leds)
