from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
	print("x: {x}, y: {y}, z: {z}".format(**sense.get_accelerometer_raw())

