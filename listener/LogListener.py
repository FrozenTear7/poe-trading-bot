import re
import pyautogui
from constants import AFK_REGEX, INCOMING_PLAYER_WHISPER_REGEX, LOG_FILE, LOG_REGEX, PLAYER_JOINED_AREA_REGEX, SELL_CURRENCY_FOR_CURRENCY_REGEX, TRADE_ACCEPTED_REGEX, TRADE_CANCELLED_REGEX, WAIT_AGAIN_RETRIES, WAIT_RETRIES
from listener.LogStateMachine import LogStateMachine
from listener.log_listener_events import CURRENCY_FOR_CURRENCY, MESSAGE_RECEIVED, PLAYER_DID_NOT_JOIN, PLAYER_DID_NOT_JOIN_RETRY, PLAYER_JOINED_AREA, TRADE_ACCEPTED, TRADE_CANCELLED
from listener.log_states import WAITING_FOR_PLAYER
from trade.TradeOrder import TradeOrder
from utils.alt_name_fix import alt_name_fix
from utils.chat_utils import afk_off, ignore_player
from utils.check_correct_whisper import check_correct_whisper
from utils.party_status import party_status
import datetime
import json
from utils.prefix_print import printtime


class LogListener():
    def __init__(self):
        self.log_file = open(LOG_FILE, 'r', encoding='utf8')
        # First read so we can start listening for new changes in listen()
        self.log_file.readlines()
        self.log_state_machine = LogStateMachine()

    def listen(self):
        reply_waits = 0
        reply_waits_retry = 0

        while True:
            pyautogui.sleep(1)
            printtime(f"Current State: {self.log_state_machine.state}")
            if self.log_state_machine.state == WAITING_FOR_PLAYER:
                if reply_waits == WAIT_RETRIES:
                    if reply_waits_retry == 0:
                        if party_status():
                            self.log_state_machine.on_event(PLAYER_DID_NOT_JOIN,current_trade) #added args: payload
                            reply_waits_retry += 1
                        else:
                            self.log_state_machine.on_event(PLAYER_DID_NOT_JOIN_RETRY,current_trade) #added args: payload
                            self.log_file.readlines()
                            reply_waits = 0
                            reply_waits_retry = 0
                    if reply_waits_retry == WAIT_AGAIN_RETRIES:
                        self.log_state_machine.on_event(PLAYER_DID_NOT_JOIN_RETRY,current_trade) #added args: payload
                        self.log_file.readlines()
                        reply_waits = 0
                        reply_waits_retry = 0
                    else:
                        reply_waits_retry += 1
                else:
                    reply_waits += 1

            for line in self.log_file.readlines():
                try:
                    log = re.match(LOG_REGEX, line).group(2)
                    if re.match(AFK_REGEX, log):
                        afk_off()

                    elif re.match(INCOMING_PLAYER_WHISPER_REGEX, log):
                        printtime(re.match(SELL_CURRENCY_FOR_CURRENCY_REGEX, log).group(0))
                        sell_currency_for_currency_whisper = re.match(SELL_CURRENCY_FOR_CURRENCY_REGEX, log)
                        current_trade = TradeOrder(CURRENCY_FOR_CURRENCY,                                      # type
                                                   sell_currency_for_currency_whisper.group(2),                # buyer
                                                   alt_name_fix(sell_currency_for_currency_whisper.group(5)),  # sell_currency
                                                   sell_currency_for_currency_whisper.group(4),                # sell_amount
                                                   alt_name_fix(sell_currency_for_currency_whisper.group(7)),  # buy_currency
                                                   sell_currency_for_currency_whisper.group(6)                 # buy_amount
                                                   )
                        config_file = open('stash_state.json', 'r')
                        stash_state = json.loads(config_file.read())
                        if current_trade.sell_currency == "Chaos Orb": #Buying currency with chaos
                            target = stash_state[current_trade.buy_currency]
                            if current_trade.sell_amount/current_trade.buy_amount == target['price']['buy']['chaos']:
                                pass
                            else:
                                printtime("Offer modified!! Ignoring the Player")
                                ignore_player(current_trade.buyer)
                                continue
                        elif current_trade.buy_currency == "Chaos Orb": #Selling currency for chaos
                            target = (stash_state[current_trade.sell_currency])
                            if target['price']['sell']['chaos'] == current_trade.buy_amount/current_trade.sell_amount:
                                pass
                            else:
                                printtime("Offer modified!! Ignoring the Player")
                                ignore_player(current_trade.buyer)
                                continue
                        
                        self.log_state_machine.on_event(MESSAGE_RECEIVED, current_trade)
                        # if check_correct_whisper(current_trade):
                        #     self.log_state_machine.on_event(MESSAGE_RECEIVED, current_trade)
                    elif re.match(PLAYER_JOINED_AREA_REGEX, log):
                        printtime(re.match(PLAYER_JOINED_AREA_REGEX, log).group(0))
                        reply_waits = 0
                        reply_waits_retry = 0
                        player_joined_name = re.match(PLAYER_JOINED_AREA_REGEX, log).group(1)
                        if player_joined_name == self.log_state_machine.trade_order.buyer: # Correct player joined
                            self.log_state_machine.on_event(PLAYER_JOINED_AREA,current_trade)
                    elif re.match(TRADE_ACCEPTED_REGEX, log):
                        self.log_state_machine.on_event(TRADE_ACCEPTED,current_trade)
                        self.log_file.readlines()
                        break
                    elif re.match(TRADE_CANCELLED_REGEX, log):
                        self.log_state_machine.on_event(TRADE_CANCELLED,current_trade)
                        self.log_file.readlines()
                        break
                except Exception as e:
                    printtime(f"Log Listener ERROR: {e}")
                    pass

                pyautogui.sleep(1)
