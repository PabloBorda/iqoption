import pyautogui
x, y = pyautogui.locateCenterOnScreen("buy.png", confidence=.9)
pyautogui.moveTo(x, y, .25)
pyautogui.click()