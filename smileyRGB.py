from sense_hat import SenseHat

sense = SenseHat()

def setSmiley(color = (255, 0, 0)):
 X = color
 O = (0, 0, 0)
 pixels = [
  O, O, O, O, O, O, O, O,
  O, X, X, O, O, X, X, O,
  O, X, X, O, O, X, X, O,
  O, O, O, O, O, O, O, O,
  O, O, O, O, O, O, O, O,
  O, X, O, O, O, O, X, O,
  O, O, X, X, X, X, O, O,
  O, O, O, O, O, O, O, O
 ]
 sense.set_pixels(pixels)

r = 255
g = 0
b = 0

print(sense.get_gyroscope()["yaw"])

while(True):
	rotation = sense.get_gyroscope()["yaw"]
	if 45 <= rotation < 135:
		sense.set_rotation(180)
	elif 135 <= rotation < 225:
		sense.set_rotation(90)
	elif 225 <= rotation < 315:
		sense.set_rotation(0)
	elif 315 <= rotation <= 360 or 0 <= rotation < 45:
		sense.set_rotation(270)

	if r == 255 and g < 255 and b == 0:
		g += 5
	elif r > 0 and g == 255 and b == 0:
		r -= 5
	elif r == 0 and g == 255 and b < 255:
		b += 5
	elif r == 0 and g > 0 and b == 255:
		g -= 5
	elif r < 255 and g == 0 and b == 255:
		r += 5
	elif r == 255 and g == 0 and b > 0:
		b -= 5

	color = (r, g, b)
	
	setSmiley(color)
