import sys, time
from socket import socket,AF_INET, SOCK_STREAM
import threading

BUFSIZE = 1024000
port = 9999
def server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', int(port)))
    s.listen(1)
    print ('Server ready...')
    while 1:
        conn, (host, remoteport) = s.accept()
        while 1:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            del data
        #conn.send('OK\n')
        conn.close()
        print ('Done with', host, 'port', remoteport)
server()