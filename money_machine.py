class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUE = {
        'quarters': 0.25,
        'dimes': 0.1,
        'nickles': 0.05,
        'pennies': 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def ask_coins(self, coin):
        coins = ''
        while not coins.isdigit():
            coins = input(f"How many {coin}?: ")
        return int(coins) * self.COIN_VALUE[coin]
    def process_coins(self):
        print("Please insert coins")
        for coin in self.COIN_VALUE:
            self.money_received += self.ask_coins(coin)

        return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is your {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            self.money_received = 0
            return False