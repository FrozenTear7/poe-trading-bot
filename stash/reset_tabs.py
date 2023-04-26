import pyautogui

from constants import AMOUNT_OF_STASH_TABS


def reset_tabs():
    for _ in range(AMOUNT_OF_STASH_TABS):
        pyautogui.press('LEFT')
