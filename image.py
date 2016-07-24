import pygame


pygame.init()


display_width = 1600
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Timon')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('tim.jpg')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.35)
y = (display_height * 0.20)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    gameDisplay.fill(white)
    car(x,y)

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()