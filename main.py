import pyautogui as pag
import time

for i in range(1, 500): # This will like 500 creations
    time.sleep(1)
    pag.moveTo(900, 200)
    pag.click()
    pag.moveTo(1310, 425, 1)
    pag.click()
