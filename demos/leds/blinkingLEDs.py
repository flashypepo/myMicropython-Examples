# Example of blinking leds in micropython
# Arduino style: setup and loop
# 2017_0708 PePo - NodeMCU + led-bar
# 2016_1002 PePo - Grove-LEDs on D1 (GPIO5) and D5 (GPIO14)
# 2016-0823 PePo, based upon https://learn.adafruit.com/micropython-basics-blink-a-led/blink-led

###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import machine as board # CircuitPython-style
import time

#title
print('Blinking LEDs...') 

#configuration
pins = [15, 13, 12, 14, 10] # NodeMCU: D8, D7, D6, D5, SD3/D4(2)
# fill array of leds
leds = [] 
for pin in pins:
    leds.append(board.Pin(pin, board.Pin.OUT))

# leds on up until n
def tuneUp(n):
    '''leds until n on'''
    # first, put all leds off
    '''for led in leds:
        led.off()'''
    # light leds up to n
    # check maximum number of leds
    if n > len(leds):
        n = len(leds)
    for i in range(n):
        leds[i].on()
        time.sleep(0.1)

def tuneDown(n):
    '''leds off from n downwards'''
    # check maximum number of leds
    if n > len(leds):
        n = len(leds)
    for i in (reversed(range(0,n))):
        leds[i].off()
        time.sleep(0.1)
    
def off():
    '''all leds off'''
    for led in leds:
        led.off()

#leds on in order
import urandom as random
def demo_bar(w = 2.0):
    try:
        while True:
            off()
            n = random.getrandbits(3)# len(leds)+1
            if n > (len(leds) + 1):
                n = len(leds)+1
            #print('LEDs on up to {} ...'.format(n))
            tuneUp(n)
            time.sleep(w)
            #print('LEDs off from {} ...'.format(n))
            tuneDown(n)
    except KeyboardInterrupt:
        print('done!')
        off()
demo_bar(0.5)

''' TODO
while True:
    ###################################################################
    # Loop code goes inside the loop here, this is called repeatedly: #
    ###################################################################
    led1.high()
    led2.low()
    time.sleep(0.5)
    led1.low()
    led2.high()
    time.sleep(0.5)
'''
print('done')
