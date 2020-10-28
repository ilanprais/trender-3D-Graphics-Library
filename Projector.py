import numpy as np
import math

class Projector:

	def project(self, axis, angles, vector):

		vector = [vector[0] - axis[0], vector[1] - axis[1], vector[2] - axis[2]]

		projectionMatrix = np.array([[1, 0, 0], [0, 1, 0]])
		
		xMatrix = np.array([[1, 0, 0],[0, math.cos(math.radians(angles[0])), -1*math.sin(math.radians(angles[0]))], [0, math.sin(math.radians(angles[0])), math.cos(math.radians(angles[0]))]])
		yMatrix = zMatrix = np.array([[math.cos(math.radians(angles[1])), 0, math.sin(math.radians(angles[1]))], [0, 1, 0], [-1*math.sin(math.radians(angles[1])), 0, math.cos(math.radians(angles[1]))]])
		zMatrix = np.array([[math.cos(math.radians(angles[2])), -1*math.sin(math.radians(angles[2])), 0],[math.sin(math.radians(angles[2])), math.cos(math.radians(angles[2])), 0], [0, 0, 1]])

		rotation = xMatrix.dot(yMatrix).dot(zMatrix)
		rotated = rotation.dot(vector)
		result = projectionMatrix.dot(rotated)

		result = [result[0] + axis[0], result[1] + axis[1]]

		return result