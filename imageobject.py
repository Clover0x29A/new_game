import pygame

class ImageObject:
    def __init__(self,x , y, path) -> None:
        self.x = x
        self.y = y
        self.move_amount = 5
        self.sprite = pygame.image.load(path)