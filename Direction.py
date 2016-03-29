import random

import pygame
from Position import Position


class Direction():
    right = Position(1, 0)
    left = Position(-1, 0)
    up = Position(0, -1)
    down = Position(0, 1)

    @staticmethod
    def get_direction_by_key(key):
        if key == pygame.K_RIGHT:
            return Direction.right
        elif key == pygame.K_LEFT:
            return Direction.left
        elif key == pygame.K_UP:
            return Direction.up
        elif key == pygame.K_DOWN:
            return Direction.down
        else:
            return False

    @staticmethod
    def get_rand():
        r = random.randint(0, 3)
        if r == 0:
            return Direction.right
        elif r == 1:
            return Direction.left
        elif r == 2:
            return Direction.up
        else:
            return Direction.down

