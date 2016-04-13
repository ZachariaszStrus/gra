import math

from Direction import  Direction
from Bullet import Bullet
from Creature import Creature
from Position import Position


class Human(object, Creature):
    def __init__(self, position, appearance, world):
        Creature.__init__(self, position, appearance, world)
        self.destination_pos = Position()

    def start_moving(self, key, current_time):
        if not self.is_moving:
            direction = Direction.get_direction_by_key(key)
            self.direction = direction
            if self.check_if_can_move(current_time):
                self.destination_pos = self.position + self.direction
                self.last_time = current_time
                self.is_moving = True
                if self == self.world.player:
                    self.world.sender.send(key)

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