from Direction import *
from Creature import *
from Human import Human


class Container:
    def __init__(self):
        self.size = None
        self.map = None
        self.map_of_obstacles = None

        self.creatures = list()
        self.bullets = list()

        self.read_from_xml()
        self.get_players()

        self.player = self.creatures[1]

    def get_players(self):
        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        image = c_nodes[0].getElementsByTagName("human")[0].childNodes[0].toxml()
        for i in range(4):
            self.creatures.append(Human(self.corner(i), image, self))

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

    def corner(self, n):
        if n == 0:
            return Position(0, 0)
        elif n == 1:
            return Position(0, self.size - 1)
        elif n == 2:
            return Position(self.size - 1, self.size - 1)
        elif n == 3:
            return Position(self.size - 1, 0)
        else:
            return None

    def move_creatures(self, current_time):
        for human in self.creatures:
                human.move(current_time)

        for bullet in self.bullets:
            bullet.move(current_time)


