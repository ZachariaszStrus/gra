from socket import *
import threading
import struct

import pygame


class Listener (threading.Thread):
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
            if self.socket.recv_into(buf) > 0:
                player_id = int(buf[0])-48
                event_key = int(buf[1])
                print "Player id : ", player_id
                print "Key : ", event_key
                self.do_event(player_id, event_key)

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
        if res == 0:
            self.container.move_other_player(player_id, pygame.K_RIGHT)
        elif res == 1:
            self.container.move_other_player(player_id, pygame.K_LEFT)
        elif res == 2:
            self.container.move_other_player(player_id, pygame.K_UP)
        elif res == 3:
            self.container.move_other_player(player_id, pygame.K_DOWN)
        elif res == 4:
            self.container.stop_other_player(player_id, pygame.K_RIGHT)
        elif res == 5:
            self.container.stop_other_player(player_id, pygame.K_LEFT)
        elif res == 6:
            self.container.stop_other_player(player_id, pygame.K_UP)
        elif res == 7:
            self.container.stop_other_player(player_id, pygame.K_DOWN)



