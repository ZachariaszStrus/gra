from Container import *
from CreaturesContainer import *


class Display:
    def __init__(self, container, creatures_container):
        self.windowSizeX = 550
        self.windowSizeY = 550
        self.textures = []

        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        pygame.display.set_caption("GRA")
        self.clock = pygame.time.Clock()
        exit_game = False

        self.position = Position()
        self.time = 0
        self.last = pygame.time.get_ticks()
        self.cooldown = 100
        self.permit = True
        self.part = 0

        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        self.textureSize = int(c_nodes[0].getAttribute("textureSize"))
        for texture in c_nodes[0].getElementsByTagName("texture"):
            self.textures.append(pygame.image.load(texture.childNodes[0].toxml()).convert())

        self.centerOfScreen = Position(
            self.windowSizeX / self.textureSize / 2,
            self.windowSizeY / self.textureSize / 2
        )

        self.translation = Position(0, 0)

        while not exit_game:  # main loop
            self.repaint(container, creatures_container)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        creatures_container.human.start_moving(Position(1, 0), pygame.time.get_ticks())
                    elif event.key == pygame.K_LEFT:
                        creatures_container.human.start_moving(Position(-1, 0), pygame.time.get_ticks())
                    elif event.key == pygame.K_DOWN:
                        creatures_container.human.start_moving(Position(0, 1), pygame.time.get_ticks())
                    elif event.key == pygame.K_UP:
                        creatures_container.human.start_moving(Position(0, -1), pygame.time.get_ticks())
                    elif event.key == pygame.K_ESCAPE:
                        exit_game = True
                    elif event.key == pygame.K_SPACE:
                        creatures_container.bullets.append(Bullet(Position(creatures_container.human.position.x,
                                                                           creatures_container.human.position.y),
                                                                  container,
                                                                  Position(creatures_container.human.direction.x,
                                                                           creatures_container.human.direction.y),
                                                                  pygame.time.get_ticks()))
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        creatures_container.human.end_moving(pygame.time.get_ticks())
                    elif event.key == pygame.K_LEFT:
                        creatures_container.human.end_moving(pygame.time.get_ticks())
                    elif event.key == pygame.K_DOWN:
                        creatures_container.human.end_moving(pygame.time.get_ticks())
                    elif event.key == pygame.K_UP:
                        creatures_container.human.end_moving(pygame.time.get_ticks())

            creatures_container.human.move(pygame.time.get_ticks())
            for i in range(len(creatures_container.bullets)):
                creatures_container.bullets[i].move(pygame.time.get_ticks())

        pygame.quit()

    def repaint(self, container, creatures_container):
        self.gameDisplay.fill((0, 0, 0))

        for y in range(container.size):
            for x in range(container.size):
                map_position = Position(x, y) - creatures_container.human.position + self.centerOfScreen
                image = self.textures[container.map[y][x].appearance]
                self.gameDisplay.blit(image, (self.textureSize * map_position.x,
                                              self.textureSize * map_position.y)
                                      )

        self.gameDisplay.blit(pygame.image.load(creatures_container.human.appearance),
                              (self.centerOfScreen.x * self.textureSize, self.centerOfScreen.y * self.textureSize))

        for i in range(len(creatures_container.bullets)):
            bullet_position = creatures_container.bullets[
                                 i].position - creatures_container.human.position + self.centerOfScreen
            self.gameDisplay.blit(pygame.image.load(creatures_container.bullets[i].appearance),
                                  (self.textureSize * bullet_position.x, self.textureSize * bullet_position.y))

        pygame.display.update()


C = Container()
cc = CreaturesContainer(C)
disp = Display(C, cc)
