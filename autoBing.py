import pyautogui
import random
import ctypes

iterations = int(input('Enter number of searches: ')) - 1

def bing():
    text = open('SearchText.txt')
    words = text.read()
    sample = random.sample(words.split(), 6)
    search = ' '.join(sample)
    print(search) # Ignore. To check if the search string is working properly.

    # Automation script
    pyautogui.press('win', interval=0.5)
    pyautogui.typewrite('bing.com', interval=0.07)
    pyautogui.press('enter', interval=2)
    pyautogui.typewrite(search, interval=0.1)
    pyautogui.press('enter', interval=1.5)
    pyautogui.press('space', interval=1)
    pyautogui.press('pageup', interval=1)

def bing2():
    text = open('SearchText.txt')
    words = text.read()
    sample = random.sample(words.split(), 6)
    search = ' '.join(sample)
    print(search)  # Ignore. To check if the search string is working properly.

    # Automation script
    pyautogui.hotkey('ctrl', 't', interval=0.5)
    pyautogui.typewrite(search, interval=0.07)
    pyautogui.press('enter', interval=1)
    pyautogui.press('space', interval=1)
    pyautogui.press('pageup', interval=1)

bing()

for i in range(iterations):
    x = bing2()

ctypes.windll.user32.MessageBoxW(None, "The script has finished searching " + str(iterations + 1) + " times.", "bingCash", 0)
<<<<<<< HEAD
=======

pyautogui.press('~', interval=2)
pyautogui.hotkey('alt', 'shift', 'tab', interval=0)
>>>>>>> 25431d6ddf534c945a8be056735b8613d7fff34d
