import os
#!/usr/bin/python3
from sense_hat import SenseHat
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

update_screen()

def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + "' | pdsend 3000")
    
def audioOn():
    message = '0 1;' #Id=0 (DSP), message=1 (turn it on)
    send2Pd(message)
    
def setVolume():
    vol = 80 # set volume value (0-100)
    message = '1 ' + str(vol) + ';' # make a string for use with Pdsend
    send2Pd(message)
    
def send_note(event):
    global x, y
    message = '1 '+ str(x) +';'
    send2Pd(message)
    print(message)
    
while True:
    for event in hat.stick.get_events():
        move_dot(event)
        send_note(event)
        update_screen()