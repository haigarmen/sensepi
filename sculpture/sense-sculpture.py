from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

pause = 0.01

# Define some colours
w = (255, 255, 255) #White 
b = (0, 0, 0) # Black

# Set up where each colour will display
frame_1 = [
    w, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
]

frame_2 = [
    b, b, b, b, b, b, b, b,
    w, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
]

frame_3 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    w, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
]

frame_4 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    w, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
]

frame_5 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    w, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
]
frame_6 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    w, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
]

frame_7 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    w, w, w, w, w, w, w, w,
    b, b, b, b, b, b, b, b,
]
frame_8 = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    w, w, w, w, w, w, w, w,
]

# Display these colours on the LED matrix
while True:
    sense.set_pixels(frame_1)
    sleep(pause)
    sense.set_pixels(frame_2)
    sleep(pause)
    sense.set_pixels(frame_3)
    sleep(pause)
    sense.set_pixels(frame_4)
    sleep(pause)
    sense.set_pixels(frame_5)
    sleep(pause)
    sense.set_pixels(frame_6)
    sleep(pause)
    sense.set_pixels(frame_7)
    sleep(pause)
    sense.set_pixels(frame_8)
    sleep(pause)

#sense.set_pixels(frame_3)
