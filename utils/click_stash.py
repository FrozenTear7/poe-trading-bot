import pyautogui

from constants import MOVETO_DURATION, STASH_COORDINATES


def click_stash():
    pyautogui.moveTo(STASH_COORDINATES[0], STASH_COORDINATES[1], MOVETO_DURATION)
    pyautogui.click()
