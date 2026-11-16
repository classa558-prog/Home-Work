import random
import pygame
pygame.init()
Width, height = 500, 400
Movement_speed = 5
Screen = pygame.display.set_mode([400, 500])
running = True
class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        super.__init__()
        self.image = pygame.Surface([width, height])
        self.color = self.image.fill(color)
        self.rect = self.image.get_rect()
    def update(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, 500 - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, 400 - self.rect.width), 0)
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x = random.randint(0, Width - sprite1.rect.width)
sprite1.rect.y = random.randint(0, height - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x = random.randint(0, Width - sprite2.rect.width)
sprite2.rect.y = random.randint(0, height - sprite2.rect.height)
all_sprites.add(sprite2)  # Fixed: added sprite2 instead of sprite1 again
running, won = True, False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * Movement_speed
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * Movement_speed
    sprite1.move(x_change, y_change)
    all_sprites.draw(Screen)
    pygame.display.flip()


    