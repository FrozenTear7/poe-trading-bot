import pyautogui
from constants import STASH_TAB_PRICING_MENU_THRESHOLD, STASH_TAB_PRICING_MENU_SELECT_ABOVE_THRESHOLD, STASH_TAB_PRICING_MENU_SELECT_UNDER_THRESHOLD

from utils.prefix_print import printtime
from utils.translate_coordinates import translate_coordinates_horizontal, translate_coordinates_vertical


def set_price(price):
    printtime(f'Setting price: {price}')
    pyautogui.click(button='right')

    x, _ = pyautogui.position()
    if x > translate_coordinates_horizontal(STASH_TAB_PRICING_MENU_THRESHOLD):
        pyautogui.moveRel(translate_coordinates_horizontal(STASH_TAB_PRICING_MENU_SELECT_ABOVE_THRESHOLD[0]),
                          translate_coordinates_vertical(STASH_TAB_PRICING_MENU_SELECT_ABOVE_THRESHOLD[1]))
    else:
        pyautogui.moveRel(translate_coordinates_horizontal(STASH_TAB_PRICING_MENU_SELECT_UNDER_THRESHOLD[0]),
                          translate_coordinates_vertical(STASH_TAB_PRICING_MENU_SELECT_UNDER_THRESHOLD[1]))
    pyautogui.click()

    # Select the note option
    pyautogui.press('UP')
    pyautogui.press('UP')
    pyautogui.press('ENTER')

    pyautogui.hotkey('CTRL', 'A')
    pyautogui.typewrite(price)
    pyautogui.press('ENTER')
