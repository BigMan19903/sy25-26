import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load sprites
player_image = pygame.image.load('fat_guy.png')
enemy_image = pygame.image.load('vegetable.png')

player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

player_mask = pygame.mask.from_surface(player_image)
enemy_mask = pygame.mask.from_surface(enemy_image)

font = pygame.font.SysFont(None, 36)

# Game variables
initial_player_speed = 5
player_speed = initial_player_speed
enemy_speed = 10

player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

enemies = []
initial_enemy_count = 1
for _ in range(initial_enemy_count):
    enemies.append([random.randint(0, WIDTH - 50), 0])

score = 0
past_scores = []

game_over = False
show_game_over_screen = False

# Ghost trail
trail_surface = pygame.Surface((WIDTH, HEIGHT))
trail_surface.set_alpha(50)
trail_surface.fill((0, 0, 0))

# Shake variables
shake_duration = 0
shake_magnitude = 20

# Speed cap
max_player_speed = initial_player_speed * 1.68
last_score_for_speed = 0

def trigger_shake(duration):
    global shake_duration
    shake_duration = duration

while True:
    if not show_game_over_screen:
        # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT]:
            player_pos[0] += player_speed

        if player_pos[0] < 0:
            player_pos[0] = 0
        elif player_pos[0] > WIDTH - player_size:
            player_pos[0] = WIDTH - player_size

        # Enemies update
        for enemy in enemies:
            enemy[1] += enemy_speed
        for i in range(len(enemies)):
            if enemies[i][1] > HEIGHT:
                enemies[i] = [random.randint(0, WIDTH - 50), 0]
                score += 1

        # Speed increase at score milestones
        if score // 12 > last_score_for_speed:
            potential_speed = player_speed * 1.25
            if potential_speed <= max_player_speed:
                player_speed = potential_speed
            else:
                player_speed = max_player_speed
            last_score_for_speed = score // 12

        # More enemies
        if score // 10 > len(enemies) - 1:
            enemies.append([random.randint(0, WIDTH - 50), 0])

        # Collision detection
        collision = False
        player_rect = pygame.Rect(player_pos[0], player_pos[1], 50, 50)
        for enemy in enemies:
            enemy_rect = pygame.Rect(enemy[0], enemy[1], 50, 50)
            offset_x = int(enemy_rect.x - player_rect.x)
            offset_y = int(enemy_rect.y - player_rect.y)
            if player_mask.overlap(enemy_mask, (offset_x, offset_y)):
                collision = True
                break

        if collision:
            past_scores.append(score)
            show_game_over_screen = True
            continue  # Skip to game over screen in next iteration

        # Near miss
        near_miss = False
        for enemy in enemies:
            dx = abs(enemy[0] + 50/2 - (player_pos[0] + 50/2))
            dy = abs(enemy[1] + 50/2 - (player_pos[1] + 50/2))
            if dx < 50 and dy < 50:
                near_miss = True
                break

        if near_miss:
            trigger_shake(10)

        # Ghost trail
        screen.blit(trail_surface, (0, 0))
        trail_surface.fill((0, 0, 0, 50))

        # Shake offset
        offset_x = offset_y = 0
        if shake_duration > 0:
            offset_x = random.randint(-shake_magnitude, shake_magnitude)
            offset_y = random.randint(-shake_magnitude, shake_magnitude)
            shake_duration -= 1

        # Draw everything
        screen.fill((255, 255, 255))
        for enemy in enemies:
            screen.blit(enemy_image, (enemy[0], enemy[1]))
        screen.blit(player_image, (player_pos[0], player_pos[1]))
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        temp_surface = pygame.Surface((WIDTH, HEIGHT))
        temp_surface.blit(screen, (0, 0))
        screen.fill((255, 255, 255))
        screen.blit(temp_surface, (offset_x, offset_y))
        pygame.display.flip()
        clock.tick(60)

    else:
        # Game Over Screen with scores
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Restart game
                    score = 0
                    player_speed = initial_player_speed
                    enemies.clear()
                    for _ in range(initial_enemy_count):
                        enemies.append([random.randint(0, WIDTH - 50), 0])
                    past_scores.append(score)
                    show_game_over_screen = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        # Draw styled "Game Over" box
        screen.fill((30, 30, 30))
        box_rect = pygame.Rect(50, HEIGHT//4, WIDTH - 100, HEIGHT//2)
        pygame.draw.rect(screen, (50, 50, 50), box_rect)
        pygame.draw.rect(screen, (200, 0, 0), box_rect, 5)

        # Large "Game Over" text
        game_over_text = font.render("GAME OVER!", True, (255, 255, 255))
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//4 + 20))

        # Instructions
        instruct_text = font.render("Press R to Restart or ESC to Quit", True, (255, 255, 255))
        screen.blit(instruct_text, (WIDTH//2 - instruct_text.get_width()//2, HEIGHT//4 + 60))

        # Show last scores
        scores_title = font.render("Past Scores:", True, (255, 255, 255))
        screen.blit(scores_title, (60, HEIGHT//2))
        for i, sc in enumerate(past_scores[-10:]):
            score_line = font.render(f"{i+1}. {sc}", True, (255, 255, 255))
            screen.blit(score_line, (80, HEIGHT//2 + 30 + i*30))

        pygame.display.flip()
        clock.tick(60)