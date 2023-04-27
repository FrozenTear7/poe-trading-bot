from stash.move_to_stash import move_to_stash
from utils.chat_utils import thank_user, leave_party
from utils.stash_state import update_stash_state


def trade_accepted(trade_order):
    thank_user(trade_order.buyer)
    leave_party()

    move_to_stash(trade_order.buy_currency, trade_order.buy_amount)
    update_stash_state(trade_order.sell_currency, trade_order.sell_amount,
                       trade_order.buy_currency, trade_order.buy_amount)
