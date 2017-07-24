# blinky.py - blink LED aan/uit op WeMOS - LoLin32
# LED_BUILTIN = 5, zie achterzijde van de development board

from machine import Pin
import time

led = Pin(5, Pin.OUT)
led.value(1) # led off

for i in range(10):
   led.value(0)
   time.sleep(0.25)
   led.value(1)
   time.sleep(0.25)
