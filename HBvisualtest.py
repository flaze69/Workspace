import pyautogui
import time
import keyboard
import random
import win32api, win32con

# 720 360
# 1180 820
#color rgb(255, 255, 255)
#square rgb(37, 115, 193)
#field rgb(43, 135, 209)

cx, cy, width, height = (725, 365, 460, 460)

def coords(pic):
    X_coords = []
    Y_coords = []
    prev = pic.getpixel((0, 0))

    for x in range(0, width):
        if pic.getpixel((x, 0)) != prev and pic.getpixel((x, 0))[0] == 43:
            X_coords.append(x-10)
        prev = pic.getpixel((x, 0))

    for y in range(0, height):
        if pic.getpixel((0, y)) != prev and pic.getpixel((0, y))[0] == 43:
            Y_coords.append(y-10)
        prev = pic.getpixel((0, y))

    X_coords.append(width-10)
    Y_coords.append(width-10)
    return X_coords, Y_coords

def form_net(X_coords, Y_coords):
    net = [(x, y) for x in X_coords for y in Y_coords]
    return net

def get_white_pos(pic, res):
    coords = []
    for x, y in res:
        if pic.getpixel((x, y))[0] == 255:
            coords.append((x, y))
    return coords

def click_white(coords):
    for x, y in coords:
        pyautogui.click(x+cx, y+cy)
        time.sleep(0.05)

keyboard.wait("s")
pyautogui.click(900, 700)
time.sleep(0.1)

while keyboard.is_pressed("q") != True:
    res = form_net(*coords(pyautogui.screenshot(region=(cx, cy, width, height))))
    time.sleep(1)

    pic = pyautogui.screenshot(region=(cx, cy, width, height))
    time.sleep(1)

    click_white(get_white_pos(pic, res))
    time.sleep(1.15)