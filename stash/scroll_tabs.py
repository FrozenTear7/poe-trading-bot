import pyautogui


def scroll_tabs(tab_index):
    for _ in range(tab_index):
        pyautogui.press('RIGHT')
