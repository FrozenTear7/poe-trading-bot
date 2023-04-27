import re
import pyautogui
import pyperclip
from constants import CLIPBOARD_CURRENCY_REGEX

from utils.chat_utils import copy_text


if __name__ == '__main__':
    pyautogui.sleep(3)
    x, y = pyautogui.position()

    pyperclip.copy('')
    copy_text()
    clipboard_data = pyperclip.paste().replace('\r', '').replace('\n', ' - ').replace(',', '')

    currency_data = re.match(CLIPBOARD_CURRENCY_REGEX, clipboard_data)

    CURRENCY_TAB = {
        currency_data.group(1): {
            'exchangeName': 'wisdom',
            'buyLimit': 3000,
            'sell': {
                'active': False,
                'tabName': 'C',
                'subTabName': 'General',
                'x': round(x / 2560, 3),
                'y': round(y / 1440, 3)
            },
            'buy': {
                'active': False,
                'tabName': 'T1',
                'x': f'generic_trade_tab_x(1)',
                'y': f'generic_trade_tab_y(1)'
            },
            'stackSize': int(currency_data.group(3))
        }
    }

    print(CURRENCY_TAB)
