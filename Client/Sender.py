import socket


class Sender:
    SERVER = ("localhost", 9876)

    @staticmethod
    def send(key):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(Sender.SERVER)
        sock.send(bytes(key))
        sock.close()
