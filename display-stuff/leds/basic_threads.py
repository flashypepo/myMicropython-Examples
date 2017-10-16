# example basic multi-tasking
# 2017-0903 PePo based upon https://youtu.be/iyoS9aSiDWg
# 3 LED's connected on WeMOS-OLED ESP32
# ESP32 micropython 1.9.1 version 20170903
from micropython import const
import _thread as th
import time
import machine

# specify LEDs
LED1_PIN = const(12)
LED2_PIN = const(13)
LED3_PIN = const(15)
led1 = machine.Pin(LED1_PIN, machine.Pin.OUT)
led2 = machine.Pin(LED2_PIN, machine.Pin.OUT)
led3 = machine.Pin(LED3_PIN, machine.Pin.OUT)

#specify a task for each LED
def loop_led1(e):
	while True:
		led1.value(not led1.value())
		time.sleep(e)

def loop_led2(e):
	while True:
		led2.value(not led2.value())
		time.sleep(e)

def loop_led3(e):
	while True:
		led3.value(not led3.value())
		time.sleep(e)

# activate the tasks simultaneously
th.start_new_thread(loop_led1, (1.0,)) # blink nominal
th.start_new_thread(loop_led2, (.5,))   # blink faster
th.start_new_thread(loop_led3, (.1,))  # blink fastest
