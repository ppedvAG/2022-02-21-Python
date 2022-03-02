import pyautogui


# print(pyautogui.size())
print(pyautogui.position())
# (x=364, y=301)
# (x=1363, y=307)
# (x=1374, y=929)
# (x=362, y=928)
pyautogui.moveTo(-1897, 852, duration=1)
pyautogui.click()
windows = pyautogui.getAllWindows()
for window in windows:
    print(window.title)
print(pyautogui.getActiveWindowTitle())
np = pyautogui.screenshot(region=(364, 301, 1000, 600))
(pyautogui.locateOnScreen(np))

pyautogui.hotkey("windows", "x")
pyautogui.hotkey("a")
