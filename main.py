# install pip install pyautogui
# https://pyautogui.readthedocs.io/en/latest/install.html
import pyautogui

print(pyautogui.position())
# position (580, 237)

# position of browser address bar
pyautogui.click(580, 237)

# type text
pyautogui.typewrite("Hello World")

# click "enter"
pyautogui.typewrite(["enter"])

# hotkey to copy
pyautogui.hotkey("ctrl", "c")