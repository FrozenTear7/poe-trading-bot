from math import floor
import pyautogui
from constants import CELL_SIZE, EQUIPMENT, HEIGHT, MOVETO_DURATION


def place_item(slots_taken):
    pyautogui.moveTo(EQUIPMENT['start']['x'] + (floor(slots_taken / HEIGHT) * CELL_SIZE),
                     EQUIPMENT['start']['y'] + ((slots_taken % HEIGHT) * CELL_SIZE), MOVETO_DURATION)
    pyautogui.click()
