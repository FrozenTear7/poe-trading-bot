from constants import TRADE_WINDOW_END_LEFT, TRADE_WINDOW_END_TOP, TRADE_WINDOW_START_LEFT, TRADE_WINDOW_START_TOP


def item_within_window(x, y, width, height):
    return x >= TRADE_WINDOW_START_LEFT and x + width <= TRADE_WINDOW_END_LEFT \
        and y >= TRADE_WINDOW_START_TOP and y + height <= TRADE_WINDOW_END_TOP
