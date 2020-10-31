import pygame
from Objects import TShape

class TCube(TShape.TShape):

	def __init__(self, topLeft, width, height, depth, border, fill, projector):
		# topLeft, topRight, bottomRight, bottomLeft, again with depth
		self.vertexes = []
		self.vertexes.append(topLeft)
		self.vertexes.append([topLeft[0] + width, topLeft[1], topLeft[2]])
		self.vertexes.append([topLeft[0] + width, topLeft[1] + height, topLeft[2]])
		self.vertexes.append([topLeft[0], topLeft[1] + height, topLeft[2]])
		self.vertexes.append([topLeft[0], topLeft[1], topLeft[2] + depth])
		self.vertexes.append([topLeft[0] + width, topLeft[1], topLeft[2] + depth])
		self.vertexes.append([topLeft[0] + width, topLeft[1] + height, topLeft[2] + depth])
		self.vertexes.append([topLeft[0], topLeft[1] + height, topLeft[2] + depth])
		super().__init__(self.vertexes, fill, projector)
		self.border = border

	def generateAxis(self):
		return [(self.vertexes[0][0] + self.vertexes[6][0]) / 2, (self.vertexes[0][1] + self.vertexes[6][1]) / 2, (self.vertexes[0][2] + self.vertexes[6][2]) / 2]

	def display(self, surface):

		points = self.projectedVertexes()

		if self.fill != None:

			for i in [[0, 1, 2, 4], [1, 0, 4, 5], [4, 5, 6, 7], [7, 6, 2, 3], [3, 0, 4, 7], [2, 1, 5, 6]]:
				pygame.draw.polygon(surface, self.fill, (points[i[0]], points[i[1]], points[i[2]], points[i[3]]))

		for i in [0, 1, 2]:
			pygame.draw.line(surface, self.border, (points[i][0], points[i][1]),(points[i + 1][0], points[i + 1][1]))
		pygame.draw.line(surface, self.border, (points[3][0], points[3][1]),(points[0][0], points[0][1]))
		for j in [4, 5, 6]:
			pygame.draw.line(surface, self.border, (points[j][0], points[j][1]),(points[j + 1][0], points[j + 1][1]))
		pygame.draw.line(surface, self.border, (points[7][0], points[7][1]),(points[4][0], points[4][1]))
		for k in [0, 1, 2, 3]:
			pygame.draw.line(surface, self.border, (points[k][0], points[k][1]),(points[k + 4][0], points[k + 4][1]))


