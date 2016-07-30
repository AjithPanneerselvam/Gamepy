import pygame
import random

stop = False
screen=pygame.display.set_mode((1600,800))
img=pygame.image.load(r"data/images/tree.png")
img1=pygame.image.load(r"data/images/coconut.png")
shadow = pygame.image.load(r'data/images/shadow.jpg')

white = (255,255,255)
screen.fill(white)
pygame.draw.line(screen, (0, 0, 0), (500, 800), (500,0))
pygame.draw.line(screen, (0, 0, 0), (1100, 800), (1100,0))
screen.blit(shadow,(700,650))

while stop == False :
	for event in pygame.event.get():
		k=k=pygame.key.get_pressed()	
		if event.type == pygame.QUIT or k[pygame.K_ESCAPE]:
			stop =True

	screen.fill(white)
	pygame.draw.line(screen, (0, 0, 0), (500, 800), (500,0))
	pygame.draw.line(screen, (0, 0, 0), (1100, 800), (1100,0))
	screen.blit(shadow,(700,650))

	row = random.randrange(100,600,50)
	screen.blit(img ,(100,row));
	pygame.display.flip()
	pygame.time.wait(600)

	row = random.randrange(100,600,50)
	screen.blit(img1,(1200,row))				
	pygame.display.flip()
	pygame.time.wait(100)

pygame.quit()
	
