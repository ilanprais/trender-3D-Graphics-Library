import pygame
from Projection import Projector

class TShape:

	def __init__(self, vertexes, color = (255, 255, 255)):
		self.vertexes = vertexes
		self.color = color
		self.angles = [0, 0, 0]
		self.axis = self.generateAxis()
		self.projector = Projector.Projector()

	def projectedVertexes(self):
		projected = []
		for ver in self.vertexes:
			projected.append(self.projector.project(self.axis, self.angles, ver))
		return projected

	def generateAxis(self):
		pass

	def bind(self, other):
		self.axis = other.axis

	def resetAxis(self):
		self.axis = self.generateAxis()

	def setAngles(self, angles):
		self.angles = angles

	def moveLocation(self, vector):
		for ver in self.vertexes:
			for i in [0, 1, 2]:
				ver[i] += vector[i]

	def moveAngles(self, vector):
		for i in [0, 1, 2]:
			self.angles[i] += vector[i]

	def display(self, surface):
		points = self.projectedVertexes()
		for i in range (len(points) - 1):
			pygame.draw.line(surface, self.color, (points[i][0], points[i][1]),(points[i + 1][0], points[i + 1][1]))
		pygame.draw.line(surface, self.color, (points[len(points) - 1][0], points[len(points) - 1][1]),(points[0][0], points[0][1]))