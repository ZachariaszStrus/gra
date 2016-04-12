import pygame


class Button:
    def __init__(self, colour, fontcolour, pos, dim, text, disp):
        self.colour = colour
        self.fontcolour = fontcolour
        self.dim = (pos.x, pos.y, dim[0], dim[1])
        self.text = text
        self.display = disp

    def draw(self):
        text_font = pygame.font.Font('freesansbold.ttf', 20)
        pygame.draw.rect(self.display, self.colour, self.dim)
        text_surf = text_font.render(self.text, True, self.fontcolour)
        text_rect = text_surf.get_rect()
        text_rect.center = ((self.dim[0] + self.dim[2]/2), (self.dim[1] + self.dim[3]/2))
        self.display.blit(text_surf, text_rect)

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        return self.dim[0] < mouse[0] < self.dim[0] + self.dim[2] and self.dim[1] < mouse[1] < self.dim[1] + self.dim[3]