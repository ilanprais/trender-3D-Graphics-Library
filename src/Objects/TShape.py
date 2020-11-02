import pygame
from Projection import Projector

class TShape:

	def __init__(self, vertexes, fill, projector):
		self.vertexes = vertexes
		self.fill = fill
		self.angles = [0, 0, 0]
		self.axis = self.generateAxis()
		self.projector = projector
		self.binded = None

	def projectedVertexes(self):
		projected = []
		for ver in self.vertexes:
			projected.append(self.projector.project(self.axis, self.angles, ver))
		return projected

	def generateAxis(self):
		pass

	def bind(self, other):
		self.axis = other.axis
		self.binded = other

	def resetAxis(self):
		self.axis = self.generateAxis()

	def setAngles(self, angles):
		self.angles = angles

	def moveLocation(self, vector):
		for ver in self.vertexes:
			for i in [0, 1, 2]:
				ver[i] += vector[i]

		if self.binded == None or self.binded == self:
			self.axis = [self.generateAxis()[0], self.generateAxis()[1], self.generateAxis()[2]]	
		else:
			self.axis = self.binded.axis

	def moveAngles(self, vector):
		for i in [0, 1, 2]:
			self.angles[i] += vector[i]

	def display(self, surface):
		pass