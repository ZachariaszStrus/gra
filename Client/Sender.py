import threading
import socket

import pygame


class Sender:
    key_array = {pygame.K_RIGHT: 0, pygame.K_LEFT: 1, pygame.K_UP: 2, pygame.K_DOWN: 3}

    def __init__(self, address=("25.37.158.69", 9998)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self.socket.connect(address):
            return

    def send(self, t, k):
        self.socket.send(bytes(self.get_key_message(t, k)))
        # print "Sent : ", self.get_key_message(t, k)

    def close(self):
        self.socket.close()

    def get_key_message(self, t, k):
        res = bytearray(1)
        if t == pygame.KEYDOWN:
            res = Sender.key_array[k]
        elif t == pygame.KEYUP:
            res = Sender.key_array[k]+len(Sender.key_array)
        else:
            res = False

        return res

    def send_position(self, pos):
        res = bytearray(2)
        res[0] = int(pos.x)
        res[1] = int(pos.y)
        print "Position sent : ", int(pos.x), " ", int(pos.y)
        self.socket.send(res)


