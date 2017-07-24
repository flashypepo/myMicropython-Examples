# leuk voorbeeld van een socket verbinding met een Starwars animatie
# 2017-0719 PePo nieuw
# source = http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/network_tcp.html

# pre-condition: device is connected to the web/internet
def starwars():
    import socket

    #Then get the IP address of the telnet-server
    addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)

    #The getaddrinfo function actually returns a list of addresses, and each address has more information than we need. We want to get just the first valid address, and then just the IP address and port of the server. To do this use:
    addr = addr_info[0][-1]

    #If you type addr_info and addr at the prompt you will see exactly what information they hold.
    #Using the IP address we can make a socket and connect to the server:
    s = socket.socket()
    s.connect(addr)

    #Now that we are connected we can download and display the data:
    # Ctrl-C to stop
    while True:
        data = s.recv(500)
        print(str(data, 'utf8'), end='')

# run example
try:
    starwars()
except:
    print('Done')
