from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

def setSmiley(color = (255, 0, 0)):
  X = color
  O = (0, 0, 0)
  pixels = [
   O, O, O, O, O, O, O, O,
   O, X, X, O, O, X, X, O,
   O, X, X, O, O, X, X, O,
   O, O, O, O, O, O, O, O,
   O, X, O, O, O, O, X, O,
   O, X, O, O, O, O, X, O,
   O, O, X, X, X, X, O, O,
   O, O, O, O, O, O, O, O
  ]
  sense.set_pixels(pixels)


while(True):
  sense.set_rotation(0)
  setSmiley()
  sleep(.3)

  sense.set_rotation(90)
  setSmiley((0, 255, 0))
  sleep(.3)

  sense.set_rotation(180)
  setSmiley((0, 0, 255))
  sleep(.3)

  sense.set_rotation(270)
  setSmiley((255, 255, 255))
  sleep(.3)
