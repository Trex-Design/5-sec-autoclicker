from pynput.mouse import Button, Controller
import time
import sys

mouse = Controller()
counter=0
while True:    
    print('on')
    time.sleep(.1)
    mouse.press(Button.left)
    mouse.release(Button.left)
    if counter==60:
        print('exit')
        sys.exit()
    else:
        counter+=1
