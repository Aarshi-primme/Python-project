import pygame #1

#Initiailze pygame
pygame.init() #2

#Create a display surface and set its caption
WINDOW_WIDTH = 600 #3
WINDOW_HEIGHT = 300 #4
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #5 Test Run (Tuple -- window pops up and close)
pygame.display.set_caption("Hello semester2") #14

#The main game loop

running = True #6
while running: #7
    #pass #8 Test Run -- comment after run
    #Loop through a list of Event objects that have occured
    for event in pygame.event.get(): #9 keyboard and mouse event
        print(event) # 10 Test Run
        if event.type == pygame.QUIT: #11
            running = False #12

#End the game
pygame.quit() #13

# Total 14 Lines
