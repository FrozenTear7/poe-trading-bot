from constants import TRADE_WINDOW
from utils.translate_coordinates import translate_coordinates_horizontal, translate_coordinates_vertical


def item_within_window(x, y, width, height):
    return x >= translate_coordinates_horizontal(TRADE_WINDOW[0]) and x + width <= translate_coordinates_horizontal(TRADE_WINDOW[2]) \
        and y >= translate_coordinates_vertical(TRADE_WINDOW[1]) and y + height <= translate_coordinates_vertical(TRADE_WINDOW[3])
