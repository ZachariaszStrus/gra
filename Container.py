from Block import *


class Container:
    def __init__(self):
        self.size = self.read_size()
        self.segmentSize = self.read_segment_size()
        self.map = [[None]*self.size for i in range(self.size)]
        self.segments = []
        self.read_segments()
        self.fill()

    def read_segment_size(self):
        DOMTree = minidom.parse('init.xml')
        cNodes = DOMTree.childNodes
        return int(cNodes[0].getElementsByTagName("segmentSize")[0].childNodes[0].toxml())

    def read_size(self):
        DOMTree = minidom.parse('init.xml')
        cNodes = DOMTree.childNodes
        return int(cNodes[0].getElementsByTagName("size")[0].childNodes[0].toxml())

    def read_segments(self):
        DOMTree = minidom.parse('segments.xml')
        cNodes = DOMTree.childNodes
        for i in cNodes[0].getElementsByTagName("segment"):
            self.segments.append(i.childNodes[0].toxml())

    def random_block(self, options, block, walkable):
        if block.walkable == walkable:
            options.append(random.choice(Block.blocks[walkable][block.type]))

    def fill(self):
        for i in range(self.size / self.segmentSize):
            for j in range(self.size / self.segmentSize):

                #  losowanie segmentu
                segment = random.choice(self.segments)

                for k in range(self.segmentSize):
                    for l in range(self.segmentSize):

                        #  odczytywanie poszczegolnego pola segmentu
                        if segment[k*self.segmentSize+l] == 'o':
                            walkable = 1
                        elif segment[k*self.segmentSize+l] == 'x':
                            walkable = 0

                        options = []

                        if i*self.segmentSize+(k-1) < 0 and j*self.segmentSize+(l-1) < 0:
                            options.append(random.choice(random.choice(Block.blocks[walkable])))
                        elif i*self.segmentSize+(k-1) < 0:
                            self.random_block(options, self.map[i * self.segmentSize + k][j * self.segmentSize + (l - 1)], walkable)
                        elif j*self.segmentSize+(l-1) < 0:
                            self.random_block(options, self.map[i * self.segmentSize + (k - 1)][j * self.segmentSize + l], walkable)
                        else:
                            self.random_block(options, self.map[i * self.segmentSize + k][j * self.segmentSize + (l - 1)], walkable)
                            self.random_block(options, self.map[i * self.segmentSize + (k - 1)][j * self.segmentSize + l], walkable)
                            self.random_block(options, self.map[i * self.segmentSize + (k - 1)][j * self.segmentSize + (l - 1)], walkable)

                        if len(options) == 0 or random.randint(1, 10) < 3:
                            block = random.choice(random.choice(Block.blocks[walkable]))
                        else:
                            block = random.choice(options)

                        self.map[i*self.segmentSize+k][j*self.segmentSize+l] = block

C = Container()



