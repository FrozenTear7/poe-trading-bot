from math import ceil, floor
import re
import pyautogui
from constants import AFK_REGEX, INCOMING_PLAYER_WHISPER_REGEX, LEAGUE_NAME, LOG_FILE, LOG_REGEX, PLAYER_JOINED_AREA_REGEX, SELL_CURRENCY_FOR_CURRENCY_REGEX, TRADE_ACCEPTED_REGEX, TRADE_CANCELLED_REGEX, WAIT_AGAIN_RETRIES, WAIT_RETRIES, CURRENCY_TAB
from listener.LogStateMachine import LogStateMachine
from listener.log_listener_events import CURRENCY_FOR_CURRENCY, MESSAGE_RECEIVED, PLAYER_DID_NOT_JOIN, PLAYER_DID_NOT_JOIN_RETRY, PLAYER_JOINED_AREA, TRADE_ACCEPTED, TRADE_CANCELLED
from listener.log_states import WAITING_FOR_PLAYER
from trade.TradeOrder import TradeOrder
from utils.chat_utils import afk_off, ignore_player
from utils.check_correct_whisper import check_correct_whisper
from utils.party_status import party_status
from utils.prefix_print import printtime
from utils.stash_state import get_stash_state


class LogListener():
    def __init__(self, price_calculator):
        self.log_file = open(LOG_FILE, 'r', encoding='utf8')
        # readlines() moves the file cursor to the end so we only see newly added chat messages
        self.log_file.readlines()
        self.log_state_machine = LogStateMachine()
        self.price_calculator = price_calculator

    def listen(self):
        reply_waits = 0
        reply_waits_retry = 0

        while True:
            pyautogui.sleep(1)
            printtime(f"Current state: {self.log_state_machine.state}")

            if self.log_state_machine.state == WAITING_FOR_PLAYER:
                printtime(
                    f'Waiting for trader: {current_trade.buyer}, waiting: {reply_waits}, wait_retries: {reply_waits_retry}')

                if reply_waits == WAIT_RETRIES:
                    if reply_waits_retry == 0:
                        if party_status():
                            printtime(
                                f'Trader: {current_trade.buyer} has not joined, kicking trader and waiting for their possible loading in outside of the party')
                            self.log_state_machine.on_event(PLAYER_DID_NOT_JOIN, current_trade)
                            reply_waits_retry += 1
                        else:
                            printtime(
                                f'Trader: {current_trade.buyer} ignored the party invite, return to READY state')
                            self.log_state_machine.on_event(PLAYER_DID_NOT_JOIN_RETRY, current_trade)
                            reply_waits = 0
                            reply_waits_retry = 0
                            self.log_file.readlines()
                    elif reply_waits_retry == WAIT_AGAIN_RETRIES:
                        printtime(
                            f'Trader: {current_trade.buyer} has not joined after both periods of waiting, return to READY state')
                        self.log_state_machine.on_event(PLAYER_DID_NOT_JOIN_RETRY, current_trade)
                        reply_waits = 0
                        reply_waits_retry = 0
                        self.log_file.readlines()
                    else:
                        reply_waits_retry += 1
                else:
                    reply_waits += 1

            for line in self.log_file.readlines():
                try:
                    log = re.match(LOG_REGEX, line).group(2)

                    if re.match(AFK_REGEX, log):
                        printtime('Waking the bot up from being afk')
                        afk_off()
                    elif re.match(INCOMING_PLAYER_WHISPER_REGEX, log):
                        printtime(f'Incoming offer: {log}')

                        sell_currency_for_currency_whisper = re.match(SELL_CURRENCY_FOR_CURRENCY_REGEX, log)
                        if sell_currency_for_currency_whisper.group(8) != LEAGUE_NAME:
                            printtime('Invalid league trade request')
                            continue

                        current_trade = TradeOrder(CURRENCY_FOR_CURRENCY,
                                                   sell_currency_for_currency_whisper.group(2),
                                                   sell_currency_for_currency_whisper.group(5),
                                                   sell_currency_for_currency_whisper.group(4),
                                                   sell_currency_for_currency_whisper.group(7),
                                                   sell_currency_for_currency_whisper.group(6)
                                                   )
                        stash_state = get_stash_state()

                        # FIXME: Split the offer into multiple trades
                        if current_trade.sell_amount / CURRENCY_TAB[current_trade.sell_currency]['stackSize'] > 60 or \
                                current_trade.buy_amount / CURRENCY_TAB[current_trade.buy_currency]['stackSize'] > 60:
                            printtime(f'Trade offer exceeds the inventory capacity')
                            continue
                        elif current_trade.sell_currency == 'Chaos Orb':
                            if CURRENCY_TAB[current_trade.buy_currency]['buyActive']:
                                offer_price_ratio = current_trade.sell_amount / current_trade.buy_amount
                                if self.price_calculator.verify_buy_price(offer_price_ratio, current_trade.buy_currency):
                                    pass
                                else:
                                    printtime(f'Message has been modified, ignoring player: {current_trade.buyer}')
                                    ignore_player(current_trade.buyer)
                                    continue
                            else:
                                printtime(f'Buying is currently inactive for this currency')
                                continue
                        elif current_trade.buy_currency == 'Chaos Orb':
                            if CURRENCY_TAB[current_trade.sell_currency]['sell']['active']:
                                offer_price_ratio = current_trade.buy_amount / current_trade.sell_amount
                                if self.price_calculator.verify_sell_price(offer_price_ratio, current_trade.sell_currency):
                                    pass
                                else:
                                    printtime(f'Message has been modified, ignoring player: {current_trade.buyer}')
                                    ignore_player(current_trade.buyer)
                                    continue
                            else:
                                printtime(f'Selling is currently inactive for this currency')
                                continue
                        elif current_trade.sell_currency != 'Chaos Orb' or current_trade.buy_currency != 'Chaos Orb':
                            printtime('Invalid trade offer')
                            continue
                        elif current_trade.sell_amount > stash_state[current_trade.sell_currency]['amount']:
                            printtime(f'Not enough currency: {current_trade.sell_currency} in stock')

                        if check_correct_whisper(current_trade, stash_state):
                            printtime(f'Sending party invitation to: {current_trade.buyer}')
                            self.log_state_machine.on_event(MESSAGE_RECEIVED, current_trade)
                    elif re.match(PLAYER_JOINED_AREA_REGEX, log):
                        printtime(log)

                        reply_waits = 0
                        reply_waits_retry = 0
                        player_joined_name = re.match(PLAYER_JOINED_AREA_REGEX, log).group(1)

                        if player_joined_name == self.log_state_machine.trade_order.buyer:
                            printtime(f'Correct trader: {player_joined_name} joined the area')
                            self.log_state_machine.on_event(PLAYER_JOINED_AREA, current_trade)
                    elif re.match(TRADE_ACCEPTED_REGEX, log):
                        printtime(f'Trade accepted, clearing the log file')
                        self.log_state_machine.on_event(TRADE_ACCEPTED, current_trade)
                        self.log_file.readlines()
                        break
                    elif re.match(TRADE_CANCELLED_REGEX, log):
                        printtime(f'Trade cancelled, clearing the log file')
                        self.log_state_machine.on_event(TRADE_CANCELLED, current_trade)
                        self.log_file.readlines()
                        break
                except Exception as e:
                    printtime(e)
                    pass

                pyautogui.sleep(1)
