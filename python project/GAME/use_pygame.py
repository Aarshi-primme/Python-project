import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")

fps= 0
clocl = pygame.time.Clock()

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 5

paddle1_x = 50
paddle1_y = window_height // 2 - paddle_height // 2

paddle2_x = window_width - 50 - paddle_width
paddle2_y = window_height // 2 - paddle_height // 2

# Set up the ball
ball_x = window_width // 2
ball_y = window_height // 2
ball_radius = 8
ball_speed_x = random.choice([-2, 2])
ball_speed_y = random.choice([-2, 2])

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < window_height - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < window_height - paddle_height:
        paddle2_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y <= ball_y <= paddle1_y + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= paddle2_x - ball_radius and paddle2_y <= ball_y <= paddle2_y + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= window_height - ball_radius:
        ball_speed_y = -ball_speed_y

    # Clear the screen
    window.fill(black)

    # Draw the paddles and ball
    pygame.draw.rect(window, white, (paddle1_x, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(window, white, (paddle2_x, paddle2_y, paddle_width, paddle_height))
    pygame.draw.circle(window, white, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()