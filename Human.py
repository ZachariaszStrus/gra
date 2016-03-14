from Block import *


class Human(Creature):
    def __init__(self, position, appearance, world):
        Creature.__init__(self, position, appearance, world)
        self.isRounding = False
        self.startTime = None
        self.endTimeOfRounding = None

    def start_moving(self, direction, last_time):
        self.direction = direction
        self.startTime = last_time
        self.lastTime = last_time
        self.isMoving = True
    
    def end_moving(self, current_time):
        self.isMoving = False
        self.isRounding = True
        self.endTimeOfRounding = current_time + (self.coolDown - ((current_time - self.startTime) % self.coolDown))

    def move(self, current_time):  # to fix
        if self.isMoving:
            self.position += self.direction * (float(current_time - self.lastTime) / self.coolDown)
            self.lastTime = current_time
        elif self.isRounding:
            self.position += self.direction * (float(current_time - self.lastTime) / self.coolDown)
            self.lastTime = current_time
            if current_time >= self.endTimeOfRounding:
                self.position = self.position.round()
                self.isRounding = False