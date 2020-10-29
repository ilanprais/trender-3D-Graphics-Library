import pygame
from Objects import TShape

class TRectangle(TShape.TShape):

	def __init__(self, topLeft, width, height, border, fill):
		# topLeft, topRight, bottomRight, bottomLeft
		self.topLeft = topLeft
		self.vertexes = []
		self.vertexes.append(topLeft)
		self.vertexes.append([topLeft[0] + width, topLeft[1], topLeft[2]])
		self.vertexes.append([topLeft[0] + width, topLeft[1] + height, topLeft[2]])
		self.vertexes.append([topLeft[0], topLeft[1] + height, topLeft[2]])
		super().__init__(self.vertexes, border)
		self.border = border
		self.fill = fill
		
	def generateAxis(self):
		return [(self.vertexes[0][0] + self.vertexes[2][0]) / 2, (self.vertexes[0][1] + self.vertexes[2][1]) / 2, (self.vertexes[0][2] + self.vertexes[2][2]) / 2]

	def display(self, surface):
		points = self.projectedVertexes()
		if self.fill:
			pygame.draw.polygon(surface, self.fill, (points[0], points[1], points[2], points[3]))
		for i in range (len(points) - 1):
			pygame.draw.line(surface, self.border, (points[i][0], points[i][1]),(points[i + 1][0], points[i + 1][1]))
		pygame.draw.line(surface, self.border, (points[len(points) - 1][0], points[len(points) - 1][1]),(points[0][0], points[0][1]))


