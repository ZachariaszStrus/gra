import math

from Bullet import Bullet
from Creature import Creature
from Position import Position


class Human(object, Creature):
    def __init__(self, position, appearance, world):
        Creature.__init__(self, position, appearance, world)

    def start_moving(self, direction, current_time):
        self.next_direction = direction
        if self.is_standing:
            self.is_standing = False
            super(Human, self).start_moving(direction, current_time)

    def end_moving(self, direction_key):
        if direction_key == self.direction:
            self.is_moving = False
        else:
            self.next_direction = self.direction

    def move(self, current_time):
        if self.is_moving:
            super(Human, self).move(current_time)
        else:
            if not self.position.is_almost_rounded():
                super(Human, self).move(current_time)
            elif not self.is_standing:
                self.position = self.position.round()
                self.is_moving = False
                self.is_standing = True
                self.world.sender.send_position(self.position)
                if self.direction != self.next_direction:
                    self.start_moving(self.next_direction, current_time)

    def shoot(self, current_time):
        self.world.bullets.append(Bullet(Position(self.position.x, self.position.y),
                                         self.world,
                                         Position(self.direction.x, self.direction.y),
                                         current_time))
