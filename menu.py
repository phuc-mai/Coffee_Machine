class MenuItems:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItems(name='latte', cost=2.5, water=150, milk=250, coffee=24),
            MenuItems(name='espresso', cost=1.5, water=50, milk=0, coffee=18),
            MenuItems(name='cappuccino', cost=2, water=100, milk=100, coffee=24)
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry, that drink is not available!")

