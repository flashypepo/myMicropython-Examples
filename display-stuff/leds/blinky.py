# blinky.py - blink LED aan/uit 
# _LED_PIN = 5: WeMOS-LoLin32, zie achterzijde van de development board
# _LED_PIN = 4: NodeMCU
# _LED_PIN = 2: WeMOS D1 R2, 2017_0728

from machine import Pin
import time

#_LED_PIN = 15  # NodeMCU
_LED_PIN = 2  # WeMOS D1 R2 / ESP8266

led = Pin(_LED_PIN, Pin.OUT)

''' micropython 1.8.7+: led.on() and led.off()
def off():
    led.value(0) # led off
# start led off
off()
for i in range(10):
   led.value(0)
   time.sleep(0.25)
   led.value(1)
   time.sleep(0.25)
# end led off
off() 
'''
def blink(dt=0.1):
    led.on()
    time.sleep(dt)
    led.off()
    time.sleep(dt)

#while True:
for i in range(10):
    #blink()
    blink(0.2)
    
led.on() #WeMOS D1 R2, pulldown!
#led.off() #otherwise
print('done!')
