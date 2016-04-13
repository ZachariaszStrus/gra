import threading
import socket

import pygame


class Sender:
    key_array = {pygame.K_RIGHT: 0, pygame.K_LEFT: 1, pygame.K_UP: 2, pygame.K_DOWN: 3, pygame.K_SPACE: 4}

    def __init__(self, address=("25.37.158.69", 9998)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self.socket.connect(address):
            return

    def send(self, k):
        self.socket.send(bytes(self.get_key_message(k)))
        # print "Sent : ", self.get_key_message(k)

    def close(self):
        self.socket.close()

    def get_key_message(self, k):
        res = bytearray(1)
        res = Sender.key_array[k]

        return res

    def send_position(self, pos):
        res = bytearray(2)
        res[0] = int(pos.x)
        res[1] = int(pos.y)
        # print "Position sent : ", int(pos.x), " ", int(pos.y)
        self.socket.send(res)


