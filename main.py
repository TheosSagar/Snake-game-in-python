import pygame
import random

pygame.init()

# Setting up the display
width = 480
height = 360
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

count = 0

# Random food generation
random_food_width = random.randint(0, width - 5)
random_food_height = random.randint(0, height - 5)

# Players
player = pygame.Rect(230, 160, 20, 20)
player2 = pygame.Rect(random_food_width, random_food_height, 20, 20)

# Clock for fixed frames for game
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

direction = (0, 0) # For auto movement of the player

game_over = False # To Check if the game is over or not
food_exist = True

running = True # To keep the screen on
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    score = font.render(f"Score: {count}", True, (255, 255, 255, 255), None)
    score_rect = score.get_rect(topleft = (width - 470, height - 350))
    screen.blit(score, score_rect)

    if not game_over:
        collide = pygame.Rect.colliderect(player, player2)
        keys = pygame.key.get_pressed()

        if (player.left <= 0 or player.right >= width or player.top <= 0 or player.bottom >= height):
            print("Hit the wall!!")
            game_over = True

        if keys[pygame.K_UP]:
            direction = (0, -5)

        elif keys[pygame.K_DOWN]:
            direction = (0, 5)

        elif keys[pygame.K_LEFT]:
            direction = (-5, 0)

        elif keys[pygame.K_RIGHT]:
            direction = (5, 0)

        player.x += direction[0]
        player.y += direction[1]

        if collide == True:
            print("Ate!!")

            # Count Score
            count+=1

            # Random food generation
            random_food_width = random.randint(0, width - 5)
            random_food_height = random.randint(0, height - 5)

            player2.topleft = (random_food_width, random_food_height)

    elif game_over:
        text = font.render("Game Over!", True, (255, 255, 255, 255), None)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)
        
    pygame.draw.rect(screen, (210, 210, 255, 0), player)

    if food_exist:
        pygame.draw.rect(screen, (255, 10, 5, 0), player2)

    pygame.display.flip()

    clock.tick(30)
        