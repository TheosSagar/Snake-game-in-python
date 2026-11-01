import pygame

pygame.init()

width = 480
height = 360
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

player = pygame.Rect(230, 160, 20, 20)
player2 = pygame.Rect(290, 190, 20, 20)

clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

game_over = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
        
    if not game_over:
        collide = pygame.Rect.colliderect(player, player2)
        keys = pygame.key.get_pressed()

        if (player.left <= 0 or player.right >= width or player.top <= 0 or player.bottom >= height):
            print("Hit the wall!!")
            game_over = True

        if keys[pygame.K_UP]:
            player.y -= 4

        if keys[pygame.K_DOWN]:
            player.y += 4

        if keys[pygame.K_LEFT]:
            player.x -= 4

        if keys[pygame.K_RIGHT]:
            player.x += 4

        if collide == True:
            game_over = True
            print("Collided!!")

    elif game_over:
        text = font.render("Game Over!", True, (255, 255, 255, 255), None)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
            

        
    pygame.draw.rect(screen, (210, 210, 255, 0), player)
    pygame.draw.rect(screen, (255, 10, 5, 0), player2)
    pygame.display.flip()

    clock.tick(60)
        