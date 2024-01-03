import pygame

#Initialize pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Restricted Movement!")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5

#Load images
Owl_image = pygame.image.load("Owl.png")
Owl_rect = Owl_image.get_rect()
Owl_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
sound_1 = pygame.mixer.Sound('sound_1.wav')

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()
    print(keys)
    

    #Move the Owl continuously
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and Owl_rect.left > 0:
        Owl_rect.x -= VELOCITY
    sound_1.play()
    pygame.time.delay(20) 
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and Owl_rect.right < WINDOW_WIDTH:
        Owl_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and Owl_rect.top > 0:
        Owl_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and Owl_rect.bottom < WINDOW_HEIGHT:
        Owl_rect.y += VELOCITY
    
    #Fill the display
    display_surface.fill((0, 0, 0))

    
 

    #Blit assets
    display_surface.blit(Owl_image, Owl_rect)

    #Update the display
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

#End the game
pygame.quit()

