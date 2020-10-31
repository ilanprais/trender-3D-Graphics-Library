import pygame
from Objects import TShape

class TPoint(TShape.TShape):

	def __init__(self, vector, fill, projector):
		super().__init__([vector], fill, projector)

	def generateAxis(self):
		return self.vertexes[0]

	def display(self, surface):
		point = self.projectedVertexes()[0]
		pygame.draw.circle(surface, self.fill, [int(point[0]), int(point[1])], 3)