#coding=utf-8

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSOCK = socket(AF_INET,SOCK_DGRAM)
tcpCliSOCK.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSOCK.send(data.encode('utf-8'))
    data = tcpCliSOCK.recv(BUFSIZE)
    if not data:
        break
    print(data.decode('utf-8'))
tcpCliSOCK.close()
