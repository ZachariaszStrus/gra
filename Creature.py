from Thing import *


class Creature(Thing):
    def __init__(self, position, appearance, world):
        Thing.__init__(self, appearance)
        self.position = position
        self.world = world

        self.last_time = None
        self.cool_down = 150

        self.direction = Position()
        self.is_moving = False

    def start_moving(self, direction, last_time):
        self.direction = direction
        self.last_time = last_time
        self.is_moving = True

    def end_moving(self):
        self.is_moving = False

    def move(self, current_time):
        self.position += self.direction * (float(current_time - self.last_time) / self.cool_down)
        self.last_time = current_time

    def check_if_can_move(self, new_position):
        if self.is_outside_of_map(new_position) or \
                self.world.map_of_obstacles[int(new_position.y)][int(new_position.x)]:
            return False
        else:
            return True

    def is_outside_of_map(self, new_position):
        return new_position.x < 0 or new_position.y < 0 or \
               new_position.x >= self.world.size or new_position.y >= self.world.size


