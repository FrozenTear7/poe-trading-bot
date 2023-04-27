from constants import CURRENCY_TAB, HEIGHT, WIDTH


def check_correct_whisper(trade_order, stash_state):
    stash_state_sell_currency = stash_state[trade_order.sell_currency]
    stash_state_buy_currency = stash_state[trade_order.buy_currency]

    return ((trade_order.sell_currency == 'Chaos Orb' and trade_order.buy_amount + stash_state_buy_currency <= CURRENCY_TAB[trade_order.buy_currency]['buyLimit']) or trade_order.buy_currency == 'Chaos Orb') \
        and trade_order.sell_amount <= stash_state_sell_currency \
        and trade_order.sell_amount <= HEIGHT * WIDTH * CURRENCY_TAB[trade_order.sell_currency]['stackSize'] \
        and trade_order.buy_amount <= HEIGHT * WIDTH * CURRENCY_TAB[trade_order.buy_currency]['stackSize']
