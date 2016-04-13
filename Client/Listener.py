from socket import *
import threading
import struct

import pygame

from Position import Position


class Listener (threading.Thread):
    key_array = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE]

    def __init__(self, container, address=("25.37.158.69", 9999)):
        threading.Thread.__init__(self)

        self.container = container

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(address)
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            buf = bytearray(2)
            size = self.socket.recv_into(buf)
            if size > 0:
                player = int(buf[0])-48
                key = Listener.key_array[int(buf[1])]
                self.container.handle_server_input(player, key)

        self.socket.close()

    def receive_map(self):
        buf = bytearray(4)
        results = list()

        while len(results) < 3:
            if self.socket.recv_into(buf) > 0:
                num = struct.unpack("!i", buf)[0]
                results.append(self.get_string(num))

        map_file = open("container.xml", "w")
        map_file.write(results[0])
        map_file.close()

        self.container.player_id = int(results[1])
        self.container.number_of_players = int(results[2])

    def get_string(self, i):
        size = i
        tab = list()
        while size > 0:
            if size < 100:
                buf = bytearray(size)
                size = 0
            else:
                buf = bytearray(100)
                size -= 100

            while 1:
                if self.socket.recv_into(buf) > 0:
                    tab.append(buf)
                    break

        result = ''
        for s in tab:
            result += s.decode('utf-8')

        return result





