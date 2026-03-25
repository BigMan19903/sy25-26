import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load sprites (make sure these images are in the same directory)
player_image = pygame.image.load('fat_guy.png')
enemy_image = pygame.image.load('vegetable.png')

# Scale sprites if needed
player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_speed = 10

# List of enemies (positions)
enemies = []
initial_enemy_count = 1
for _ in range(initial_enemy_count):
    enemies.append([random.randint(0, WIDTH - enemy_size), 0])

score = 0
game_over = False

# Create a surface for ghost trail
trail_surface = pygame.Surface((WIDTH, HEIGHT))
trail_surface.set_alpha(50)
trail_surface.fill((0, 0, 0))

# Screen shake variables
shake_duration = 0
shake_magnitude = 20  # Stronger shake

def trigger_shake(duration):
    global shake_duration
    shake_duration = duration

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5

    # Keep player within bounds
    if player_pos[0] < 0:
        player_pos[0] = 0
    elif player_pos[0] > WIDTH - player_size:
        player_pos[0] = WIDTH - player_size

    # Update enemies
    for enemy in enemies:
        enemy[1] += enemy_speed

    # Reset enemies and increase difficulty
    for i in range(len(enemies)):
        if enemies[i][1] > HEIGHT:
            enemies[i] = [random.randint(0, WIDTH - enemy_size), 0]
            score += 1

    # Add more enemies as score increases
    if score // 10 > len(enemies) - 1:
        enemies.append([random.randint(0, WIDTH - enemy_size), 0])
        enemy_speed = 10 + score * 0.2

    # Collision detection
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    collision = False
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)
        if player_rect.colliderect(enemy_rect):
            collision = True
            break

    if collision:
        print("Game Over!")
        game_over = True

    # Detect near misses (within 50 pixels)
    near_miss = False
    for enemy in enemies:
        dx = abs(enemy[0] + enemy_size/2 - (player_pos[0] + player_size/2))
        dy = abs(enemy[1] + enemy_size/2 - (player_pos[1] + player_size/2))
        if dx < 50 and dy < 50 and not player_rect.colliderect(pygame.Rect(enemy[0], enemy[1], enemy_size, enemy_size)):
            near_miss = True
            break

    if near_miss:
        trigger_shake(10)  # Shake for 10 frames

    # Draw ghost trail
    screen.blit(trail_surface, (0, 0))
    trail_surface.fill((0, 0, 0, 50))

    # Apply screen shake offset if active
    offset_x = offset_y = 0
    if shake_duration > 0:
        offset_x = random.randint(-shake_magnitude, shake_magnitude)
        offset_y = random.randint(-shake_magnitude, shake_magnitude)
        shake_duration -= 1
    else:
        shake_duration = 0

    # Draw enemies (vegetables)
    for enemy in enemies:
        screen.blit(enemy_image, (enemy[0], enemy[1]))
    # Draw player (fat guy)
    screen.blit(player_image, (player_pos[0], player_pos[1]))

    # Apply offset for shake
    temp_surface = pygame.Surface((WIDTH, HEIGHT))
    temp_surface.blit(screen, (0, 0))
    screen.fill((0, 0, 0))
    screen.blit(temp_surface, (offset_x, offset_y))

    pygame.display.update()
    clock.tick(30)

pygame.quit()