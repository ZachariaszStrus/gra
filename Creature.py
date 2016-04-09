from Thing import *


class Creature(Thing):
    def __init__(self, position, appearance, world):
        Thing.__init__(self, appearance)
        self.position = position
        self.world = world
        self.is_moving = False
        self.last_time = None
        self.cool_down = 200
        self.direction = Position(1, 0)

    def start_moving(self, direction, last_time):
        self.direction = direction
        self.last_time = last_time
        self.is_moving = True

    def end_moving(self):
        self.is_moving = False

    def move(self, current_time):
        if self.is_moving:
            self.position += self.direction * (float(current_time - self.last_time) / self.cool_down)
            self.last_time = current_time

    def can_move_to(self, new_position):
        pass


