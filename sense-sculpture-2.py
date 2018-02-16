from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()

pause = 0.1

# Define some colours
w = (255, 255, 255) #White 
b = (0, 0, 0) # Black

# Set up where each colour will display
# Display these colours on the LED matrix
while True:
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.clear((0, 0, 0))
    sense.set_pixel(x, y, (random.randint(100,255),random.randint(100,255),random.randint(100,255)))
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, (random.randint(100,255),random.randint(100,255),random.randint(100,255)))
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, (random.randint(100,255),random.randint(100,255),random.randint(100,255)))
    x = random.randint(0,7)
    y = random.randint(0,7)
    sense.set_pixel(x, y, (random.randint(100,255),random.randint(100,255),random.randint(100,255)))
    sleep(pause)
