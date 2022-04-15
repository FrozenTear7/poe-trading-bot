class TradeOrder():
    def __init__(self, type, buyer, sell_currency, sell_amount, buy_currency, buy_amount):
        self.type = type
        self.buyer = buyer
        self.sell_currency = sell_currency
        self.sell_amount = int(sell_amount)
        self.buy_currency = buy_currency
        self.buy_amount = int(buy_amount)

    def update_buy_amount(self, amount):
        self.buy_amount = amount
