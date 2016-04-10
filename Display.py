from Client.Listener import Listener
from Client.Sender import Sender
from Container import *
from Direction import *


class Display:
    def __init__(self, display, container):
        self.windowSizeX = display.get_width()
        self.windowSizeY = display.get_height()
        self.textures = []
        self.container = container

        self.gameDisplay = display
        self.clock = pygame.time.Clock()

        dom_tree = minidom.parse('textures.xml')
        c_nodes = dom_tree.childNodes
        self.textureSize = int(c_nodes[0].getAttribute("textureSize"))
        for texture in c_nodes[0].getElementsByTagName("texture"):
            self.textures.append(pygame.image.load(texture.childNodes[0].toxml()).convert())

        self.centerOfScreen = Position(
            self.windowSizeX / self.textureSize / 2,
            self.windowSizeY / self.textureSize / 2
        )

        #self.listener = Listener()
        #self.listener.start()
        #self.sender = Sender()

        self.player = container.player
        self.start_game()

    def start_game(self):
        exit_game = False
        while not exit_game:  # main loop
            self.repaint(self.container)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.KEYDOWN:
                    new_direction = Direction.get_direction_by_key(event.key)
                    if new_direction:
                        self.player.start_moving(new_direction, pygame.time.get_ticks())
                        #self.sender.send(event.key)
                    elif event.key == pygame.K_ESCAPE:
                        exit_game = True
                    elif event.key == pygame.K_SPACE:
                        self.container.bullets.append(Bullet(Position(self.player.position.x,
                                                                      self.player.position.y),
                                                             self.container,
                                                             Position(self.player.direction.x,
                                                                      self.player.direction.y),
                                                             pygame.time.get_ticks()))
                    elif event.key == pygame.K_F1:
                        self.container.move_other_players()

                elif event.type == pygame.KEYUP:
                    if Direction.get_direction_by_key(event.key):
                        self.player.end_moving(Direction.get_direction_by_key(event.key))

            for human in self.container.creatures:
                human.move(pygame.time.get_ticks())

            bullets_to_remove = list()
            for i in range(len(self.container.bullets)):
                if not self.container.bullets[i].move(pygame.time.get_ticks()):
                    bullets_to_remove.append(i)

            for i in bullets_to_remove:
                self.container.bullets.pop(i)

    def repaint(self, container):
        self.gameDisplay.fill((0, 0, 0))

        map_position = self.centerOfScreen - self.player.position
        for y in range(container.size):
            for x in range(container.size):
                field_position = Position(x, y) + map_position
                image = self.textures[container.map[y][x]]
                self.gameDisplay.blit(image, (self.textureSize * field_position.x,
                                              self.textureSize * field_position.y))
                image_id = container.map_of_obstacles[y][x]
                if image_id:
                    image = self.textures[image_id]
                    self.gameDisplay.blit(image, (self.textureSize * field_position.x,
                                                  self.textureSize * field_position.y))

        for human in container.creatures:
            position = human.position + map_position
            self.gameDisplay.blit(pygame.image.load(human.appearance),
                                  (position.x * self.textureSize,
                                   position.y * self.textureSize))

        for bullet in container.bullets:
            bullet_position = bullet.position - self.player.position + self.centerOfScreen
            self.gameDisplay.blit(pygame.image.load(bullet.appearance),
                                  (self.textureSize * bullet_position.x, self.textureSize * bullet_position.y))

        pygame.display.update()
