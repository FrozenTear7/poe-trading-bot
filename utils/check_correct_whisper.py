from constants import CURRENCY_TAB, HEIGHT, WIDTH
from utils.stash_state import get_stash_state_currency


def check_correct_whisper(trade_order):
    stash_state_currency = get_stash_state_currency(
        trade_order.buy_currency) if trade_order.sell_currency == 'Chaos Orb' else get_stash_state_currency(trade_order.sell_currency)
    stash_state_sell_currency = get_stash_state_currency(trade_order.sell_currency)
    stash_state_buy_currency = get_stash_state_currency(trade_order.buy_currency)

    return ((trade_order.sell_currency == 'Chaos Orb'
            and trade_order.sell_amount % stash_state_currency['price']['buy']['chaos'] == 0
            and trade_order.buy_amount % stash_state_currency['price']['buy']['self'] == 0
            and trade_order.buy_amount + stash_state_buy_currency['amount'] <= CURRENCY_TAB[trade_order.buy_currency]['buyLimit'])
            or (trade_order.buy_currency == 'Chaos Orb'
            and trade_order.buy_amount % stash_state_currency['price']['sell']['chaos'] == 0
            and trade_order.sell_amount % stash_state_currency['price']['sell']['self'] == 0)) \
        and trade_order.sell_amount <= stash_state_sell_currency['amount'] \
        and trade_order.sell_amount <= HEIGHT * WIDTH * CURRENCY_TAB[trade_order.sell_currency]['stackSize'] \
        and trade_order.buy_amount <= HEIGHT * WIDTH * CURRENCY_TAB[trade_order.buy_currency]['stackSize']
