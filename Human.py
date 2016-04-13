import math

import pygame

from Direction import  Direction
from Bullet import Bullet
from Creature import Creature
from Position import Position


class Human(object, Creature):
    def __init__(self, position, appearance, world):
        Creature.__init__(self, position, appearance, world)
        self.destination_pos = Position()
        self.moves_to_do = list()

    def start_moving(self, key, current_time):
        direction = Direction.get_direction_by_key(key)
        if not self.is_moving:
            self.direction = direction
            if self.check_if_can_move(current_time):
                self.destination_pos = self.position + self.direction
                self.last_time = current_time
                self.is_moving = True
                if self == self.world.player:
                    self.world.sender.send(key)
            return True
        else:
            if self == self.world.player:
                self.moves_to_do.append(direction)
            return False

    def move(self, current_time):
        if self.is_moving:
            if not self.position.is_almost_at(self.destination_pos):
                super(Human, self).move(current_time)
            else:
                self.position = self.position.round()
                if len(self.moves_to_do) == 0:
                    self.end_moving()
                else:
                    self.direction = self.moves_to_do.pop(0)

    def shoot(self, current_time):
        self.world.sender.send(pygame.K_SPACE)
        self.world.bullets.append(Bullet(Position(self.position.x, self.position.y),
                                         self.world,
                                         Position(self.direction.x, self.direction.y),
                                         current_time))
