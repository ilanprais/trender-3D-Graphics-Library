import numpy as np
import math

class Projector:

	def __init__(self, maxWidth, maxHeight, distance = 1.75):
		self.maxWidth = maxWidth
		self.maxHeight = maxHeight
		self.distance = distance

	def project(self, axis, angles, vector):

		vectorAtZero = [vector[0] - axis[0], vector[1] - axis[1], vector[2] - axis[2]]
		
		xMatrix = self.xMatrix(angles)
		yMatrix = self.yMatrix(angles)
		zMatrix = self.zMatrix(angles)

		rotation = xMatrix.dot(yMatrix).dot(zMatrix)
		rotated = rotation.dot(vectorAtZero)

		factor = (rotated[2] + axis[2])/500
		z = 1/(self.distance - factor)

		projMatrix = np.array([[z, 0, 0], [0, z, 0]])

		result = projMatrix.dot(rotated)
		result = [result[0] + axis[0], result[1] + axis[1]]

		return result

	def xMatrix(self, angles):
		matrix = np.array([[1, 0, 0],[0, math.cos(math.radians(angles[0])), -1*math.sin(math.radians(angles[0]))], [0, math.sin(math.radians(angles[0])), math.cos(math.radians(angles[0]))]])
		return matrix

	def yMatrix(self, angles):
		matrix = zMatrix = np.array([[math.cos(math.radians(angles[1])), 0, math.sin(math.radians(angles[1]))], [0, 1, 0], [-1*math.sin(math.radians(angles[1])), 0, math.cos(math.radians(angles[1]))]])
		return matrix

	def zMatrix(self, angles):
		matrix = np.array([[math.cos(math.radians(angles[2])), -1*math.sin(math.radians(angles[2])), 0],[math.sin(math.radians(angles[2])), math.cos(math.radians(angles[2])), 0], [0, 0, 1]])
		return matrix
