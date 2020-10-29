import pygame
from Objects import TShape

class TLine(TShape.TShape):

	def __init__(self, start, end, fill = (255, 255, 255)):
		super().__init__([start, end], fill)

	def generateAxis(self):
		return [(self.vertexes[0][0] + self.vertexes[1][0]) / 2 , (self.vertexes[0][1] + self.vertexes[1][1]) / 2, (self.vertexes[0][2] + self.vertexes[1][2]) / 2]

	def display(self, surface):
		points = self.projectedVertexes()
		for i in range (len(points) - 1):
			pygame.draw.line(surface, self.fill, (points[i][0], points[i][1]),(points[i + 1][0], points[i + 1][1]))
		pygame.draw.line(surface, self.fill, (points[len(points) - 1][0], points[len(points) - 1][1]),(points[0][0], points[0][1]))
