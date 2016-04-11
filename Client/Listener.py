import socket
import threading

import struct


class Listener (threading.Thread):
    def __init__(self, address=("localhost", 9999)):
        threading.Thread.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(address)
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        buf = bytearray(4096)
        while self.running:
            if self.socket.recv_into(buf) > 0:
                print "Received :", buf
        self.socket.close()

