from Block import *


class Human(Creature):
    def __init__(self, position, appearance, world):
        Creature.__init__(self, position, appearance, world)
        self.is_rounding = False
        self.previous_direction = None
        self.start_time = None
        self.end_time_of_rounding = None

    def set_direction(self, direction):
        self.direction = direction

    def start_moving(self, direction, last_time):
        if not self.is_moving:
            self.direction = direction
            if not self.is_rounding:
                self.previous_direction = self.direction
                self.start_time = last_time
                self.last_time = last_time
                self.is_moving = True

    def end_moving(self, direction_key, current_time):
        if direction_key == self.direction:
            self.is_moving = False
            self.is_rounding = True
            self.end_time_of_rounding = current_time + (self.cool_down - ((current_time - self.start_time) % self.cool_down))

    def move(self, current_time):  # to fix
        if self.is_moving:
            self.position += self.direction * (float(current_time - self.last_time) / self.cool_down)
            self.last_time = current_time
        elif self.is_rounding:
            self.position += self.previous_direction * (float(current_time - self.last_time) / self.cool_down)
            self.last_time = current_time
            if current_time >= self.end_time_of_rounding:
                self.position = self.position.round()
                self.is_rounding = False