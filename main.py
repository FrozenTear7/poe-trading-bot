from listener.LogListener import LogListener
from update_stash_state import update_stash_state
from utils.PriceCalculator import PriceCalculator
from utils.chat_utils import clear_ignore_list
from utils.prefix_print import printtime
from constants import PYAUTOGUI_SPEED
import pyautogui
import pytesseract

from utils.translate_coordinates import translate_coordinates_horizontal, translate_coordinates_vertical

pyautogui.PAUSE = PYAUTOGUI_SPEED

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'

    printtime('Configuring the bot')

    printtime('Setting up the price calculator')
    price_calculator = PriceCalculator()

    printtime('Updating the stash state')
    # update_stash_state(price_calculator)
    printtime('Finished updating the stash state')

    printtime('Clearing the ignore list')
    clear_ignore_list()

    log_listener = LogListener(price_calculator)
    try:
        printtime("Listening to incoming trade offers")
        log_listener.listen()
    except KeyboardInterrupt:
        printtime("Stopping the bot")
