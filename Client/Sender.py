import threading
import socket


#("localhost", 9876)
class Sender:

    def __init__(self, address=("localhost", 9999)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(address)

    def send(self, key):
        self.socket.send(bytes(self.get_key_index(key)))

    def close(self):
        self.socket.close()

    @staticmethod
    def get_key_index(key):
        return key
