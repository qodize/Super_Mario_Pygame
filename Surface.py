import pygame


class Surface:
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        self.x, self.y, self.width, self.height = x, y, width, height
        self.left = self.x
        self.right = self.x + self.width
        self.up = self.y
        self.down = self.y + self.height
        self.color = pygame.Color(color)

    def draw(self, screen, SCR_X):
        self.rect = pygame.Rect(self.x - SCR_X, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect, 0)
