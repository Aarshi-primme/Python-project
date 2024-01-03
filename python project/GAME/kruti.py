import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bottle Shooter")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 10

# Set up the bottle
bottle_size = 50
bottle_x = random.randint(0, width - bottle_size)
bottle_y = random.randint(50, 150)
bottle_speed = 5

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_x += player_speed
            if event.key == pygame.K_SPACE:
                if abs(player_x - bottle_x) < bottle_size and abs(player_y - bottle_y) < bottle_size:
                    bottle_x = random.randint(0, width - bottle_size)
                    bottle_y = random.randint(50, 150)

    # Update game objects
    player_x = max(0, min(width - player_size, player_x))
    bottle_y += bottle_speed

    # Check for collision with the bottle
    if abs(player_x - bottle_x) < bottle_size and abs(player_y - bottle_y) < bottle_size:
        bottle_x = random.randint(0, width - bottle_size)
        bottle_y = random.randint(50, 150)

    # Clear the screen
    screen.fill(black)

    # Draw the player
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    # Draw the bottle
    pygame.draw.rect(screen, white, (bottle_x, bottle_y, bottle_size, bottle_size))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
