import trender

r = trender.trender(800, 600)
r.initialize()

line1 = r.line([100, 100, 100], [250, 250, 250])
cube1 = r.cube([250, 250, 250], 100, 100, 100)
cube1.setAngles([20, 20, 0])
line1.setAngles([20, 20, 0])

line1.bind(cube1)

r.add(line1)
r.add(cube1)

while r.isRunning():
	r.moveAllAngles([0, 3, 0])
	r.renderFrame()
	r.wait()


