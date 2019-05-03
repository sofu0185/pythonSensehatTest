from sense_hat import SenseHat

sense = SenseHat()

while True:
	raw = sense.get_accelerometer_raw()
	print("x: {x}, y: {y}, z: {z}".format(**raw))
