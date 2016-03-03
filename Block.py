from Creature import *

class Block(Thing):
    blocks = [[] for i in range(2)]

    @staticmethod
    def readTable():
        DOMTree = minidom.parse("textures.xml")
        cNodes = DOMTree.childNodes

        types = [[] for i in range(2)]
        i = 0

        for texture in cNodes[0].getElementsByTagName("texture"):
            type = texture.getAttribute("type")
            walkable = texture.getAttribute("walkable")

            if walkable == 'True':
                walkable = 1
            else:
                walkable = 0

            if types[walkable].count(type) == 0:
                index = len(Block.blocks[walkable])
                types[walkable].append(type)
                Block.blocks[walkable].append([Block(walkable, i, index)])
            else:
                index = types[walkable].index(type)
                Block.blocks[walkable][index].append(Block(walkable, i, index))
            i += 1

    def __init__(self, walkable, appearance, type):
        Thing.__init__(self, appearance)
        self.walkable = walkable
        self.type = type

Block.readTable()