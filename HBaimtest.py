import pyautogui
import time
import keyboard
import random
import win32api, win32con

# 400 350
# 1600 350
#color rgb(149, 195, 232)

time.sleep(2)
cx, cy, width, height = (400, 350, 1200, 380)

while keyboard.is_pressed("q") == False:
    flag = 0
    pic = pyautogui.screenshot(region=(cx, cy, width, height))
    
    for x in range(0, width, 20):
        for y in range(0, height, 10):

            r, g, b = pic.getpixel((x, y))

            if r == 149 and b == 232:
                flag = 1
                pyautogui.click(x+cx, y+cy)
                time.sleep(0.01)
                break

        if flag == 1:
            break

