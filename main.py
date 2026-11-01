import pygame

pygame.init()

width = 480
height = 360
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

player = pygame.Rect(230, 160, 20, 20)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player.y -= 4

        if keys[pygame.K_DOWN]:
            player.y += 4

        if keys[pygame.K_LEFT]:
            player.x -= 4

        if keys[pygame.K_RIGHT]:
            player.x += 4

        screen.fill((0, 0, 0))
        
        pygame.draw.rect(screen, (210, 210, 255, 0), player)
        pygame.display.flip()
        