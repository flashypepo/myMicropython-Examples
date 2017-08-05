# reads data from USB-serial to collect data from development board
# source: Python for Secret Agents, Volume II, 2015 (Safari online)
# usage:
# 1. run data-feed on development board
# 2. run this collector on computer
# 3. development board and computer are connected via USB
# pre-condition: pyserial installed on computer

import serial, sys
def sample(port, baudrate=9600, limit=128):
    with serial.Serial(port, baudrate, timeout=1) as sensor:
        while limit != 0:
            line = sensor.readline()
            if line:
                print(line.decode("ascii").rstrip())
                sys.stdout.flush()
                limit -= 1

while True:
    sample('/dev/tty.SLAB_USBtoUART', 115200)
