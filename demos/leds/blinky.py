# blinky.py - blink LED aan/uit 
# LED_PIN = 5: WeMOS-LoLin32, zie achterzijde van de development board
# LED_PIN = 4: NodeMCU

from machine import Pin
import time

LED_PIN = 15  # NodeMCU

led = Pin(LED_PIN, Pin.OUT)
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
