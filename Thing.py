from xml.dom import minidom
import pygame
import random
from Position import *

class Thing:
    def __init__(self, appearance):
        self.appearance = appearance  # index