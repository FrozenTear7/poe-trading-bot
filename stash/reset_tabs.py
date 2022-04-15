import pyautogui


def reset_tabs():
    pyautogui.keyDown('CTRL')
    for _ in range(15):
        pyautogui.hotkey('CTRL', 'LEFT')
    pyautogui.keyUp('CTRL')
