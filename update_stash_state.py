import pyautogui
import pyperclip
import re
from constants import CLIPBOARD_CURRENCY_REGEX, CURRENCY_TAB, MOVETO_DURATION, STASH_TABS, SUB_TABS
from stash.reset_tabs import reset_tabs
from stash.scroll_tabs import scroll_tabs
from stash.set_price import set_price
from utils.chat_utils import copy_text
from utils.click_stash import click_stash
from utils.prefix_print import printtime
from utils.stash_state import update_stash_amount
from utils.translate_coordinates import translate_coordinates_horizontal, translate_coordinates_vertical


def update_sell_price(currency_name, currency_config, price_calculator):
    printtime(f'Resetting tabs')
    reset_tabs()

    printtime(f'Scrolling to sell tab: {currency_config["sell"]["tabName"]}')
    scroll_tabs(STASH_TABS.index(currency_config['sell']['tabName']))

    if currency_config['sell']['subTabName']:
        sub_tab_coordinates = SUB_TABS[currency_config['sell']['tabName']][currency_config['sell']['subTabName']]
        sub_tab_button_coords = (translate_coordinates_horizontal(
            sub_tab_coordinates['x']), translate_coordinates_vertical(sub_tab_coordinates['y']))

        printtime(f'Moving cursor to subTab: ({sub_tab_button_coords[0]}, {sub_tab_button_coords[1]})')
        pyautogui.moveTo(sub_tab_button_coords[0], sub_tab_button_coords[1], MOVETO_DURATION)
        pyautogui.click()

    tab_location_coords = (translate_coordinates_horizontal(currency_config['sell']['x']), translate_coordinates_vertical(
        currency_config['sell']['y']))

    printtime(f'Moving cursor to currency position: ({tab_location_coords[0]}, {tab_location_coords[1]})')
    pyautogui.moveTo(tab_location_coords[0], tab_location_coords[1], MOVETO_DURATION)

    copy_text()

    pyperclip.copy('')
    clipboard_data = pyperclip.paste().replace('\r', '').replace('\n', ' - ').replace(',', '')

    if clipboard_data == '':
        printtime(f'Currency missing from the stash, setting stash amount to: 0')
        update_stash_amount(currency_name, 0)
    else:
        currency_data = re.match(CLIPBOARD_CURRENCY_REGEX, clipboard_data)
        currency_amount = int(currency_data.group(2))

        printtime(f'Setting stash amount of currency to: {currency_amount}')
        update_stash_amount(currency_name, currency_amount)

        # The only currency we don't have to price is chaos orb
        if currency_config['sell']['active']:
            set_price(price_calculator.get_sell_price(currency_name))


def update_buy_price(currency_name, currency_config, price_calculator):
    if currency_config['buy']['active']:
        printtime(f'Resetting tabs')
        reset_tabs()

        printtime(f'Scrolling to buy tab: {currency_config["buy"]["tabName"]}')
        scroll_tabs(STASH_TABS.index(currency_config['buy']['tabName']))

        tab_location_coords = (currency_config['buy']['x'], currency_config['buy']['y'])

        printtime(f'Moving cursor to currency position: ({tab_location_coords[0]}, {tab_location_coords[1]})')
        pyautogui.moveTo(tab_location_coords[0], tab_location_coords[1])

        set_price(price_calculator.get_buy_price(currency_name, currency_config['exchangeName']))
    else:
        printtime(f'Buying is inactive for this currency')


def update_stash_state(price_calculator):
    pyautogui.sleep(3)
    printtime('Opening the stash')
    click_stash()

    # For each item the currency tab setup
    for currency_name in list(CURRENCY_TAB):
        currency_config = CURRENCY_TAB[currency_name]
        pyperclip.copy('')

        printtime(f'Fetching stash state for: {currency_name}')

        printtime(f'Setting sell price for currency: {currency_name}')
        update_sell_price(currency_name, currency_config, price_calculator)
        printtime(f'Finished setting sell price for: {currency_name}')

        printtime(f'Setting buy price for currency: {currency_name}')
        update_buy_price(currency_name, currency_config, price_calculator)
        printtime(f'Finished setting buy price for: {currency_name}')

    pyautogui.press('ESC')
