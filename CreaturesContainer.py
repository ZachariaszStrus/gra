from Direction import *
from Bullet import *


class CreaturesContainer:
    def __init__(self, container):
        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        image = c_nodes[0].getElementsByTagName("human")[0].childNodes[0].toxml()
        self.creatures = []
        for i in range(4):
            self.creatures.append(Human(container.corner(i), image, container))
        self.bullets = []

    def move_other_players(self):
        for i in range(1, 4):
            self.creatures[i].start_moving(Direction.get_rand(), pygame.time.get_ticks())


