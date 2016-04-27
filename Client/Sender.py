import threading
import socket

import pygame


class Sender:
    key_array = {pygame.K_RIGHT: 0, pygame.K_LEFT: 1, pygame.K_UP: 2, pygame.K_DOWN: 3, pygame.K_SPACE: 4}

    def __init__(self, address=("192.168.137.92", 9998)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self.socket.connect(address):
            return

    def send(self, k, p):
        self.socket.send(bytes(self.get_key_message(k, p)))

    def close(self):
        self.socket.close()

    def get_key_message(self, k, p):
        res = bytearray(3)
        res[0] = Sender.key_array[k]
        res[1] = bytes(p.x)
        res[2] = bytes(p.y)
        return res



