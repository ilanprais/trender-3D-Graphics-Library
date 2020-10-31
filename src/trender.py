import pygame
from Projection import Projector
from Objects import TLine
from Objects import TPoint
from Objects import TRectangle
from Objects import TCube

class trender:

	def __init__(self, width, height, color = (0, 0, 0)):
		self.width = width
		self.height = height
		self.color = color
		self.running = True
		self.shapes = []
		self.projector = Projector.Projector(width, height)

	def initialize(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.width, self.height))

	def add(self, shape):
		self.shapes.append(shape)

	def point(self, point, color = (255, 255, 255)):
		return TPoint.TPoint(point, color, self.projector)

	def line(self, start, end, color = (255, 255, 255)):
		return TLine.TLine(start, end, color, self.projector)

	def rectangle(self, topLeft, width, height, border = (255, 255, 255), fill = None):
		return TRectangle.TRectangle(topLeft, width, height, border, fill, self.projector)

	def cube(self, topLeft, width, height, depth, border = (255, 255, 255), fill = None):
		return TCube.TCube(topLeft, width, height, depth, border, fill, self.projector)

	def cameraDistance(self, dist):
		self.projector.distance = dist

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

	def background(self, color):
		self.color = color

	def renderFrame(self):
		self.screen.fill(self.color)
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

		    
