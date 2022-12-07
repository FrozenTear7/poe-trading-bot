import pyautogui
import pyperclip
import re
from constants import CLIPBOARD_CURRENCY_REGEX, CURRENCY_TAB, MOVETO_DURATION, STASH_TABS, SUB_TABS
from stash.reset_tabs import reset_tabs
from stash.set_price import set_chaos_price, set_price
from utils.click_stash import click_stash
from utils.stash_state import get_stash_state_currency, update_stash_amount


def set_sell_price(current_currency_name, currency_config, stash_state_currency):
    reset_tabs()
    if currency_config['sellActive']:
        if currency_config['tabName']:
            for _ in range(STASH_TABS.index(currency_config['tabName'])):
                pyautogui.hotkey('CTRL', 'RIGHT')

        sub_tab_coordinates = SUB_TABS[currency_config['tabName']][currency_config['subTabName']]

        pyautogui.moveTo(sub_tab_coordinates['x'], sub_tab_coordinates['y'], MOVETO_DURATION)
        pyautogui.click()
        pyautogui.moveTo(currency_config['sell']['x'],
                         currency_config['sell']['y'])

        pyautogui.keyDown('CTRL')
        pyautogui.press('C')
        pyautogui.keyUp('CTRL')

        clipboard_data = pyperclip.paste().replace('\r', '').replace('\n', ' - ').replace(',', '')

        if clipboard_data == '':
            update_stash_amount(current_currency_name, 0)
        else:
            currency_data = re.match(CLIPBOARD_CURRENCY_REGEX, clipboard_data)
            price_already_set = 'Note: ~price' in clipboard_data

            currency_amount = int(currency_data.group(2))

            update_stash_amount(current_currency_name, currency_amount)
            set_price(stash_state_currency, price_already_set)

    # Exception for Chaos Orb, duplicated lines due to laziness Kapp
    if current_currency_name == "Chaos Orb":
        sub_tab_coordinates = SUB_TABS[currency_config['tabName']][currency_config['subTabName']]
        pyautogui.moveTo(sub_tab_coordinates['x'], sub_tab_coordinates['y'], MOVETO_DURATION)
        pyautogui.click()
        pyautogui.moveTo(currency_config['sell']['x'],
                         currency_config['sell']['y'])
        pyautogui.keyDown('CTRL')
        pyautogui.press('C')
        pyautogui.keyUp('CTRL')
        clipboard_data = pyperclip.paste().replace('\r', '').replace('\n', ' - ').replace(',', '')
        currency_data = re.match(CLIPBOARD_CURRENCY_REGEX, clipboard_data)
        price_already_set = 'Note: ~price' in clipboard_data
        currency_amount = int(currency_data.group(2))
        update_stash_amount(current_currency_name, currency_amount)


def set_buy_price(current_currency_name, stash_state_currency):
    reset_tabs()
    pyautogui.hotkey('CTRL', 'RIGHT')
    if CURRENCY_TAB[current_currency_name]['buyActive']:
        pyautogui.moveTo(CURRENCY_TAB[current_currency_name]['buy']['x'],
                         CURRENCY_TAB[current_currency_name]['buy']['y'])
        set_chaos_price(stash_state_currency, CURRENCY_TAB[current_currency_name]['exchangeName'], True)


def update_stash_state():
    pyautogui.sleep(3)
    click_stash()

    for current_currency_name in list(CURRENCY_TAB):
        currency_config = CURRENCY_TAB[current_currency_name]
        pyperclip.copy('')
        stash_state_currency = get_stash_state_currency(current_currency_name)

        set_sell_price(current_currency_name, currency_config, stash_state_currency)
        set_buy_price(current_currency_name, stash_state_currency)

    pyautogui.press('ESC')
