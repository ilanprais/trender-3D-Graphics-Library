import trender

WIDTH = 800
HEIGHT = 600
BACKGROUND = (100, 80, 93)

r = trender.trender(WIDTH, HEIGHT)
r.background(BACKGROUND)
r.initialize()
r.cameraDistance(1.3)


objects = []

# Body
cube = r.cube([300, 230, 300], 200, 200, 200)
cube.fill = [50, 50, 50]
objects.append(cube)

# Roof
line1 = r.line([300, 230, 300], [400, 130, 400])
objects.append(line1)

line2 = r.line([500, 230, 300], [400, 130, 400])
objects.append(line2)

line3 = r.line([300, 230, 500], [400, 130, 400])
objects.append(line3)

line4 = r.line([500, 230, 500], [400, 130, 400])
objects.append(line4)

# door
rect1 = r.rectangle([375, 330, 300], 50, 100)
objects.append(rect1)

rect2 = r.rectangle([385, 375, 300], 5, 5)
objects.append(rect2)

for obj in objects:
	obj.setAngles([0, 0, 0])
	obj.bind(cube)
	r.add(obj)

while r.isRunning():
	# r.moveAllLocations([0, 0, 5])
	r.moveAllAngles([0, 2, 0])
	r.renderFrame()
	r.wait()


