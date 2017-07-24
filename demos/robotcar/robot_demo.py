import machine, motor, bot, time

print('creating i2c and motors ...')
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
motors = motor.DCMotors(i2c) #creates motors object

LEFT=0 #M0 - left motor
RIGHT=3 #M4 - right motor
print('creating robot ...')
robot = bot.Robot(motors, LEFT, RIGHT) # creates robot

dt = 3 # duration in seconds
print('robot moves ...')
robot.left(2000, dt) #turn left
time.sleep(0.3)
robot.right(2000, dt) # turn right
time.sleep(0.3)
robot.forward(2000, dt) #forward
time.sleep(0.3)
robot.backward(2000, dt) #backwards
time.sleep(0.3)

print('robot demo ...')
speed = 3000 #motorspeed
for i in range(3):
    robot.left(speed, dt)
    time.sleep(0.3)
    robot.right(speed, dt)
    time.sleep(0.3)
    robot.forward(speed, dt)
    time.sleep(0.3)
    robot.backward(speed, dt)
    time.sleep(1.0)

print('done')
