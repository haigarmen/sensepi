# This file has been written to your home directory for convenience. It is
# saved as "/home/pi/joystick_loop-2017-11-17-23-24-04.py"

#!/usr/bin/python3

import os
from sense_hat import SenseHat

# my python script that communications with Pd

def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + "' | pdsend 3000")

def sendNote(x):
    note = x + 60
    message = '1 ' + str(note) + ';' # make a string for use with Pdsend
    send2Pd(message)
    print(note)

x = y = 4
hat = SenseHat()

def update_screen():
    hat.clear()
    hat.set_pixel(x, y, 255, 255, 255)

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def move_dot(event):
    global x, y
    if event.action in ('pressed', 'held'):
        x = clamp(x + {
            'left': -1,
            'right': 1,
            }.get(event.direction, 0))
        y = clamp(y + {
            'up': -1,
            'down': 1,
            }.get(event.direction, 0))
    sendNote(x)

update_screen()

while True:
    for event in hat.stick.get_events():
        move_dot(event)
        update_screen()
