import pyautogui
import pyperclip
from constants import CURRENCY_TAB, MOVETO_DURATION, STASH_TABS, SUB_TABS, PYAUTOGUI_SPEED, TAKE_ITEM_SPEED
from stash.place_item import place_item
from utils.click_stash import click_stash
from utils.stash_state import get_stash_state_currency
from stash.reset_tabs import reset_tabs

width = 12
height = 5


def switch_tab(currency_config):
    for _ in range(STASH_TABS.index(currency_config['tabName'])):
        pyautogui.hotkey('CTRL', 'RIGHT')

    pyautogui.moveTo(SUB_TABS[currency_config['tabName']][currency_config['subTabName']]
                     ['x'], SUB_TABS[currency_config['tabName']][currency_config['subTabName']]
                     ['y'], MOVETO_DURATION)
    pyautogui.click()


def take_currency(name, amount):
    currency_config = CURRENCY_TAB[name]
    stash_state = get_stash_state_currency(name)

    taken = 0
    slots_taken = 0

    click_stash()
    reset_tabs()
    switch_tab(currency_config)

    # Extra Validation if target currency have only 1 left
    if amount == 1 and stash_state['amount'] == 1:
        pyautogui.moveTo(currency_config['sell']['x'], currency_config['sell']['y'], MOVETO_DURATION)
        pyautogui.keyDown('CTRL')
        pyautogui.click()
        pyautogui.keyUp('CTRL')
        slots_taken += 1

    # Original Logic
    else:
        while taken < amount:

            pyautogui.PAUSE = TAKE_ITEM_SPEED

            if (amount - taken) >= currency_config['stackSize'] or (amount == stash_state['amount'] and amount - taken == 1):
                pyautogui.moveTo(currency_config['sell']['x'], currency_config['sell']['y'], MOVETO_DURATION)
                pyautogui.keyDown('CTRL')
                pyautogui.click()
                pyautogui.keyUp('CTRL')

                taken += currency_config['stackSize']
            else:
                # Open amount selection
                pyautogui.moveTo(currency_config['sell']['x'], currency_config['sell']['y'], MOVETO_DURATION)
                pyautogui.keyDown('SHIFT')
                pyautogui.click()
                pyautogui.keyUp('SHIFT')

                # Move the slider
                for _ in range(amount - taken - 1):
                    pyautogui.press('RIGHT')
                pyautogui.press('ENTER')

                place_item(slots_taken)

                taken += (amount - taken)

            slots_taken += 1

        pyautogui.PAUSE = PYAUTOGUI_SPEED

    pyautogui.press('ESC')
