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


# 1. Trade user
# 2. Check if waiting popup exists
# 3. If popup disappears check if trade window exists
# 4. If trade window exists proceed
# 5. If user cancells kick and shit
# 6. If trade window did not appear sleep for 5s and retry
# 7. If still nothing happens kick the user

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

        try:
            total_amount = 0
            cell_index = 0
            while total_amount < trade_order.buy_amount:
                move_cursor_to_cell(cell_index)
                cell_currency, cell_amount = get_cell_info_currency()

                if cell_currency != trade_order.buy_currency:
                    raise TradeException('Wrong currency')

                total_amount += cell_amount
                cell_index += 1
        except Exception as e:
            print(e)
            pyautogui.press('ESC')
            return

        trade_order.update_buy_amount(total_amount)
        accept_trade()
    else:
        pyautogui.sleep(5)
        trade_currency_for_currency(trade_order, n + 1)
