import os

# my python script that communications with Pd

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