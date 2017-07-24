# LED_Breathing in micropython
#
# bron:
# LED_Breathing.ino Arduining.com  20 AUG 2015
# Using NodeMCU Development Kit V1.0
# Going beyond Blink sketch to see the blue LED breathing.
#  https://arduinin.com/2015/08/20/nodemcu-breathing-led-with-arduino-ide/g

import machine
import time

LEDPin = 5 #16 # NodeMCU D0 / GPIO16
BRIGHT = 350 #max LED intensity (1-500)
INHALE = 1250 #inhalation time in millisec
PULSE = INHALE * 1000 / BRIGHT
REST = 1000 # rest between inhalations

# Setup
pin = machine.Pin(16, machine.Pin.OUT)
pwm5 = machine.PWM(pin, freq=500, duty=512)
print(pin.value())

# Loop
while True:
    # ramp increasing intensity, inhalation
    for i in range(1, BRIGHT):
        #print(i)
        pin.low() # LED on
        time.sleep_ms(i * 10)
        pin.high() # LED off
        print(int(PULSE - i * 10) // 1000)
        time.sleep_ms(int(PULSE - i * 10) // 1000)
        time.sleep_ms(0) # to prevent watchdog firing(?)

    # ramp decreasing intensity, exhalation (half time)
    for i in range(BRIGHT -1, 1, -1):
        print(i)
        pin.low() # LED on
        time.sleep_ms(i * 10)
        pin.high() # LED off
        #time.sleep_ms(int(PULSE - i * 10))
        i = i-1
        time.sleep_ms(0)

    time.sleep_ms(REST)
