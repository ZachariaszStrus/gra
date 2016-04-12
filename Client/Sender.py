import threading
import socket

import pygame


class Sender:

    def __init__(self, address=("25.37.158.69", 9998)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self.socket.connect(address):
            return

    def send(self, event):
        if self.get_key_index(event):
            self.socket.send(bytes(self.get_key_index(event)))
            print "Sent : ", self.get_key_index(event)

    def close(self):
        self.socket.close()

    def get_key_index(self, event):
        res = bytearray(1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                res = 0
            elif event.key == pygame.K_LEFT:
                res = 1
            elif event.key == pygame.K_UP:
                res = 2
            elif event.key == pygame.K_DOWN:
                res = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                res = 4
            elif event.key == pygame.K_LEFT:
                res = 5
            elif event.key == pygame.K_UP:
                res = 6
            elif event.key == pygame.K_DOWN:
                res = 7
        else:
            res = False

        return res
