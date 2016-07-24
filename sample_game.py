"""
A game to be built using pygame module

import os, sys, math, pygame, pygame.mixer
from pygame.locals import *

#Defining some basic colors
black = 0,
""" 

import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class PygView(object):


    def __init__(self, width=640, height=400, fps=30):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        #self.height = width // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 20, bold=True)


    def load_image(self, name, colorkey=None):
	 	fullname = os.path.join('data\images', name)
		try:
   	 		image = pygame.image.load(fullname)
		except pygame.error, message:
			print 'Cannot load image:', name
    		raise SystemExit, message
		image = image.convert()

		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
        	image.set_colorkey(colorkey, RLEACCEL)

		return image, image.get_rect()


    def run(self):
        """The mainloop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            #self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
             #              self.clock.get_fps(), " "*5, self.playtime))
            self.load_image('tim.jpg')

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()


    def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text) # fw: font width,  fh: font height
        surface = self.font.render(text, True, (0, 255, 0))
        # // makes integer division in python3
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

 	

####

if __name__ == '__main__':

    # call with width of window and fps
    PygView(640, 400).run()