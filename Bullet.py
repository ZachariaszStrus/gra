from xml.dom import minidom

from Human import *
from Creature import *


class Bullet(object, Creature):
    def __init__(self, human_position, world, direction, last_time, owner):
        Creature.__init__(self, human_position, self.get_image(), world)
        self.start_moving(direction, last_time)
        self.cool_down = 100
        self.owner = owner

    def get_image(self):
        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        return c_nodes[0].getElementsByTagName("bullet")[0].childNodes[0].toxml()

    def move(self, current_time):
        if self.check_if_can_move(current_time):
            super(Bullet, self).move(current_time)
        else:
            self.world.bullets.remove(self)

    def check_if_can_move(self, current_time):
        if self.is_moving:
            new_position = self.position + self.direction * (float(current_time - self.last_time) / self.cool_down)
            new_position = new_position.round()
            if self.collision_with_creatures(new_position) or \
                    self.is_outside_of_map(new_position) or \
                    self.collision_with_obstacles(new_position):
                self.is_moving = False
                return False
            return True
        return False

    def collision_with_creatures(self, new_position):
        for creature in self.world.creatures:
            if creature == self.owner:
                continue
            if new_position == creature.position:
                creature.restart()
                return True
        return False

    def collision_with_obstacles(self, new_position):
        if self.world.map_of_obstacles[int(new_position.y)][int(new_position.x)]:
            self.world.map_of_obstacles[int(new_position.y)][int(new_position.x)] = None
            return True

        return False
