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


while(True):
	if r == 255 and g < 255 and b == 0:
		g += 1
	elif r > 0 and g == 255 and b == 0:
		r -= 1
	elif r == 0 and g == 255 and b < 255:
		b += 1
	elif r == 0 and g > 0 and b == 255:
		g -= 1
	elif r < 255 and g == 0 and b == 255:
		r += 1
	elif r == 255 and g == 0 and b > 0:
		b -= 1
	
	color = (r, g, b)
	
	setSmiley(color)
