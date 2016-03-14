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

    def start_moving(self, direction, last_time):
        self.direction = direction
        self.lastTime = last_time
        self.isMoving = True

    def end_moving(self):
        self.isMoving = False

    def move(self, current_time):
        if self.isMoving:
            self.position += self.direction * (float(current_time - self.lastTime) / self.coolDown)
            self.lastTime = current_time



