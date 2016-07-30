import pygame
stop = False
screen=pygame.display.set_mode((600,600))
img=pygame.image.load(r"t1.png")
img1=pygame.image.load(r"t2.png")	
while stop == False :
	for event in pygame.event.get():
		k=k=pygame.key.get_pressed()	
		if event.type == pygame.QUIT or k[pygame.K_ESCAPE]:
			stop =True
	screen.blit(img ,(0,0));
	pygame.display.flip()
	pygame.time.wait(100)
	screen.blit(img1,(0,0))				
	pygame.display.flip()
	pygame.time.wait(100)
	
