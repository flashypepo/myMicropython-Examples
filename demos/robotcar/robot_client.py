# project: a client running on a device (Mac/Win/Linux) 
# connected to a server, running on the Huzzah ESP8266
# 2017-0716 source: https://forums.adafruit.com/viewtopic.php?f=60&t=117874
import socket

def run():
    host = '192.168.178.24' # host ip
    #MAC-test: host = '192.168.178.14' #host ip-address
    port = 5000

    mySocket = socket.socket()
    mySocket.connect((host, port))
    print('Client connected to host: {0}, port: {1} '.format(host, port))

    # get user command
    # 2017-0716: 'f' = go forward, 'b' = go backwards, 
    #            'l'=turn left, 'r'= turn right
    #            's' = stop
    message = input(" -> ") 

    # as long as user command is not 'q', send command to server
    while message != 'q':
        mySocket.send(message.encode()) # send command to server
        data = mySocket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")
    
    mySocket.close()

if __name__ == '__main__':
    run()
