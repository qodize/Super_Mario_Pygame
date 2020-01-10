import pygame
from maps.map_1 import surfaces
from pygame.examples.eventlist import main
# main()


def is_intersect(self, surface):
    left1, up1, right1, down1, left2, up2, right2, down2 = self.left, self.up, self.right, self.down, surface.left, surface.up, surface.right, surface.down
    return right1 > left2 and left1 < right2 and up1 < down2 and down1 > up2

class Unit:
    def __init__(self, x, y, width = 20, height=30):
        self.pos = self.x, self.y = x, y
        self.width = width
        self.height = height
        self.left = self.x
        self.right = self.x + self.width
        self.up = self.y
        self.down = self.y + self.height

        self.maygo_left = True
        self.maygo_right = True
        self.maygo_up = True
        self.maygo_down = True
        self.check_possible_moves_x()
        self.check_possible_moves_y()

        self.speed_x = 0
        self.speed_y = 0
        self.body_color = pygame.Color("red")
        self.on_ground = False
        self.a_y = 0

    def set_pos(self, x, y):
        self.pos = self.x, self.y = x, y
        self.set_borders()

    def set_borders(self):
        self.pos = self.x, self.y
        self.left = self.x
        self.right = self.x + self.width
        self.up = self.y
        self.down = self.y + self.height

    def move(self):
        # self.check_possible_moves_x()
        # if self.speed_x < 0 and self.maygo_left or self.speed_x > 0 and self.maygo_right:
        #     self.x += self.speed_x
        self.x += self.speed_x
        self.set_borders()
        self.check_possible_moves_x()

        # self.check_possible_moves_y()
        # if self.speed_y < 0 and self.maygo_up or self.speed_y > 0 and self.maygo_down:
        self.y += self.speed_y
        self.set_borders()
        self.check_possible_moves_y()


    def render(self, screen):
        global SCR_X, SCR_Y
        rect = pygame.Rect(
            int(self.x - SCR_X),
            int(self.y - SCR_Y),
            self.width,
            self.height,
        )
        pygame.draw.rect(screen, self.body_color, rect)

    def change_speed(self):
        # self.check_possible_moves_x()
        # self.check_possible_moves_y()
        if self.maygo_down:
            self.a_y = (40 * 40 / (FPS ** 2)) * SCALE_D
            self.speed_y += self.a_y
        else:
            self.a_y = 0
            if self.speed_y > 0:
                self.speed_y = 1

    def check_possible_moves_x(self):
        self.maygo_left, self.maygo_right = True, True
        for surface in surfaces:
            if is_intersect(self, surface):
                if self.speed_x > 0:
                    self.maygo_right = False
                    self.x = surface.left - self.width
                    # self.x -= self.speed_x
                elif self.speed_x < 0:
                    self.maygo_left = False
                    self.x = surface.right
                    # self.x -= self.speed_x
                self.set_borders()


    def check_possible_moves_y(self):
        self.maygo_up, self.maygo_down = True, True
        for surface in surfaces:
            if is_intersect(self, surface):
                if self.speed_y > 0:
                    self.maygo_down = False
                    self.y = surface.up - self.height
                    # self.y -= self.speed_y
                elif self.speed_y < 0:
                    self.maygo_up = False
                    self.speed_y = 1
                    self.y = surface.down
                    # self.y -= self.speed_y
                self.set_borders()


pygame.init()

size = WIDTH, HEIGHT = 800, 640
FPS = 60
SCALE_D = 3.5
BASEMARIOSPEED = 150 * SCALE_D
MARIOJUMPSPEED = 450 * SCALE_D

screen = pygame.display.set_mode(size)
SCR_X = 0
SCR_Y = 150

clock = pygame.time.Clock()
sky_color = pygame.Color("blue")

Mario = Unit(42 * SCALE_D, 193 * SCALE_D, 10 * SCALE_D, 15 * SCALE_D)

running = True
while running:
    # Mario.check_possible_moves_y()
    # Mario.check_possible_moves_x()
    Mario.move()
    SCR_X = (Mario.x - 150)
    Mario.change_speed()

    # print(Mario.x, Mario.y, end=" ")
    # print(f"{Mario.maygo_down=}")
    # print(SCR_X)

    screen.fill(sky_color)
    for surface in surfaces:
        surface.draw(screen, SCR_X, SCR_Y)
    Mario.render(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # moving left-right
        if event.type == pygame.KEYDOWN:
            if event.key == 276:
                Mario.speed_x = -BASEMARIOSPEED / FPS
            elif event.key == 275:
                Mario.speed_x = BASEMARIOSPEED / FPS
            elif event.key == 273:
                if Mario.maygo_up and not Mario.maygo_down:
                    Mario.speed_y = -MARIOJUMPSPEED / FPS
                    # Mario.maygo_down = True
        elif event.type == pygame.KEYUP:
            if event.key == 276:
                if Mario.speed_x < 0:
                    Mario.speed_x = 0
            elif event.key == 275:
                if Mario.speed_x > 0:
                    Mario.speed_x = 0

    clock.tick(FPS)
pygame.quit()

