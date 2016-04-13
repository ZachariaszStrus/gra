import math
from xml.dom import minidom

import pygame

from Direction import  Direction
from Bullet import Bullet
from Creature import Creature
from Position import Position


class Human(object, Creature):
    def __init__(self, position, world):
        Creature.__init__(self, position, self.get_image(), world)
        self.destination_pos = Position()
        self.moves_to_do = list()

    def get_image(self):
        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        return c_nodes[0].getElementsByTagName("human")[0].childNodes[0].toxml()

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
        else:
            if self != self.world.player:
                self.moves_to_do.append(key)

    def move(self, current_time):
        if self.is_moving:
            if not self.position.is_almost_at(self.destination_pos):
                super(Human, self).move(current_time)
            else:
                self.position = self.position.round()
                self.end_moving()
                if len(self.moves_to_do) != 0:
                    self.start_moving(self.moves_to_do.pop(0), current_time)

    def shoot(self):
        if self == self.world.player:
            self.world.sender.send(pygame.K_SPACE)
        self.world.bullets.append(Bullet(Position(self.position.x, self.position.y),
                                         self.world,
                                         Position(self.direction.x, self.direction.y),
                                         pygame.time.get_ticks(),
                                         self))

    def restart(self):
        self.position = self.world.corner(self.world.coreatures.index(self))
