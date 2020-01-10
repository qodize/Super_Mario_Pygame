import pygame

SCALE_D = 3.5

class Surface:
    def __init__(self, x, y, width, height, color=(0, 0, 0)):
        self.x, self.y, self.width, self.height = x * SCALE_D, y * SCALE_D, width * SCALE_D, height * SCALE_D
        self.left = self.x
        self.right = self.x + self.width
        self.up = self.y
        self.down = self.y + self.height
        self.color = pygame.Color(color)

    def draw(self, screen, SCR_X, SCR_Y):
        self.rect = pygame.Rect((self.x - SCR_X), (self.y - SCR_Y), self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect, 0)

# class Tube(Surface):
#
# class Block
#
# class GoldenBlock
#