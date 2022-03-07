import sys
import pygame
from math import floor
from pygame.locals import *

pygame.init()

width, height = 700, 600

DISPLAY = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect 4")

clock = pygame.time.Clock()

while True:
	DISPLAY.fill((0, 0, 0))
	mx, my = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	clock.tick(60)
