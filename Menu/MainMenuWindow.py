import pygame

from Container import Container
from Display import Display
from Menu.Button import Button


class MainMenuWindow:
    def __init__(self):
        self.windowSizeX = 550
        self.windowSizeY = 550

        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        self.gameDisplay.fill((0, 0, 0))
        pygame.display.set_caption("GRA")

        self.add_controlls()

        exit_game = False
        while not exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_game()
                    exit_game = True

        pygame.quit()

    def start_game(self):
        c = Container()
        disp = Display(self.gameDisplay, c)

    def add_controlls(self):
        self.start_game_button = Button((255, 255, 255), (50, 50, 150, 150), "Start game", self.gameDisplay)

    def draw_menu(self):
        self.start_game_button.draw()
        pygame.display.update()

MainMenuWindow()