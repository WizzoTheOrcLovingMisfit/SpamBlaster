import time

import pyautogui
from pynput import mouse



   
    

print('Enter your message:')
blaster = input()
 
with mouse.Events() as events:
    for event in events:
        print('Click your target')
        try:
            if event.button == mouse.Button.left:
                while 1: ''' Loop is broken by default with pyautogui's escape, putting the mouse in the top left corner'''
                    print('innit')
                    print(event.button)
                    pyautogui.press('enter')
                    pyautogui.write(blaster)    
                    time.sleep(.01)
            elif event.button == mouse.Button.right:  '''listener can be broken by right clicking'''  
                break 
            else:
                print(type(event))
        except:
                print(type(event))
                