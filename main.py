import pyautogui
from time import sleep
import os

os.system('start calc.exe')
while not pyautogui.locateOnScreen('7.png'):
    pass
with open('Problem.txt', 'r') as f:
    for Text in f.readline().split():
        if (Text == '+'):
            Text = 'Addition'
        if (Text == '='):
            Text = 'Equal'
        pyautogui.click(Text+'.png')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('alt', 'f4')
os.system('start notepad.exe Problem.txt')
sleep(2)
pyautogui.hotkey('end')
pyautogui.hotkey('ctrl', 'v')
