from menu import Menu, MenuItems
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice in options.split('/') and choice != '':
        drink = menu.find_drink(choice)
        if coffee_maker.is_resources_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        choice = input(f"Your choice is not available.\nWhat would you like? ({options}): ")