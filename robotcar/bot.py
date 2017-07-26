# MicroPython LOGO style robot.
# Author: Tony DiCola
# License: Public Domain
import time


class Robot:
    # Make a class to give a simple LOGO turtle style interface to the bot.

    def __init__(self, motors, left_motor, right_motor):
        # Save the motor controller and left/right motor numbers.
        self._motors = motors
        self._left_motor = left_motor
        self._right_motor = right_motor

    def _drive(self, left_speed, right_speed, time_sec):
        # Drive the motors at the specified speed and amount of time.
        self._motors.speed(self._left_motor, left_speed)
        self._motors.speed(self._right_motor, right_speed)
        time.sleep(time_sec)
        self._motors.brake(self._left_motor)
        self._motors.brake(self._right_motor)

    def forward(self, speed, time_sec):
        # Move both motors forward for the specified time, then stop.
        self._drive(speed, speed, time_sec)

    def backward(self, speed, time_sec):
        # Move both motors backward for the specified time, then stop.
        self._drive(-speed, -speed, time_sec)

    def right(self, speed, time_sec):
        # Move right motor forward and left motor backward to spin right.
        self._drive(-speed, speed, time_sec)

    def left(self, speed, time_sec):
        # Move left motor forward and right motor backward to spin left.
        self._drive(speed, -speed, time_sec)
