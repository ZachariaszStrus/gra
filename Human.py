import math

from Bullet import Bullet
from Creature import Creature
from Position import Position


class Human(object, Creature):
    def __init__(self, position, appearance, world):
        Creature.__init__(self, position, appearance, world)

    def start_moving(self, direction, current_time):
        if not self.is_moving:
            self.direction = direction
            if self.check_if_can_move(self.position + self.direction):
                self.is_moving = True

    def move(self, current_time):
        if not self.position.is_almost_rounded():
            super(Human, self).move(current_time)
        else:
            self.position = self.position.round()
            self.end_moving()

    def shoot(self, current_time):
        self.world.bullets.append(Bullet(Position(self.position.x, self.position.y),
                                         self.world,
                                         Position(self.direction.x, self.direction.y),
                                         current_time))