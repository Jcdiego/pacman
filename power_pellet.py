import pygame

class PowerPellet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 20, 20)
        self.color = (255, 255, 255)
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.rect.center, 10)
