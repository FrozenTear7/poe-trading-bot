from listener.LogListener import LogListener
from update_stash_state import update_stash_state
from utils.chat_utils import clear_ignore_list


if __name__ == '__main__':
    update_stash_state()
    clear_ignore_list()

    log_listener = LogListener()
    try:
        log_listener.listen()
    except KeyboardInterrupt:
        print('Stopping the bot')
