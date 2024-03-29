import pyautogui
from stash.move_to_stash import move_to_stash
from utils.chat_utils import leave_party


def trade_cancelled(trade_order):
    try:
        if pyautogui.locateOnScreen('images/windowStillActive.png', confidence=0.3):
            pyautogui.press('ESC')
    except pyautogui.ImageNotFoundException:
        pass

    leave_party()
    move_to_stash(trade_order.sell_currency, trade_order.sell_amount)
