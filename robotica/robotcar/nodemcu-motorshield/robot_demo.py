# RobotCar demo with the NodeMCU shield for ESP8266
# NodeMCU shield uses the chip L293D, which uses no I2C.
# Speed motors are PWM-controlled. Separate pins for direction of the motors. 
# D4 controls also blue led (reverse logic), so it lights on when motor B goes backwards,

# Very helpfull was following sites:
# http://www.rudiswiki.de/wiki/WiFiCar-NodeMCU
# https://smartarduino.gitbooks.io/user-mannual-for-esp-12e-motor-shield/content/how_to_get_it.html

# 2017-0724 PePo new
import machine, bot, time
import motor

print('creating the 2 motors ...')
# NodeMCU shield interface: http://www.rudiswiki.de/wiki/WiFiCar-NodeMCU
#ESP12E Dev Kit Control Port:
__D1 = 5  # GPIO05 motor PWMA   -- left motor
__D3 = 0  # GPIO00 motor dirA

__D2 = 4  # GPIO04 motor PWMB   -- right motor
__D4 = 2  # GPIO02 motor dirB
__FREQUENCY = 1600  # no idea what the value should be. Also working: 500

leftMotor = motor.Motor(__D1, __D3, __FREQUENCY)
#print('left motor:', leftMotor)
print('left motor - frequency = ', leftMotor.freq())

rightMotor = motor.Motor(__D2, __D4, __FREQUENCY)
#print('right motor:', rightMotor)
print('right motor - frequency = ', rightMotor.freq())

print('creating robot ...')
robot = bot.Robot(leftMotor, rightMotor)
#print('robot:', robot)

dt = 3 # duration in seconds
speed = 1023 # range: 0 .. 1023, effectively 600 - 1023
# According to http://www.rudiswiki.de/wiki/WiFiCar-NodeMCU
# motor start running if speed > 600 .. 1023
# motor stops if speed < 300
print('robot turns {0}... left'.format(speed))
robot.left(speed, dt) #turn left
time.sleep(0.3)

print('robot turns {0}... right '.format(speed))
robot.right(speed, dt) # turn right
time.sleep(0.3)

print('robot moves {0}... forwards'.format(speed))
robot.forward(speed, dt) #forward
time.sleep(0.3)

print('robot moves {0} ... backwards'.format(speed))
robot.backward(speed, dt) #backwards
time.sleep(0.3)

print('robot ... stops')
robot.stops() #stops
print('done')
