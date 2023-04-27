from math import ceil, floor
import requests

from constants import LEAGUE_NAME


class PriceCalculator():
    def __init__(self):
        response = requests.get(
            f'https://poe.ninja/api/data/currencyoverview?league={LEAGUE_NAME}&type=Currency&language=en')
        self.currency_json = response.json()

    def get_currency_config(self, currency_name):
        return list(filter(lambda curr: curr['currencyTypeName'] == currency_name, self.currency_json['lines']))[0]

    def get_sell_price(self, currency_name):
        currency_config = self.get_currency_config(currency_name)
        sell_price = round(currency_config['receive']['value'], 2)

        return f'~price {sell_price} chaos'

    def verify_sell_price(self, offered_price, currency_name):
        currency_config = self.get_currency_config(currency_name)
        return round(currency_config['receive']['value'], 2) == round(offered_price, 2)

    def get_buy_price(self, currency_name, exchangeName):
        currency_config = self.get_currency_config(currency_name)
        sell_price = round(currency_config['pay']['value'], 2)

        return f'~price {sell_price} {exchangeName}'

    def verify_buy_price(self, offered_price, currency_name):
        currency_config = self.get_currency_config(currency_name)
        return round(currency_config['pay']['value'], 2) == round(offered_price, 2)
