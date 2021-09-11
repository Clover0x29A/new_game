import pygame, sys
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Move Font')

FPS = 30
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

class MyFont:
    def __init__(self, font_name, ) -> None:
        self.font_obj = pygame.font.Font(font_name, 32)
        self.text_surface_obj = self.font_obj.render('Move Font!', True, GREEN, BLUE)
        self.text_rect_obj = self.text_surface_obj.get_rect()
        self.text_rect_obj.center = (250, 250)
        self.directionX = 'left'
        self.move_amount_x = -5
        self.directionY = 'down'
        self.move_amount_y = 5


    def move_fontX(self):
        if self.text_rect_obj.center[0] <= 70 and self.directionX == 'left':
            self.move_amount_x = -self.move_amount_x
            self.directionX = 'right'
        elif self.text_rect_obj.center[0]>= 430 and self.directionX == 'right':
            self.move_amount_x = -self.move_amount_x
            self.directionX = 'left'
        self.text_rect_obj.center = (self.text_rect_obj.center[0] + self.move_amount_x, self.text_rect_obj.center[1])

    def move_fontY(self):
        if self.text_rect_obj.center[1] <= 200 and self.directionY == 'up':
            self.move_amount_y = -self.move_amount_y
            self.directionY = 'down'
        elif self.text_rect_obj.center[1]>= 275 and self.directionY == 'down':
            self.move_amount_y = -self.move_amount_y
            self.directionY = 'up'
        self.text_rect_obj.center = (self.text_rect_obj.center[0], self.text_rect_obj.center[1] + self.move_amount_y)


move_text = MyFont('freesansbold.ttf')


while True:
    display.fill(BLACK)
    display.blit(move_text.text_surface_obj, move_text.text_rect_obj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    move_text.move_fontX()
    move_text.move_fontY()
    pygame.display.update()
    clock.tick(FPS)