from socket import *
import threading
import struct

import pygame

from Position import Position


class Listener (threading.Thread):
    key_array = [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN]

    def __init__(self, container, address=("25.37.158.69", 9999)):
        threading.Thread.__init__(self)

        self.container = container

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(address)
        self.running = True

    def stop(self):
        self.running = False

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

    def run(self):
        while self.running:
            buf = bytearray(4)
            size = self.socket.recv_into(buf)
            if size > 0:
                if size == 2:
                    player_id = int(buf[0])-48
                    event_key = int(buf[1]) - 48
                    print "Player id : ", player_id
                    print "Key : ", event_key
                    self.do_event(player_id, event_key)
                elif size == 3:
                    player_id = int(buf[0])-48
                    x = int(buf[1])
                    y = int(buf[2])
                    print "Player id : ", player_id
                    print "Position update : ", x, " ", y
                    self.container.update_player_position(player_id, Position(x, y))

        self.socket.close()

    def receive_map(self):
        buf = bytearray(4)
        results = list()

        while len(results) < 2:
            if self.socket.recv_into(buf) > 0:
                num = struct.unpack("!i", buf)[0]
                results.append(self.get_string(num))

        map_file = open("container.xml", "w")
        map_file.write(results[0])
        map_file.close()
        print int(results[1])
        self.container.player_id = int(results[1])

    def do_event(self, player_id, res):
        if res < len(Listener.key_array):
            self.container.move_other_player(player_id, Listener.key_array[res])
        else:
            self.container.stop_other_player(player_id, Listener.key_array[res-len(Listener.key_array)])



