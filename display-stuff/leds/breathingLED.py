# LED_Breathing in micropython
#   trial-and-error for BRIGHT and wait
#   Uses D1 / /GPIO05 with PWM
# by PePo 2017_0325, based upon idea from ardunaut
#
# Source:
# LED_Breathing.ino Arduining.com  20 AUG 2015, by ardunaut
# Using NodeMCU Development Kit V1.0
# Going beyond Blink sketch to see the blue LED breathing.
#  https://arduinin.com/2015/08/20/nodemcu-breathing-led-with-arduino-ide/g

from machine import Pin, PWM
import time

LEDPin = 15 # NodeMCU D8/GPIO15 (Amica) D1/GPIO05, initially D0 / GPIO16
BRIGHT = 768 #512 #max LED intensity (1-1023)
#INHALE = 1250 #inhalation time in millisec --PePo not used
#PULSE = INHALE * 1000 / BRIGHT --PePo not used
REST = 1000 # rest between inhalations

# Setup
pwm = PWM(Pin(LEDPin), freq=1000) # PWM-pin

# Loop
while True:
    try:
        # ramp increasing intensity, inhalation
        #print("inhalation...")
        for i in range(1, BRIGHT, 1):
            #print("duty=", i)
            pwm.duty(i)
            time.sleep_ms(2)

        # ramp decreasing intensity, exhalation (half time)
        #print("exhalation...")
        for i in range(BRIGHT, 1, -2):
            #print("duty=", i)
            pwm.duty(i)
            time.sleep_ms(2)

        time.sleep_ms(REST) # take a rest
        
    except KeyboardInterrupt:
        pwm.value = 0 # led off
        print('done')
