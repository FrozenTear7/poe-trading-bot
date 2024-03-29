import math
import pyautogui
from trade.TradeException import TradeException
from trade.trade_waits import wait_for_user_items
from utils.resetCursor import reset_cursor
from constants import CELL_SIZE, HEIGHT, TRADE_WINDOW


def move_cursor_to_cell(cell_index):
    height_index = cell_index % HEIGHT
    width_index = math.floor(cell_index / HEIGHT)

    if width_index == 0:
        offset_x = 0
    else:
        offset_x = 0
        for i in range(width_index):
            offset_x += TRADE_WINDOW[CELL_SIZE], i

    if height_index == 0:
        offset_y = 0
    else:
        offset_y = 0
        for i in range(height_index):
            offset_y += TRADE_WINDOW[CELL_SIZE], i

    if not wait_for_user_items():
        raise TradeException()

    if cell_index % 5 == 0:
        reset_cursor()
    pyautogui.moveTo(TRADE_WINDOW['start']['x'] + offset_x, TRADE_WINDOW['start']['y'] + offset_y)
