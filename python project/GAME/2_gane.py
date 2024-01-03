#drawing on display

import pygame #1

#Intiailize Pygame
pygame.init() #2

#Create a display surface and set its caption
WINDOW_WIDTH = 600 #3
WINDOW_HEIGHT = 600 #4
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #5
pygame.display.set_caption("Drawing Objects") #6

#Define colors as RGB tuples # 14
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGNETA = (255, 0, 255)

#Give a background color to the display
display_surface.fill(BLUE) # 15 Run the code now and check it will be black -- update the display--16

#Draw various shapes on our display
#Line(surface, color, starting point, ending point, thickness)
pygame.draw.line(display_surface, RED, (0,0), (100,100), 5) # 17 you can write RGB instead of colors
pygame.draw.line(display_surface, GREEN, (100,100), (200,300), 1)# 18

#Circle(surface, color, center, radius, thickness...0 for fill)
pygame.draw.circle(display_surface, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 200, 6) #19 -- // To avoid decimal value
pygame.draw.circle(display_surface, YELLOW, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 195, 0) #20 -- // To avoid decimal value

#Rectangle(surface, color, (top-left x, top-left y, width, height))
pygame.draw.rect(display_surface, CYAN, (500, 0, 100, 100)) #21
pygame.draw.rect(display_surface, MAGNETA, (500, 100, 50, 100)) #22

#The main game loop
running = True #7
while running: #8
    for event in pygame.event.get(): #9
        print(event) #10 Optional
        if event.type == pygame.QUIT: #11
            running = False #12

    #Update the display
    pygame.display.update() #16

#End the game
pygame.quit() #13

#======= Total 22