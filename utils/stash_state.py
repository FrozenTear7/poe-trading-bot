import json

from constants import CURRENCY_TAB

config_file_name = 'stash_state.json'


def get_stash_state():
    config_file = open(config_file_name, 'r')
    return json.loads(config_file.read())


def get_stash_state_currency(currency):
    try:
        config_file = open(config_file_name, 'r')
        stash_state = json.loads(config_file.read())
        return stash_state[currency]
    except FileNotFoundError:
        print('Please provide a valid stash_state file')
        exit(1)


def update_stash_state(buy_currency, buy_amount, sell_currency, sell_amount):
    try:
        config_file = open(config_file_name, 'r')
        stash_state = json.loads(config_file.read())

        stash_state[buy_currency]['amount'] = stash_state[buy_currency]['amount'] - buy_amount
        if sell_currency == 'Exalted Shard':
            stash_state[sell_currency]['amount'] = (
                stash_state[sell_currency]['amount'] + sell_amount) % CURRENCY_TAB[sell_currency]['stackSize']
        else:
            stash_state[sell_currency]['amount'] = stash_state[sell_currency]['amount'] + sell_amount

        with open(config_file_name, 'w') as stash_state__file:
            json.dump(stash_state, stash_state__file, sort_keys=True, indent=4)
    except FileNotFoundError:
        print('Please provide a valid stash_state file')
        exit(1)


def update_stash_amount(currency_name, amount):
    try:
        config_file = open(config_file_name, 'r')
        stash_state = json.loads(config_file.read())

        stash_state[currency_name] = amount

        with open(config_file_name, 'w') as stash_state__file:
            json.dump(stash_state, stash_state__file, sort_keys=True, indent=4)  # prettier
    except FileNotFoundError:
        print('Please provide a valid stash_state file')
        exit(1)


def update_stash_prices(currency_name, sell_chaos, sell_self, buy_chaos, buy_self):
    try:
        config_file = open(config_file_name, 'r')
        stash_state = json.loads(config_file.read())

        stash_state[currency_name]['price']['sell']['chaos'] = sell_chaos
        stash_state[currency_name]['price']['sell']['self'] = sell_self
        stash_state[currency_name]['price']['buy']['chaos'] = buy_chaos
        stash_state[currency_name]['price']['buy']['self'] = buy_self

        with open(config_file_name, 'w') as stash_state__file:
            json.dump(stash_state, stash_state__file, sort_keys=True, indent=4)
    except FileNotFoundError:
        print('Please provide a valid stash_state file')
        exit(1)
