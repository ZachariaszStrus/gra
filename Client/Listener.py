from socket import *
import threading
import struct


class Listener (threading.Thread):
    def __init__(self, address=("localhost", 9999)):
        threading.Thread.__init__(self)

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
        buf = bytearray(4)
        results = list()

        while len(list) < 3:
            while self.running:
                if self.socket.recv_into(buf) > 0:
                    num = struct.unpack("!i", buf)[0]
                    print(num)
                    results.append(self.get_string(num))
                    print results[len(results) - 1]

        # 0 = index gracza
        # 1 = nazwa pliku
        # 2 = treść pliku

        #map_file = open(results[1], "w")
        #map_file.write(results[2])
        #map_file.close()

        self.socket.close()



