import pygame

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blitting Images!")

#Create images...returns a Surface object with the image drawon on it.
#We can then get the rect of the surface and use the rect to position the image.
Owl_left_image = pygame.image.load("Owl_left.png")
Owl_left_rect = Owl_left_image.get_rect()
Owl_left_rect.topleft = (0,0)

Owl_right_image = pygame.image.load("Owl_right.png")
Owl_right_rect = Owl_right_image.get_rect()
Owl_right_rect.topright = (WINDOW_WIDTH, 0)

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit (copy) a surface object at the given coordinates to our display
    display_surface.blit(Owl_left_image, Owl_left_rect)
    display_surface.blit(Owl_right_image, Owl_right_rect)

    pygame.draw.line(display_surface, (255, 255, 255), (0, 75), (WINDOW_WIDTH, 75), 4)

    #Update the display
    pygame.display.update()

#End the game
pygame.quit()