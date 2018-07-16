#coding=utf-8
from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST,PORT)

class myRequestHandler(SRH):
    def handle(self):
        print('...connect from',self.client_address)
        self.wfile.write('[%s] %s' %(bytes(ctime(),self.rfile.readline())))

tcpServ = TCP(ADDR,myRequestHandler)
print('waiting for connetion....')
tcpServ.serve_forever()