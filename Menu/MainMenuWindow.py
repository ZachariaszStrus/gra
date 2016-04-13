import pygame

from Client.Listener import Listener
from Client.Sender import Sender
from Container import Container
from Display import Display
from Menu.Button import Button
from Position import Position


class MainMenuWindow:
    def __init__(self):
        self.windowSizeX = 550
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
                        exit_game = True

        pygame.quit()

    def start_game(self):
        self.draw_waiting_screen()

        sender = Sender()
        container = Container(sender)

        listener = Listener(container)
        listener.receive_map()
        listener.start()

        Display(self.gameDisplay, container)
        listener.stop()

    def add_controls(self):
        self.start_game_button = Button((255, 255, 255), (0, 0, 0),
                                        Position(50, 50), (450, 150),
                                        "Start game",
                                        self.gameDisplay)

    def draw_menu(self):
        self.gameDisplay.fill((0, 0, 0))
        self.start_game_button.draw()
        pygame.display.update()

    def draw_waiting_screen(self):
        self.gameDisplay.fill((0, 0, 0))
        Button((0, 0, 0), (255, 255, 255),
               Position(50, 200), (450, 150),
               "Waiting for map . . .",
               self.gameDisplay).draw()
        pygame.display.update()


MainMenuWindow()