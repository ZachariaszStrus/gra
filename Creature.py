from Thing import *


class Creature(Thing):
    def __init__(self, position, appearance, world):
        Thing.__init__(self, appearance)
        self.position = position
        self.world = world
        self.isMoving = False
        self.lastTime = None
        self.coolDown = 200
        self.direction = Position(1, 0)

    def startMoving(self, direction, lastTime):
        self.direction = direction
        self.lastTime = lastTime
        self.isMoving = True

    def endMoving(self):
        self.isMoving = False

    def move(self, curentTime):
        if self.isMoving:
            self.position += self.direction * (float(curentTime - self.lastTime) / self.coolDown)
            self.lastTime = curentTime



