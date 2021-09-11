import pygame, sys
from pygame.locals import *
from imageobject import ImageObject

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
FPS = 60
clock = pygame.time.Clock()
aqua = (0, 255, 255)
grey = (100, 100, 100)
cat_image = 'cat.png'
squirrel_image = 'squirrel.png'
cat = ImageObject(450, 400, cat_image)
squirrel = ImageObject(25, 459, squirrel_image)

images = [cat, squirrel]
pygame.display.set_caption('Hello World!')
def draw_rect():
    my_rect = pygame.Rect(10, 10, 480, 480)
    return my_rect

def move_cat(cat):
    if cat.x <= 0:
        cat.move_amount = -cat.move_amount
    elif cat.x >= 500:
        cat.move_amount = -cat.move_amount
    cat.x += cat.move_amount

def blit_images(images):
    for image in images:
        DISPLAYSURF.blit(image.sprite, (image.x, image.y))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ps_rect = draw_rect()
    pygame.draw.rect(DISPLAYSURF, aqua, ps_rect)
    move_cat(cat)
    blit_images(images)
    pygame.display.update()
    clock.tick(FPS)