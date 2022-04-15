import pyautogui
import math
from constants import EQUIPMENT, HEIGHT, MOVETO_DURATION


def place_item(slots_taken):
    pyautogui.moveTo(EQUIPMENT['start']['x'] + (math.floor(slots_taken / HEIGHT) * EQUIPMENT['cellSize']),
                     EQUIPMENT['start']['y'] + ((slots_taken % HEIGHT) * EQUIPMENT['cellSize']), MOVETO_DURATION)
    pyautogui.click()
