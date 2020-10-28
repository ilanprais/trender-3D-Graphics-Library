import pygame
from Objects import TLine
from Objects import TPoint
from Objects import TRectangle
from Objects import TCube

class trender:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.running = True
		self.shapes = []

	def initialize(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))

	def add(self, shape):
		self.shapes.append(shape)

	def point(self, point, color = (255, 255, 255)):
		return TPoint.TPoint(point, color)

	def line(self, start, end, color = (255, 255, 255)):
		return TLine.TLine(start, end, color)

	def rectangle(self, topLeft, width, height, color = (255, 255, 255)):
		return TRectangle.TRectangle(topLeft, width, height, color)

	def cube(self, topLeft, width, height, depth, color = (255, 255, 255)):
		return TCube.TCube(topLeft, width, height, depth, color)

	def moveAllLocations(self, vector):
		for shape in self.shapes:
			shape.moveLocation(vector)

	def moveAllAngles(self, vector):
		for shape in self.shapes:
			shape.moveAngles(vector)

	def wait(self, interval = 50):
		pygame.time.wait(interval)

	def isRunning(self):
		return self.running

	def renderFrame(self):
		self.screen.fill((0, 0, 0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

		for shape in self.shapes:
			shape.display(self.screen)

		pygame.display.update()

	def render(self, interval = 50):
		self.running = True

		while self.running:
			self.renderFrame()
			self.wait(interval)

		    
