import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen.")
screen.fill((0, 0, 0))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.draw.rect(screen, (255, 0, 0), (320, 240, 50, 50))
        pygame.display.flip()
print("Pungi")