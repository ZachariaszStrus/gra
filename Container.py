from Direction import *
from Bullet import *
from Creature import *


class Container:
    def __init__(self):
        self.size = None
        self.map = None
        self.map_of_obstacles = None

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

    def read_from_xml(self):
        dom_tree = minidom.parse('container.xml')
        nodes = dom_tree.childNodes

        self.size = int(nodes[0].getAttribute('size'))
        self.map = list()
        self.map_of_obstacles = list()

        for i in nodes[0].getElementsByTagName("background")[0].getElementsByTagName("line"):
            tmp = list()
            for j in range(self.size):
                tmp.append(int(i.childNodes[0].toxml()[j]))
            self.map.append(tmp)

        for i in nodes[0].getElementsByTagName("foreground")[0].getElementsByTagName("line"):
            tmp = list()
            for j in range(self.size):
                char = i.childNodes[0].toxml()[j].encode("utf-8")
                if char is not "n":
                    tmp.append(int(char))
                else:
                    tmp.append(None)

            self.map_of_obstacles.append(tmp)

C = Container()
C.read_from_xml()


