import mouse
import keyboard
import time

#включение / выключение
isClick = False
def set_clicker():
    global isClick
    if isClick:
        isClick = False
    else:
        isClick = True

# кнопка для включения / выключения
keyboard.add_hotkey('CTRL + F6', set_clicker)

# нажатие левой кнопки мышки
while True:
    if isClick:
        mouse.click(button='left')
        time.sleep(0.01)