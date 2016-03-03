from Block import *


class Human(Creature):
    def __init__(self, position, appearance, world):
        Creature.__init__(self, position, appearance, world)
        self.isRounding = False
        self.startTime = None
        self.endTimeOfRounding = None

    def startMoving(self, direction, lastTime):
        self.direction = direction
        self.startTime = lastTime
        self.lastTime = lastTime
        self.isMoving = True

    def endMoving(self, curentTime):
        self.isMoving = False
        self.isRounding = True
        self.endTimeOfRounding = curentTime + (self.coolDown - ((curentTime - self.startTime) % self.coolDown))

    def move(self, curentTime):  # to fix
        if self.isMoving:
            self.position += self.direction * (float(curentTime - self.lastTime) / self.coolDown)
            self.lastTime = curentTime
        elif self.isRounding:
            self.position += self.direction * (float(curentTime - self.lastTime) / self.coolDown)
            self.lastTime = curentTime
            if curentTime >= self.endTimeOfRounding:
                self.position = self.position.round()
                self.isRounding = False