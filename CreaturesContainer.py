from Bullet import *


class CreaturesContainer:
    def __init__(self, C):
        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        image = c_nodes[0].getElementsByTagName("human")[0].childNodes[0].toxml()
        self.human = Human(Position(), image, C)
        self.bullets = []


