import pygame
from Objects import TShape

class TLine(TShape.TShape):

	def __init__(self, start, end, color = (255, 255, 255)):
		super().__init__([start, end], color)

	def generateAxis(self):
		return [(self.vertexes[0][0] + self.vertexes[1][0]) / 2 , (self.vertexes[0][1] + self.vertexes[1][1]) / 2, (self.vertexes[0][2] + self.vertexes[1][2]) / 2]

