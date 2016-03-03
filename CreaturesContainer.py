from Bullet import *


class CreaturesContainer:
    def __init__(self, C):
        DOMTree = minidom.parse('textures.xml')
        cNodes = DOMTree.childNodes
        image = cNodes[0].getElementsByTagName("human")[0].childNodes[0].toxml()
        self.human = Human(Position(), image, C)
        self.bullets = []


