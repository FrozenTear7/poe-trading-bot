import pyautogui


def reset_cursor():
    pyautogui.moveRel(-pyautogui.position().x + 1, 1)
    pyautogui.moveRel(1, -pyautogui.position().y + 1)
