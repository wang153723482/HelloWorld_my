# -*- coding: utf-8 -*-
#!/usr/bin/python
#coding=utf-8
import threading
import socket

class Client():
    def __init__(self, c):
        address = ('127.0.0.1', 10010)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        # ff = os.path.normcase(fn)

        try:
            send_context = SendContext(s, c)
            send_context.start()
        except IOError:
            print 'open err'


class SendContext(threading.Thread):
    def __init__(self, sock, context):
        threading.Thread.__init__(self)
        self.sock = sock
        self.context = context

    def run(self):
        self.sock.send(self.context+'\r')
        data = self.sock.recv(1024)
        print data
        self.sock.close()
        print 'close socket'

s = '{"InvoiceIndex":"123456789012345678901234567890123456789012345678901234567890123","CardList":[{"EAN":"6923127360014","CardNo":"6374975510000213449","InputType":"01","FaceValue":"10000","CNYCode":"CNY"}]}'
# c = Client(s)

# 上面用了多线程，不知道客户端为何要用多线程！！！！！！！


class DES3():
    result = ''
    def __init__(self, c):
        self.result = 'aa'+c
        address = ('127.0.0.1', 10010)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.send(c+'\r')
        self.result = s.recv(1024)
        s.close()

        # try:
        #     send_context = SendContext(s, c)
        #     send_context.start()
        # except IOError:
        #     print 'open err'


print DES3('Dd').result
