import trender

WIDTH = 800
HEIGHT = 600
BACKGROUND = (100, 80, 93)

r = trender.trender(WIDTH, HEIGHT)
r.background(BACKGROUND)
r.initialize()

pathLength = 6
pathWidth = 4


for i in range (pathWidth):
	for j in range (pathLength):
		cube = r.cube([200 + 105*i, HEIGHT - 120, j*105], 90, 90, 90)
		cube.setAngles([30, (-1 + i%3)*5, 0])
		r.add(cube)
		print(cube.vertexes[0][2])

while r.isRunning():
	r.moveAllLocations([0, 0, 5])
	# r.moveAllAngles([0, 0, 0])
	r.renderFrame()
	r.wait()


