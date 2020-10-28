import pygame
import Projector
import TShape

class TPoint(TShape.TShape):

	def __init__(self, vector, color = (255, 255, 255)):
		super().__init__([vector], color)

	def generateAxis(self):
		return self.vertexes[0]

	def display(self, surface):
		point = self.projectedVertexes()[0]
		pygame.draw.circle(surface, self.color, [int(point[0]), int(point[1])], 3)