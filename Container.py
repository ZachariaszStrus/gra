from Direction import *
from Bullet import *
from Creature import *


class Container:
    def __init__(self):


        self.creatures = list()
        self.bullets = list()

    def get_players(self):
        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        image = c_nodes[0].getElementsByTagName("human")[0].childNodes[0].toxml()
        for i in range(4):
            self.creatures.append(Human(container.corner(i), image, container))

    def move_other_players(self):
        for i in range(1, 4):
            self.creatures[i].start_moving(Direction.get_rand(), pygame.time.get_ticks())


