try:
    import usocket as socket
except:
    import socket

def main(use_stream=False):
    s = socket.socket()

    # 2017-0811 PePo - same tests
    #ORG: ai= socket.getaddrinfo("google.com", 80) #302 moved
    #ai= socket.getaddrinfo("w3schools.com", 80) #page moved to https
    ai = socket.getaddrinfo("academic.evergreen.edu", 80) #200 OK
    print("Address infos:", ai)
    addr = ai[0][-1] #get last item [-1] in tuple

    print("Connect address:", addr)
    s.connect(addr)

    if use_stream:
        # MicroPython socket objects support stream (aka file) interface
        # directly, but the line below is needed for CPython.
        #DEBUG: print('use_stream is True')
        s = s.makefile("rwb", 0)
        s.write(b"GET / HTTP/1.0\r\n\r\n")
        print(s.read())
    else:
        #DEBUG: print('use_stream is False')
        s.send(b"GET / HTTP/1.0\r\n\r\n")
        print(s.recv(4096))

    s.close()

main()
