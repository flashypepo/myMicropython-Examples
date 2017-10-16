# Example of a blinking led in micropython
# source: https://www.aliexpress.com/item/TPYBoard-v202-pyboard-micropython-development-board-ESP8266-python-Lua/32820901786.html
# 2017-0725 PePo

###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import machine
import time, math

print('Pulse LED...')

_LEDPIN = 13 #13=TTGO ESP32, 5=WeMOS_Lolin32 2=Lolin_OLED, 2=WeMOS_D1R2

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

def cleanup():
    global led
    led.duty(1023) #WeMOS_D1/R2: off due pullUp
    time.sleep(0.1) #waiT
    led.deinit() #deinit
    del led #remove

led = machine.PWM(machine.Pin(_LEDPIN), freq=10000)

###################################################################
# Loop code goes inside the loop here, this is called repeatedly: #
###################################################################
#for i in range(20):
while True:
    pulse(led, 20)
cleanup()
