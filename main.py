from listener.LogListener import LogListener
from update_stash_state import update_stash_state
from utils.chat_utils import clear_ignore_list
from utils.prefix_print import printtime

if __name__ == '__main__':
    printtime("Configuring Bot...")
    update_stash_state() # Make sure to browse over the tabs before starting the bot, or the timer would be off.
    clear_ignore_list()
    log_listener = LogListener()
    try:
        printtime("Listening Log...")
        log_listener.listen()
    except KeyboardInterrupt:
        printtime("Stopping the bot...")