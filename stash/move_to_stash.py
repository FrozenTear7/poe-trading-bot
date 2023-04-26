import math
import pyautogui
import time
from constants import CELL_SIZE, CURRENCY_TAB, EQUIPMENT, HEIGHT, MOVETO_DURATION, WIDTH
from stash.reset_tabs import reset_tabs
from stash.set_price import set_price
from utils.click_stash import click_stash
from utils.stash_state import get_stash_state_currency


def move_to_stash(name, amount):
    stash_state = get_stash_state_currency(name)
    cells = math.ceil(amount / CURRENCY_TAB[name]['stackSize'])

    currency_config = CURRENCY_TAB

    item_counter = 1

    click_stash()
    time.sleep(1)  # For stash loading time

    for i in range(WIDTH):
        for j in range(HEIGHT):
            pyautogui.moveTo(EQUIPMENT['start']['x'] + (i * EQUIPMENT[CELL_SIZE]),
                             EQUIPMENT['start']['y'] + (j * EQUIPMENT[CELL_SIZE]), MOVETO_DURATION)
            pyautogui.keyDown('CTRL')
            pyautogui.click()
            pyautogui.keyUp('CTRL')

            item_counter += 1
            if item_counter > cells:
                if name != 'Chaos Orb' and stash_state['amount'] == 0 and currency_config[name]['sellActive']:
                    pyautogui.moveTo(currency_config[name]['sell']['x'],
                                     currency_config[name]['sell']['y'], MOVETO_DURATION)
                    set_price(stash_state)

                reset_tabs()
                pyautogui.press('ESC')
                return

    pyautogui.press('ESC')
