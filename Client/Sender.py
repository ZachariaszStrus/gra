import threading
import socket


class Sender:

    def __init__(self, address=("25.37.158.69", 9998)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self.socket.connect(address):
            return

    def send(self, key):
        self.socket.send(bytes(self.get_key_index(key)))
        print "Sent : ", self.get_key_index(key)

    def close(self):
        self.socket.close()

    def get_key_index(self, key):
        return key
