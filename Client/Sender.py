import threading
import socket

import pygame


class Sender:

    def __init__(self, address=("25.37.158.69", 9998)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self.socket.connect(address):
            return

    def send(self, t, k):
        if self.get_key_index(t, k):
            self.socket.send(bytes(self.get_key_index(t, k)))
            print "Sent : ", self.get_key_index(t, k)

    def close(self):
        self.socket.close()

    def get_key_index(self, t, k):
        res = bytearray(1)
        if t == pygame.KEYDOWN:
            if k == pygame.K_RIGHT:
                res = 0
            elif k == pygame.K_LEFT:
                res = 1
            elif k == pygame.K_UP:
                res = 2
            elif k == pygame.K_DOWN:
                res = 3
        elif t == pygame.KEYUP:
            if k == pygame.K_RIGHT:
                res = 4
            elif k == pygame.K_LEFT:
                res = 5
            elif k == pygame.K_UP:
                res = 6
            elif k == pygame.K_DOWN:
                res = 7
        else:
            res = False

        return res
