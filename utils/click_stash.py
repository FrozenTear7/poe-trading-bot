import pyautogui

from constants import MOVETO_DURATION, STASH_COORDINATES
from utils.translate_coordinates import translate_coordinates_horizontal, translate_coordinates_vertical


def click_stash():
    pyautogui.moveTo(translate_coordinates_horizontal(
        STASH_COORDINATES[0]), translate_coordinates_vertical(STASH_COORDINATES[1]), MOVETO_DURATION)
    pyautogui.click()
