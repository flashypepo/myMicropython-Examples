# project: a socket server running on the huzzah ESP8266
# and a client running on Mac/client
# 2017-0716 source: https://forums.adafruit.com/viewtopic.php?f=60&t=117874
import socket
import machine, motor, bot, time

def Main():
    speed = 2000 # default speed
    dt = 3 #default 3 seconds

    # creating robot
    print('creating i2c ...')
    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
    print('creating motors ...')
    motors = motor.DCMotors(i2c) #creates motors object
    _LEFT_MOTOR = 0 #M0 - left motor
    _RIGHT_MOTOR = 3 #M4 - right motor
    print('creating robot ...')
    robot = bot.Robot(motors, _LEFT_MOTOR, _RIGHT_MOTOR) # creates robot

    # creating server socket for communication I/O
    host = "192.168.178.24" # host ip
    #MAC-test: host = "192.168.178.14" #host ip-address

    port = 5000 #must be above 1024 to avoid conflict with core services
    mySocket = socket.socket()
    mySocket.bind((host, port))
    print('Robot running on host: {0}, port: {1} '.format(host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print('Connection from: ' + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('from connected user: ' + str(data))
        
        # parse user command
        data = str(data).upper()
        if data == 'H':
            help(conn)
        elif data == '+':
            speed += 500
            parse_command_echo(conn, 'speed={0}'.format(speed))
        elif data == '-':
            speed -= 500
            parse_command_echo(conn, 'speed={0}'.format(speed))
        elif data == '/':
            dt += 1
            parse_command_echo(conn, 'duration={0}'.format(dt))
        elif data == ';':
            dt -= 1
            parse_command_echo(conn, 'duration={0}'.format(dt))
        elif data == 'S':
            parse_command_echo(conn, 'robot: speed={0}, duration={1}\n'.format(speed, dt))
        else:
            parse_command_bot(robot, data, speed, dt)
            data = 'OK'
            parse_command_echo(conn, data) 

    conn.close()
    print('Connection closed')

# Car command services
def parse_command_bot(robot, data, speed, dt):
    '''parse client-commands to robot-actions'''
    if data == 'F':
        robot.forward(speed, dt) #turn left
    if data == 'B':
        robot.backward(speed, dt) #backwards
    if data == 'L':
        robot.left(speed, dt) # turn right
    if data == 'R':
        robot.right(speed, dt) # turn right

def help(conn):
    data = 'Robot commands:\n'
    data += 'F: move forwards\n'
    data += 'B: move backwards\n'
    data += 'L: turn left\n'
    data += 'R: turn right\n'
    data += '+: increase speed with 500\n'
    data += '-: decrease speed with 500\n'
    data += '/: increase time duration with 1s\n'
    data += ';: decrease time duration with 1s\n'
    data += 'S: robot parameters\n'
    data += 'H: available commands\n'
    data += 'q: stop communication\n'
    # send to client
    parse_command_echo(conn, data) 

# default ECHO-service
def parse_command_echo(conn, data):
    print('parse_command_echo() - sending: ' + str(data) )
    conn.send(data.encode())

if __name__ == '__main__':
    Main()
