from Container import *
from CreaturesContainer import *


class Display:
    def __init__(self, container, creaturesContainer):
        self.windowSizeX = 550
        self.windowSizeY = 550
        self.textures = []

        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        pygame.display.set_caption("GRA")
        self.clock = pygame.time.Clock()
        exitGame = False

        self.position = Position()
        self.time = 0
        self.last = pygame.time.get_ticks()
        self.cooldown = 100
        self.permit = True
        self.part = 0

        DOMTree = minidom.parse('textures.xml')
        cNodes = DOMTree.childNodes
        self.textureSize = int(cNodes[0].getAttribute("textureSize"))
        for texture in cNodes[0].getElementsByTagName("texture"):
            self.textures.append(pygame.image.load(texture.childNodes[0].toxml()).convert())

        self.centerOfScreen = Position(
            self.windowSizeX/self.textureSize/2,
            self.windowSizeY/self.textureSize/2
        )

        self.translation = Position(0, 0)

        while not exitGame:  # main loop
            self.repaint(container, creaturesContainer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        creaturesContainer.human.startMoving(Position(1, 0), pygame.time.get_ticks())
                    elif event.key == pygame.K_LEFT:
                        creaturesContainer.human.startMoving(Position(-1, 0), pygame.time.get_ticks())
                    elif event.key == pygame.K_DOWN:
                        creaturesContainer.human.startMoving(Position(0, 1), pygame.time.get_ticks())
                    elif event.key == pygame.K_UP:
                        creaturesContainer.human.startMoving(Position(0, -1), pygame.time.get_ticks())
                    elif event.key == pygame.K_ESCAPE:
                        exitGame = True
                    elif event.key == pygame.K_SPACE:
                        creaturesContainer.bullets.append(Bullet(Position(creaturesContainer.human.position.x,
                                                                          creaturesContainer.human.position.y),
                                                                 container,
                                                                Position(creaturesContainer.human.direction.x,
                                                                         creaturesContainer.human.direction.y),
                                                                 pygame.time.get_ticks()))
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        creaturesContainer.human.endMoving(pygame.time.get_ticks())
                    elif event.key == pygame.K_LEFT:
                        creaturesContainer.human.endMoving(pygame.time.get_ticks())
                    elif event.key == pygame.K_DOWN:
                        creaturesContainer.human.endMoving(pygame.time.get_ticks())
                    elif event.key == pygame.K_UP:
                        creaturesContainer.human.endMoving(pygame.time.get_ticks())

            creaturesContainer.human.move(pygame.time.get_ticks())
            for i in range(len(creaturesContainer.bullets)):
                creaturesContainer.bullets[i].move(pygame.time.get_ticks())

        pygame.quit()

    def repaint(self, container, creaturesContainer):
        self.gameDisplay.fill((0, 0, 0))

        for y in range(container.size):
            for x in range(container.size):
                mapPosition = Position(x, y) - creaturesContainer.human.position + self.centerOfScreen
                image = self.textures[container.map[y][x].appearance]
                self.gameDisplay.blit(image, (self.textureSize * mapPosition.x,
                                              self.textureSize * mapPosition.y)
                                      )

        self.gameDisplay.blit(pygame.image.load(creaturesContainer.human.appearance),
                              (self.centerOfScreen.x * self.textureSize, self.centerOfScreen.y * self.textureSize))

        for i in range(len(creaturesContainer.bullets)):
            bulletPosition = creaturesContainer.bullets[i].position - creaturesContainer.human.position + self.centerOfScreen
            self.gameDisplay.blit(pygame.image.load(creaturesContainer.bullets[i].appearance),
                              (self.textureSize * bulletPosition.x, self.textureSize * bulletPosition.y))

        pygame.display.update()


C = Container()
cc = CreaturesContainer(C)
disp = Display(C, cc)