import pyautogui
import math
from constants import CURRENCY_TAB
from stash.empty_equipment import empty_equipment
from trade.TradeException import TradeException
from trade.accept_trade import accept_trade
from trade.get_cell_info import get_cell_info_currency
from trade.move_cursor_to_cell import move_cursor_to_cell
from trade.trade_waits import wait_for_window
from utils.chat_utils import trade_user
from utils.resetCursor import reset_cursor
from utils.prefix_print import printtime
import pyperclip
import re
import time

cell_size=54

def trade_currency_for_currency(trade_order, n=0):
    if n == 2:
        return
    sell_currency_config = CURRENCY_TAB[trade_order.sell_currency]
    sell_cells = math.ceil(trade_order.sell_amount / sell_currency_config['stackSize'])
    trade_user(trade_order.buyer)
    trade_started = wait_for_window()
    if trade_started:
        empty_equipment(sell_cells)
        reset_cursor()
        
        check_times=0
        if check_times<3:
            try:
                total_amount = 0
                while total_amount < trade_order.buy_amount:
                    pyautogui.PAUSE=0.001
                    while True:
                        time.sleep(5)
                        if pyautogui.locate('images/acceptTradeItems.png', pyautogui.screenshot(region=(486, 824, 282, 25))): # player start putting stuff
                            for col in range(12):
                                for row in range(5):
                                    pyautogui.moveTo(312+col*cell_size,204+row*cell_size)
                        elif not pyautogui.locate('images/acceptTradeItems.png', pyautogui.screenshot(region=(486, 824, 282, 25))):
                            break
                    for col in range(12):
                        for row in range(5):
                            try:
                                pyautogui.moveTo(312+col*cell_size,204+row*cell_size)
                                pyautogui.keyDown('CTRL')
                                pyautogui.press('C')
                                pyautogui.keyUp('CTRL')
                                clipboard_data = pyperclip.paste().replace('\r', '').replace('\n', ' - ')
                                currency_data = re.match('.+Rarity: \w+ - (.+) - -+ - Stack Size: (\d+).+', clipboard_data)
                                cell_currency = currency_data.group(1)
                                cell_amount = int(currency_data.group(2))
                                pyperclip.copy('')
                                if cell_currency != trade_order.buy_currency:
                                    raise TradeException('Wrong currency')
                                total_amount += cell_amount
                            except Exception as e:
                                pass
            except Exception as e:
                printtime(e)
                pyautogui.press('ESC')
                pyautogui.PAUSE=0.1
                return
        else:
            print("check times:",check_times)
            pyautogui.PAUSE=0.1
            return

        pyautogui.PAUSE=0.1
        trade_order.update_buy_amount(total_amount)
        accept_trade()
    else:
        printtime("Trade didn't accpet.. retry in 5 seconds")
        pyautogui.sleep(5)
        trade_currency_for_currency(trade_order, n + 1)