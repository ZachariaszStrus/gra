from Human import *


class Bullet(Creature):
    def get_image(self):
        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        return c_nodes[0].getElementsByTagName("bullet")[0].childNodes[0].toxml()

    def __init__(self, human_position, world, direction, last_time):
        Creature.__init__(self, human_position, self.get_image(), world)
        self.start_moving(direction, last_time)
        self.cool_down = 100
