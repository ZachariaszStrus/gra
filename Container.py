from Direction import *
from Creature import *
from Human import Human


class Container:
    def __init__(self, sender):
        self.size = None
        self.map = None
        self.map_of_obstacles = None
        self.player_id = 0
        self.player = None

        self.number_of_players = 4

        self.sender = sender

        self.creatures = list()
        self.bullets = list()

    def load_world(self):
        self.read_from_xml()
        self.get_players()
        self.player = self.creatures[self.player_id]

    def get_players(self):
        for i in range(self.number_of_players):
            self.creatures.append(Human(self.corner(i), self))

    def handle_server_input(self, player, key):
        if Direction.get_direction_by_key(key):
            self.creatures[player].start_moving(key, pygame.time.get_ticks())
        elif key == pygame.K_SPACE:
            print "Player ", player
            self.creatures[player].shoot()

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
        for bullet in self.bullets:
            bullet.move(current_time)

        for human in self.creatures:
            human.move(current_time)


