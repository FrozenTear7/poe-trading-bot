import pyautogui
import pyperclip
import re

from constants import CLIPBOARD_CURRENCY_REGEX


def get_cell_info_currency():
    pyautogui.keyDown('CTRL')
    pyautogui.press('C')
    pyautogui.keyUp('CTRL')

    clipboard_data = pyperclip.paste().replace('\r', '').replace('\n', ' - ')
    currency_data = re.match(CLIPBOARD_CURRENCY_REGEX, clipboard_data)

    currency_name = currency_data.group(1)
    currency_amount = int(currency_data.group(2))

    return (currency_name, currency_amount)
