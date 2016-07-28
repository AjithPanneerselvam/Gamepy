import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([600, 500])

def DrawBackground(background, xpos, ypos):
    screen.blit(background, [xpos, ypos])

background = pygame.image.load('beauty.jpg')
xpos = 0
ypos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #for y in range(5):
    	#for x in range(6):
	DrawBackground(background, 300, 300)

    pygame.display.flip()