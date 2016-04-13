import pygame


class Text:
    def __init__(self, disp, text, pos, size=20, fontcolour=(255, 255, 255)):
        self.fontcolour = fontcolour
        self.size = size
        self.pos = pos
        self.text = text
        self.display = disp

    def draw(self):
        text_font = pygame.font.Font('freesansbold.ttf', 20)
        text_surf = text_font.render(self.text, True, self.fontcolour)
        text_rect = text_surf.get_rect()
        text_rect.center = (self.pos.x, self.pos.y)
        self.display.blit(text_surf, text_rect)