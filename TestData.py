from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
	print(sense.get_accelerometer_raw())
	sleep(5)

