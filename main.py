from listener.LogListener import LogListener
from update_stash_state import update_stash_state
from utils.chat_utils import clear_ignore_list
from utils.prefix_print import printtime
from constants import PYAUTOGUI_SPEED
import pyautogui

pyautogui.PAUSE = PYAUTOGUI_SPEED  # CAUTION!! Need more testing

# Make sure to browse over the tabs before starting the bot, or the timer would be off.
if __name__ == '__main__':
    printtime("Configuring Bot...")
    update_stash_state()
    exit()
    clear_ignore_list()
    log_listener = LogListener()
    try:
        printtime("Listening Log...")
        log_listener.listen()
    except KeyboardInterrupt:
        printtime("Stopping the bot...")
