import sys
import pygame
from pygame.locals import *

pygame.init()

width, height = 700, 600

DISPLAY = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect 4")

clock = pygame.time.Clock()

size = 100

class Game:
	r = 40

	def __init__(self) -> None:
		self.grid = [[None for rank in range(6)] for file in range(7)]
		self.activeColor = "r"
	
	def reset(self):
		self.grid = [[None for rank in range(6)] for file in range(7)]
		self.activeColor = "r"

	def showGrid(self):
		for i, file in enumerate(self.grid):
			for j, rank in enumerate(file):
				color = self.getColor(rank)
				pygame.draw.circle(DISPLAY, color, (i * size + 50, j * size + 50), self.r)
	
	def getCorrectRankInFile(self, file):
		for i in reversed(range(6)):
			if self.grid[file][i] is None:
				return i
		else:
			return -1
	
	def addDisc(self, file):
		rank = self.getCorrectRankInFile(file)
		if rank == -1: return

		self.grid[file][rank] = self.activeColor
		if self.check_if_won(file, rank) == 1:
			self.reset()
			print(f"{self.activeColor} won")

		self.activeColor = "y" if (self.activeColor == "r") else "r"
	
	def getColor(self, rank):
		color = (229, 229, 229)
		if rank is not None:
			if rank == "r": color = (255, 65, 52)
			if rank == "y": color = (243, 236, 36)
		return color
	
	def check_if_won(self, file, rank):
		directions = [
			[-1, 0],
			[1, 0],
			[0, -1],
			[0, 1],
			[-1, -1],
			[1, 1],
			[-1, 1],
			[1, -1],
		]

		letter_to_check = self.grid[file][rank]

		for offset in directions:
			temp_f, temp_r = file, rank
			for i in range(3):
				temp_f += offset[0]
				temp_r += offset[1]
				try:
					if self.grid[temp_f][temp_r] != letter_to_check:
						break
				except: break
			else:
				return 1
		return -1

game = Game()

while True:
	DISPLAY.fill((12, 79, 220))
	mx, my = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == MOUSEBUTTONDOWN:
			game.addDisc(mx // size)

	game.showGrid()

	file = mx // size
	rank = game.getCorrectRankInFile(file)
	if rank != -1:
		color = pygame.Color(*game.getColor(game.activeColor))
		color = color.lerp(pygame.Color(229, 229, 229), 0.3)
		pygame.draw.circle(DISPLAY, color, (file * size + 50, rank * size + 50), game.r)

	pygame.display.update()
	clock.tick(60)
