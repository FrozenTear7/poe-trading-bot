import pyautogui
import math
from constants import CURRENCY_TAB, WIDTH, HEIGHT, TRADE_WINDOW, PYAUTOGUI_SPEED, TRADE_VERIFY_RETRIES
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


def trade_currency_for_currency(trade_order, n=0):
    if n == 2:
        return
    sell_currency_config = CURRENCY_TAB[trade_order.sell_currency]
    sell_cells = math.ceil(trade_order.sell_amount / sell_currency_config['stackSize'])
    trade_user(trade_order.buyer)
    trade_started = wait_for_window()
    if trade_started:
        # Double Checking the tradeWindow to prevent errors
        if pyautogui.locate('images/tradeWindow.png', pyautogui.screenshot(region=(296, 496, 664, 362))):
            empty_equipment(sell_cells)
            reset_cursor()

            TRADE_VERIFIED_TIMES = 0  # Have Problem Moving this into constants.py

            try:
                while TRADE_VERIFIED_TIMES < TRADE_VERIFY_RETRIES:
                    pyautogui.PAUSE = 0.001

                    total_amount = 0
                    BROWSE_ITEM = True
                    VERIFY_ITEM = False

                    time.sleep(5)

                    if TRADE_VERIFIED_TIMES > 1:
                        if pyautogui.locate('images/acceptTradeItems.png', pyautogui.screenshot(region=(486, 824, 282, 25))):
                            BROWSE_ITEM = True
                        else:
                            BROWSE_ITEM = False

                    while BROWSE_ITEM:
                        if pyautogui.locate('images/acceptTradeItems.png', pyautogui.screenshot(region=(486, 824, 282, 25))):
                            for col in range(WIDTH):
                                for row in range(HEIGHT):
                                    pyautogui.moveTo(TRADE_WINDOW['start']['x']+col*TRADE_WINDOW['cellSize'],
                                                     TRADE_WINDOW['start']['y']+row*TRADE_WINDOW['cellSize'])
                            VERIFY_ITEM = True
                        elif not pyautogui.locate('images/acceptTradeItems.png', pyautogui.screenshot(region=(486, 824, 282, 25))):
                            BROWSE_ITEM = False

                    if VERIFY_ITEM:
                        for col in range(WIDTH):
                            for row in range(HEIGHT):
                                try:
                                    pyautogui.moveTo(TRADE_WINDOW['start']['x']+col*TRADE_WINDOW['cellSize'],
                                                     TRADE_WINDOW['start']['y']+row*TRADE_WINDOW['cellSize'])
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

                                    if total_amount == trade_order.buy_amount:
                                        break
                                # Catching: Empty Slot Have no .group()
                                except Exception as e:
                                    pass

                            if total_amount == trade_order.buy_amount:
                                break
                    if total_amount == trade_order.buy_amount:
                        break

                    TRADE_VERIFIED_TIMES += 1

                if TRADE_VERIFIED_TIMES == TRADE_VERIFY_RETRIES:
                    printtime(f"Trading with {trade_order.buyer} failed...")
                    pyautogui.press('ESC')
                    return

            except Exception as e:
                printtime(f"Trading Error: {e}...")
                pyautogui.press('ESC')
                pyautogui.PAUSE = PYAUTOGUI_SPEED  # set back to default stable value
                return

            pyautogui.PAUSE = PYAUTOGUI_SPEED  # set back to default value
            trade_order.update_buy_amount(total_amount)
            accept_trade()
    else:
        printtime("Trade didn't accpet.. retry in 5 seconds")
        pyautogui.sleep(5)
        trade_currency_for_currency(trade_order, n + 1)
