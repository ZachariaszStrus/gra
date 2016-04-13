import math

from Bullet import Bullet
from Creature import Creature
from Position import Position


class Human(object, Creature):
    def __init__(self, position, appearance, world):
        Creature.__init__(self, position, appearance, world)
        self.destination_pos = Position()

    def start_moving(self, direction, current_time):
        if not self.is_moving:
            self.direction = direction
            if self.check_if_can_move(current_time):
                self.destination_pos = self.position + self.direction
                self.last_time = current_time
                self.is_moving = True

    def move(self, current_time):
        if self.is_moving:
            if not self.position.is_almost_at(self.destination_pos):
                super(Human, self).move(current_time)
            else:
                self.end_moving()
                self.position = self.position.round()

    def shoot(self, current_time):
        self.world.bullets.append(Bullet(Position(self.position.x, self.position.y),
                                         self.world,
                                         Position(self.direction.x, self.direction.y),
                                         current_time))