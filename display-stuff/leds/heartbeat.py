# another blinking LED in micropython: heartbeat
# 2017-0805 PePo based upon Arduino code from
#           Python for Secret Agents Volume II, chapter 5, 2015
# Safari Online
###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import machine, time

print('hearbeat LED...')
led = machine.Pin(2, machine.Pin.OUT) #D8
led.on() # init led OFF
time.sleep(0.1) # wait
last = 0

# Blinks LED 13 once per second.
def heartbeat():
    global last
    now = time.ticks_ms() # get millisecond counter
    if now - last > 1000:
        led.off()
        last = now
    elif now - last > 900:
        led.on()

''' usage:
import heartbeat
heartbeat.demo() # loops internally forever!

# or as debugging tool:
while True:
    # other work comes here...
    heartbeat()
#'''
def demo():
    while True:
        heartbeat()
