import pygame
stop = False
screen=pygame.display.set_mode((800,600))
img=pygame.image.load(r"p1.png")
img1=pygame.image.load(r"p2.png")	
while stop == False :
	for event in pygame.event.get():
		k=k=pygame.key.get_pressed()	
		if event.type == pygame.QUIT or k[pygame.K_ESCAPE]:
			stop =True
	screen.blit(img ,(0,0));screen.blit(img,(640,0))
	pygame.display.flip()
	pygame.time.wait(200)
	screen.blit(img1,(0,0))	;screen.blit(img1,(640,0))			
	pygame.display.flip()
	pygame.time.wait(100)
	
