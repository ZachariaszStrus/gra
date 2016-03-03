from Human import *


class Bullet(Creature):
    def getImage(self):
        DOMTree = minidom.parse('textures.xml')
        cNodes = DOMTree.childNodes
        return cNodes[0].getElementsByTagName("bullet")[0].childNodes[0].toxml()

    def __init__(self, humanPosition, world, direction, lastTime):
        Creature.__init__(self, humanPosition, self.getImage(), world)
        self.startMoving(direction, lastTime)
        self.coolDown = 100