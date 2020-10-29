import trender

r = trender.trender(800, 600)
r.background((100, 80, 93))
r.initialize()

objects = []

# Body
cube = r.cube([300, 230, 300], 200, 200, 200)
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
	obj.setAngles([20, 20, 0])
	obj.bind(cube)
	r.add(obj)

while r.isRunning():
	r.moveAllLocations([0 ,0 , 2])
	r.moveAllAngles([0, 2, 0])
	r.renderFrame()
	r.wait()


