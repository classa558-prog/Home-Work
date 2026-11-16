import pygame
pygame.init()
pygame.display.set_mode(400, 500)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
rect1 = Sprite((0, 235, 48), 20, 20)
rect2 = Sprite((0, 235, 48), 20, 20)
