# project: a socket server running on the huzzah ESP8266
# and a client running on Mac/client
# 2017-0716 source: https://forums.adafruit.com/viewtopic.php?f=60&t=117874
import socket

def Main():
    # creating server socket for communication I/O
    host = "192.168.178.24" # host ip
    #MAC-test: host = "192.168.178.14" #host ip-address

    port = 5000 #must be above 1024 to avoid conflict with core services
    mySocket = socket.socket()
    mySocket.bind((host, port))
    print('Server running on host: {0}, port: {1} '.format(host, port))

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
        parse_command_echo(conn, data)

    conn.close()
    print('Connection closed')


# default ECHO-service
def parse_command_echo(conn, data):
    print('parse_command_echo() - sending: ' + str(data) )
    conn.send(data.encode())

if __name__ == '__main__':
    Main()
