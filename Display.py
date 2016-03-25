from Sender import *
from Container import *
from CreaturesContainer import *
from Direction import *


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

        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        self.textureSize = int(c_nodes[0].getAttribute("textureSize"))
        for texture in c_nodes[0].getElementsByTagName("texture"):
            self.textures.append(pygame.image.load(texture.childNodes[0].toxml()).convert())

        self.centerOfScreen = Position(
            self.windowSizeX / self.textureSize / 2,
            self.windowSizeY / self.textureSize / 2
        )

        self.player = creatures_container.creatures[0]

        while not exit_game:  # main loop
            self.repaint(container, creatures_container)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    new_direction = Direction.get_direction_by_key(event.key)
                    if new_direction:
                        self.player.start_moving(new_direction, pygame.time.get_ticks())
                    elif event.key == pygame.K_ESCAPE:
                        exit_game = True
                    elif event.key == pygame.K_SPACE:
                        creatures_container.bullets.append(Bullet(Position(self.player.position.x,
                                                                           self.player.position.y),
                                                                  container,
                                                                  Position(self.player.direction.x,
                                                                           self.player.direction.y),
                                                                  pygame.time.get_ticks()))
                    elif event.key == pygame.K_F1:
                        creatures_container.move_other_players()

                    Sender.send(event.key)

                elif event.type == pygame.KEYUP:
                    if Direction.get_direction_by_key(event.key):
                        self.player.end_moving(Direction.get_direction_by_key(event.key),
                                               pygame.time.get_ticks())

            for human in creatures_container.creatures:
                human.move(pygame.time.get_ticks())

            for bullet in creatures_container.bullets:
                bullet.move(pygame.time.get_ticks())

        pygame.quit()

    def repaint(self, container, creatures_container):
        self.gameDisplay.fill((0, 0, 0))

        map_position = self.centerOfScreen - self.player.position
        for y in range(container.size):
            for x in range(container.size):
                field_position = Position(x, y) + map_position
                image = self.textures[container.map[y][x].appearance]
                self.gameDisplay.blit(image, (self.textureSize * field_position.x,
                                              self.textureSize * field_position.y))

        for human in creatures_container.creatures:
            position = human.position + map_position
            self.gameDisplay.blit(pygame.image.load(human.appearance),
                                  (position.x * self.textureSize,
                                   position.y * self.textureSize))

        for bullet in creatures_container.bullets:
            bullet_position = bullet.position - self.player.position + self.centerOfScreen
            self.gameDisplay.blit(pygame.image.load(bullet.appearance),
                                  (self.textureSize * bullet_position.x, self.textureSize * bullet_position.y))

        pygame.display.update()


C = Container()
cc = CreaturesContainer(C)
disp = Display(C, cc)
