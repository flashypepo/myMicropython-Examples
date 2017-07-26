'''
 MicroPython Motor driver for de NodeMCU L23D motorshield
 The motors are PWM-controlled, with seprated pins for directions.
 Author: Peter van der Post
 License: Public Domain
 
 Manual: https://smartarduino.gitbooks.io/user-mannual-for-esp-12e-motor-shield/content/
 Configuration
    D1 GPIO05   motor A   input  adjust speed by PWM
    D2 GPIO04   motor B   input  adjust speed by PWM
    D3 GPIO00   motor A   input  adjust direction
    D4 GPIO02   motor B   input  adjust direction
    D5 - D8   digital IO input/output
    GPIO: 14,12,13,15
Battery: LiPo 2200mAH, 7V
'''
import machine

class Motor:
    '''
     Make a Motor class for the NodeMCU motorshield
     based upon: https://github.com/squix78/esp8266-projects/blob/master/arduino-ide/wifi-car/wifi-car.ino
     '''
    # creates Motor object on GPIOs gpiom and gpiod, freq=100 by-default
    def __init__(self, gpiom, gpiod, freq = 100):
        # motor Pins - PWM controlled
        # freq=100 seems to work, duty=0: motor off
        self._freq = freq
        self._motor = machine.PWM(machine.Pin(gpiom), freq=self._freq, duty=0)
        # direction pins
        self._direction = machine.Pin(gpiod, machine.Pin.OUT)
        # re-set Motor-object
        self._reset()
    
        # re-sets the motor: speed=0, forward direction
    def _reset(self):
        self._speed = 0 #range: 0..1023
        self._forward = 1
        self._direction.on()

    def freq(self):
        return self._freq

    # brake() - motors off
    def brake(self):
        self._motor.duty(0)
        self._reset()

    # set speed of motor, index=0: motorA, index=1: motorB
    def speed(self, value=None):
        print('\tDEBUG: speed({0}) called'.format(value))
        if value is None:
            # get current duty value
            value = self._motor.duty()
        if value > 0:
            # forward
            self._forward = 1
            self._direction.on()
            #print('\tDEBUG: forward=', self._forward)
        elif value < 0:
            # backward
            self._forward = -1
            self._direction.off()
            #print('\tDEBUG: forward=', self._forward)
        else:
            # release
            print('\tTODO: release - what TODO ?')
            self._forward = 0
            #print('\tDEBUG: forward=', self._forward)
            pass
        # motor is on
        print('\tDEBUG: motor.duty=', abs(value))
        self._motor.duty(abs(value))
