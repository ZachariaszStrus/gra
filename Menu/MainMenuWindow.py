import pygame
import sys

from Client.Listener import Listener
from Client.Sender import Sender
from Container import Container
from Display import Display
from Menu.Button import Button
from Position import Position


class MainMenuWindow:
    def __init__(self):
        self.windowSizeX = 750
        self.windowSizeY = 550

        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.windowSizeX, self.windowSizeY))
        pygame.display.set_caption("GRA")

        self.add_controls()

        exit_game = False
        while not exit_game:
            self.draw_menu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_game_button.is_clicked():
                        self.start_game()
                    elif self.exit_game_button.is_clicked():
                        exit_game = True

        pygame.quit()
        sys.exit()

    def start_game(self):
        self.draw_waiting_screen()

        sender = Sender()
        container = Container(sender)

        listener = Listener(container)
        listener.receive_map()
        listener.start()

        Display(self.gameDisplay, container)
        listener.stop()
        sender.close()

    def add_controls(self):
        self.start_game_button = Button((150, 150, 150), (0, 0, 0),
                                        Position(self.windowSizeX/10, self.windowSizeY/10),
                                        (self.windowSizeX*8/10, self.windowSizeY*2/10),
                                        "Start game",
                                        self.gameDisplay)

        self.exit_game_button = Button((150, 150, 150), (0, 0, 0),
                                        Position(self.windowSizeX/10, self.windowSizeY*3/10 + 5),
                                        (self.windowSizeX*8/10, self.windowSizeY*2/10),
                                        "Exit game",
                                        self.gameDisplay)

    def draw_menu(self):
        self.gameDisplay.fill((0, 0, 0))
        self.start_game_button.draw()
        self.exit_game_button.draw()
        pygame.display.update()

    def draw_waiting_screen(self):
        self.gameDisplay.fill((0, 0, 0))
        Button((0, 0, 0), (255, 255, 255),
               Position(self.windowSizeX/10, self.windowSizeY/2),
               (self.windowSizeX*8/10, self.windowSizeY*2/10),
               "Waiting for map . . .",
               self.gameDisplay).draw()
        pygame.display.update()


MainMenuWindow()