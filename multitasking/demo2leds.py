# voorbeeld multitasking met 2 LEDS
# bron: YouTube
# 2017-1106 PePo new, based upon Youtube example
#   PROBLEM: module _thread doesnot exist anymore in MicroPython 1.9.3
from micropython import const  #added
import _thread as th
import time
from machine import Pin

LED1_PIN = const(12) #added WeMOS D1 mini
LED2_PIN = const(13) #added WeMOS D1 mini

led1 = Pin(LED1_PIN, Pin.OUT)
led2 = Pin(LED2_PIN, Pin.OUT)

# task 1
def task1(e):
    print('task1 running..'))
    while True:
        led1.value (not led1.value())
        time.sleep(e)
# task 2
def task2(e):
    print('task2 running..'))
    while True:
        led2.value (not led2.value())
        time.sleep(e)

#start the tasks...
th.start_new_thread(task1, (1,))
th.start_new_thread(task2, (.1,))
