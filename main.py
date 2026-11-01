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
random_food_width = random.randint(0, width - 20)
random_food_height = random.randint(0, height - 20)

# Players
player = [pygame.Rect(230, 160, 20, 20)]
old_head = player[0].copy()

food = pygame.Rect(random_food_width, random_food_height, 20, 20)

# Clock for fixed frames for game
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)

direction = (0, 0) # For auto movement of the player
last_direction = (0, 0)

game_over = False # To Check if the game is over or not
food_exist = True

move_dely = 6
move_timer = 0
prev_positions = [player[0].copy()]   # NEW: where each segment was before the last step

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
        collide = pygame.Rect.colliderect(player[0], food)
        keys = pygame.key.get_pressed()

        if (player[0].left <= 0 or player[0].right >= width or player[0].top <= 0 or player[0].bottom >= height):
            print("Hit the wall!!")
            game_over = True

        if keys[pygame.K_UP] and last_direction != (0, 20):
            direction = (0, -20)

        elif keys[pygame.K_DOWN] and last_direction != (0, -20):
            direction = (0, 20)

        elif keys[pygame.K_LEFT] and last_direction != (20, 0):
            direction = (-20, 0)

        elif keys[pygame.K_RIGHT] and last_direction != (-20, 0):
            direction = (20, 0)

        move_timer += 1
        if move_timer >=  move_dely:
            move_timer = 0
            old_positions = [segment.copy() for segment in player]
            prev_positions = old_positions   # NEW: remember positions before this step

            player[0].x += direction[0]
            player[0].y += direction[1]

            collide = pygame.Rect.colliderect(player[0], food)

            for i in range(1, len(player)):
                player[i].topleft = old_positions[i-1].topleft

            last_direction = direction

            if collide:
                print("Ate!!")
                count += 1
                player.append(old_positions[-1].copy())

                random_food_width = random.randint(0, width - 20)
                random_food_height = random.randint(0, height - 20)
                food.topleft = (random_food_width, random_food_height)

            for segment in player[1:]:
                if player[0].colliderect(segment):
                    print("Collision with body")
                    game_over = True
                    break

    elif game_over:
        text = font.render("Game Over!", True, (255, 255, 255, 255), None)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        screen.blit(text, text_rect)

    # NEW: draw each segment sliding from its previous position to its current one
    t = 1 if game_over else move_timer / move_dely   # how far between steps (0 to 1)
    for i, segment in enumerate(player):
        if i < len(prev_positions):
            px, py = prev_positions[i].topleft
        else:
            px, py = segment.topleft
        draw_x = px + (segment.x - px) * t
        draw_y = py + (segment.y - py) * t
        pygame.draw.rect(screen, (210, 210, 255), (int(draw_x), int(draw_y), 20, 20))

    if food_exist:
        pygame.draw.rect(screen, (255, 10, 5, 0), food)

    pygame.display.flip()

    clock.tick(60)