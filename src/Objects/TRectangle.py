import pygame
import TShape

class TRectangle(TShape.TShape):

	def __init__(self, topLeft, width, height, color = (255, 255, 255)):
		# topLeft, topRight, bottomRight, bottomLeft
		self.topLeft = topLeft
		self.vertexes = []
		self.vertexes.append(topLeft)
		self.vertexes.append([topLeft[0] + width, topLeft[1], topLeft[2]])
		self.vertexes.append([topLeft[0] + width, topLeft[1] + height, topLeft[2]])
		self.vertexes.append([topLeft[0], topLeft[1] + height, topLeft[2]])
		super().__init__(self.vertexes, color)
		
	def generateAxis(self):
		return [(self.vertexes[0][0] + self.vertexes[2][0]) / 2, (self.vertexes[0][1] + self.vertexes[2][1]) / 2, (self.vertexes[0][2] + self.vertexes[2][2]) / 2]


