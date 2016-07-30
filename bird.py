import pygame
stop = False
screen=pygame.display.set_mode((1600,800))
img=pygame.image.load(r"t1.png")
img1=pygame.image.load(r"t2.png")	
shadow = pygame.image.load(r'shadow.jpg')	
white = (255,255,255)
screen.fill(white)
pygame.draw.line(screen, (0, 0, 0), (400, 800), (400,0))
pygame.draw.line(screen, (0, 0, 0), (1200, 800), (1200,0))
screen.blit(shadow,(700,650))
while stop == False :
	for event in pygame.event.get():
		k=k=pygame.key.get_pressed()	
		if event.type == pygame.QUIT or k[pygame.K_ESCAPE]:
			stop =True
	screen.blit(img ,(100,400));
	pygame.display.flip()
	pygame.time.wait(100)
	screen.blit(img1,(1400,400))				
	pygame.display.flip()
	pygame.time.wait(100)
	
