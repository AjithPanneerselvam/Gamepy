import pygame

class Game(object):
 def run(self,screen):
  image=pygame.image.load(r"k.png")
  image_x=10
  image_y=10
  clock=pygame.time.Clock()
  while 1:
   clock.tick(30)
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
     return
    if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
     return
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
     image_x=image_x-10
    if key[pygame.K_RIGHT]:
     image_x=image_x+10
    if key[pygame.K_DOWN]:
     image_y=image_y+10
    if key[pygame.K_UP]:
     image_y=image_y-10
    screen.fill((200,200,200))
    screen.blit(image,(image_x,image_y))
    pygame.display.flip()
if __name__ == '__main__':
	pygame.init()
	screen=pygame.display.set_mode((400,400))
	Game().run(screen)
