import pyautogui
from constants import ACCEPT_BUTTON, MOVETO_DURATION


def accept_trade():
    pyautogui.moveTo(ACCEPT_BUTTON['x'], ACCEPT_BUTTON['y'], MOVETO_DURATION)
    pyautogui.click()
