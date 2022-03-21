#prank with your friend with this program
#Code by SecretBeast_bg01

import random
import pyautogui as pg
import time

foryourfriend =('son of a bit**','mother fu***','sister fu**','scu***k','chutiya')

time.sleep(10)
for i in range(2000):
    a = random.choice(foryourfriend)
    pg.write('you '+a)
    pg.press('enter')

