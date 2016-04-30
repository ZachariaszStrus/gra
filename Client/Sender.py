import threading
import socket

import binascii
import pygame
import struct


class Sender:
    key_array = {pygame.K_RIGHT: 0, pygame.K_LEFT: 1, pygame.K_UP: 2, pygame.K_DOWN: 3, pygame.K_SPACE: 4}

    def __init__(self, address=("25.88.205.228", 9998)):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if not self.socket.connect(address):
            return

    def send(self, player, k, p):
        self.socket.sendall(self.get_message(player, k, p))

    def close(self):
        self.socket.close()

    def get_key_message(self, k, p):
        res = bytearray(3)
        res[0] = Sender.key_array[k]
        res[1] = p.x
        res[2] = p.y
        return res

    def get_message(self, player, k, p):
        values = (player, k, p.x, p.y)
        packer = struct.Struct('I I f f')
        packed_data = packer.pack(*values)
        print "sent : ", values
        return packed_data



