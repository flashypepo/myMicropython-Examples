# Blinking LED on NodeMCU, led = GPIO16
# 2017-0724 PePo new
import machine
import time

def blinkled():
    #  create builtin LED connected to pin D16 = GPIO16 on NodeMCU V3
    led = machine.Pin(16, machine.Pin.OUT)
    ledState = False # led off
    # toggle led 10x
    for i in range(30):
        if ledState:
            led.on() # led on
        else:
            led.off() # led off
        time.sleep(0.1) # 1 sec delay
        ledState =  not ledState
