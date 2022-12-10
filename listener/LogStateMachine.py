from listener.log_listener_events import CURSOR_CLEAN, CURSOR_CURRENCY, MESSAGE_RECEIVED, PLAYER_DID_NOT_JOIN, PLAYER_DID_NOT_JOIN_RETRY, PLAYER_JOINED_AREA, TRADE_ACCEPTED, TRADE_CANCELLED
from listener.log_states import CLEANUP, IN_TRADE, READY, WAITING_FOR_PLAYER
from stash.move_to_stash import move_to_stash
from stash.take_item import take_currency
from trade.TradeOrder import TradeOrder
from trade.trade_accepted import trade_accepted
from trade.trade_currency_for_currency import trade_currency_for_currency
from utils.chat_utils import ignore_player, invite_user, kick_user


class LogStateMachine:
    def __init__(self):
        self.state = READY

    def on_event(self, action, payload):
        if self.state == READY:
            if action == MESSAGE_RECEIVED:
                self.trade_order = payload
                invite_user(self.trade_order.buyer)
                self.state = WAITING_FOR_PLAYER
        elif self.state == WAITING_FOR_PLAYER:
            if action == PLAYER_DID_NOT_JOIN:
                kick_user(self.trade_order.buyer)
                invite_user(self.trade_order.buyer)
            if action == PLAYER_DID_NOT_JOIN_RETRY:
                ignore_player(self.trade_order.buyer)
                kick_user(self.trade_order.buyer)
                self.state = READY
            elif action == PLAYER_JOINED_AREA:
                take_currency(self.trade_order.sell_currency, self.trade_order.sell_amount)
                trade_currency_for_currency(self.trade_order)
                self.state = IN_TRADE
        elif self.state == IN_TRADE:
            if action == TRADE_ACCEPTED:
                trade_accepted(self.trade_order)
                self.state = READY
            elif action == TRADE_CANCELLED:
                kick_user(self.trade_order.buyer)
                move_to_stash(self.trade_order.sell_currency, self.trade_order.sell_amount)
                ignore_player(self.trade_order.buyer)
                self.state = READY
        elif self.state == CLEANUP:
            if action == CURSOR_CLEAN:
                self.state = READY
            if action == CURSOR_CURRENCY:
                self.state = READY
