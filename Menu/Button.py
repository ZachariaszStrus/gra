import pygame


class Button:
    def __init__(self, color, dim, text, disp):
        self.color = color
        self.dim = dim
        self.text = text
        self.display = disp

    def draw(self):
        text_font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.draw.rect(self.display, self.color, self.dim)
        text_surf = text_font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect()
        text_rect.center = ((self.dim[0] + self.dim[2]/2), (self.dim[1] + self.dim[3]/2))
        self.display.blit(text_surf, text_rect)

    def is_mouse_on(self, mouse):
        return self.dim[0] < mouse[0] < self.dim[0] + self.dim[2] and self.dim[1] < mouse[1] < self.dim[1] + self.dim[3]