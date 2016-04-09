import threading
import socket


class Sender:

    def __init__(self, adres):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(adres)

        #("localhost", 9876)

    def send(self, index):
        self.server.send(index)

    def close(self):
        self.server.close()


class Listener (threading.Thread):

    def __init__(self, adres):
        threading.Thread.__init__(self)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(adres)

        #("localhost", 9876)

    def run(self):
        while 1:
            print(self.server.listen())
        self.server.close()