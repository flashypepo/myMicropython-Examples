# Example of a blinking led in micropython
# source: https://www.aliexpress.com/item/TPYBoard-v202-pyboard-micropython-development-board-ESP8266-python-Lua/32820901786.html
# 2017-0725 PePo

###########################################################################
# Setup code goes below, this is called once at the start of the program: #
###########################################################################
import machine
import time, math

_LEDPIN = 5 #5=WeMOS_Lolin32 2=Lolin_OLED

print('Pulse LED...')
led = machine.PWM(machine.Pin(_LEDPIN), freq=1000)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)

###################################################################
# Loop code goes inside the loop here, this is called repeatedly: #
###################################################################
while True:
    pulse(led, 100)
