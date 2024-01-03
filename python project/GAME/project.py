import pygame, random

#Initialize Pygame
pygame.init()

#Create a display surface
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("eatting challenge!")

GREEN = (0, 255, 0)
DARKGREEN = (10, 50, 10)
BLACK = (0, 0, 0)
fonts = pygame.font.get_fonts()
#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5

#Load images
owl_image = pygame.image.load("Owl.png")
owl_rect = owl_image.get_rect()
owl_rect.topleft = (25, 25)

Rat_image = pygame.image.load("Rat.png")
Rat_rect = Rat_image.get_rect()
Rat_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
sound_1 = pygame.mixer.Sound('sound_1.wav')
music_1 = pygame.mixer.Sound('music_1.wav')


#Define text

#The main game loop
running = True
while running:
    sound_1.play()
    pygame.time.delay(20) 
    for event in pygame.event.get():
        music_1.play() #7 Test RUN
        pygame.time.delay(2)
        if event.type == pygame.QUIT:
            running = False
        
    #Get a list of all keys currently being pressed down
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and owl_rect.left > 0:
        owl_rect.x -= VELOCITY
    

    
    if keys[pygame.K_RIGHT] and owl_rect.right < WINDOW_WIDTH:
        owl_rect.x += VELOCITY
   
    if keys[pygame.K_UP] and owl_rect.top > 0:
        owl_rect.y -= VELOCITY
    if keys[pygame.K_DOWN] and owl_rect.bottom < WINDOW_HEIGHT:
        owl_rect.y += VELOCITY

    #Check for collision between two rects
    if owl_rect.colliderect(Rat_rect):
        print("HIT")
      
 
        
        Rat_rect.x = random.randint(0, WINDOW_WIDTH - 32)
        Rat_rect.y = random.randint(0, WINDOW_HEIGHT - 32)
  
    #Fill display surface
    display_surface.fill((0, 0, 0))

    #Draw rectangles to represent the rect's of each object
    pygame.draw.rect(display_surface, (0, 255, 0), owl_rect, 1)
    pygame.draw.rect(display_surface, (255, 255, 0), Rat_rect, 1)

    #Blit assets
    display_surface.blit(owl_image, owl_rect)
    display_surface.blit(Rat_image, Rat_rect)
    

    #Update dispaly
    pygame.display.update()

    #Tick the clock
    clock.tick(FPS)

#End the game
pygame.quit()
