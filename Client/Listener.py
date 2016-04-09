import socket
import threading

import sys


class Listener (threading.Thread):
    def __init__(self, address=("localhost", 9999)):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.socket.bind(address)
        except socket.error as msg:
            print msg
            sys.exit()

        self.socket.listen(10)

    def run(self):
        RECV_BUFFER = 4096
        while True:
            conn, addr = self.socket.accept()
            try:
                data = self.socket.recv(RECV_BUFFER)
                print data
            except:
                continue