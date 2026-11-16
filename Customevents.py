import pygame
import random

pygame.init()

Width, height = 400, 500
Screen = pygame.display.set_mode((Width, height))
pygame.display.set_caption("Sprite Collision")

Movement_speed = 5
Font_size = 36  # Increased so the text is actually readable

font = pygame.font.SysFont("Times New Roman", Font_size)

# Load background image
background = pygame.transform.scale(
    pygame.image.load('C:\\Users\\Agrim\\OneDrive - GEMS EDUCATION\\Desktop\\Python lessons\\Pygame\\Lesson 4\\Nice bg.jfif').convert(), 
    (Width, height)
)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        self.rect.x = max((min(self.rect.x + x_change, Width - self.rect.width)), 0)
        self.rect.y = max((min(self.rect.y + y_change, height - self.rect.height)), 0)

# Create sprite groups and objects
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

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * Movement_speed
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * Movement_speed
        sprite1.move(x_change, y_change)

        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    # --- DRAWING SECTION ---
    # 1. Draw background first
    Screen.blit(background, (0, 0))

    # 2. Draw surviving sprites
    all_sprites.draw(Screen)

    # 3. Draw win text LAST so it's always on top of everything
    if won:
        # Changed to white so it pops out against your background!
        win_text = font.render("You win!", True, pygame.Color('white'))
        
        # Optional: Add a black shadow/outline effect so it's super easy to read
        shadow_text = font.render("You win!", True, pygame.Color('black'))
        
        text_x = (Width - win_text.get_width()) // 2
        text_y = (height - win_text.get_height()) // 2
        
        # Blit shadow slightly offset, then real text on top
        Screen.blit(shadow_text, (text_x + 2, text_y + 2))
        Screen.blit(win_text, (text_x, text_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
