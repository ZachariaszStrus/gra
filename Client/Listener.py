import socket
import threading


class Listener (threading.Thread):
    def __init__(self, address=("localhost", 9999)):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(address)

    def run(self):
        while 1:
            pass
            #print(self.socket.listen(10))
        self.socket.close()
