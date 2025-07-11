from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

"""
MenuItem Class
Attributes:
- name
- cost
- ingredients
Menu Class
Methods:
- get_items()
Returns all the names of the available menu items as a concatenated string.
e.g. “latte/espresso/cappuccino”
- find_drink(order_name)
CoffeeMaker Class
Methods:
- report()
Prints a report of all resources.

- is_resource_sufficient(drink)
Parameter drink: (MenuItem) The MenuItem object to make.
Prints a message if ingredients are insufficient.
Returns True when the drink order can be made, False if ingredients are insufficient.

make_coffee(order)
Parameter order: (MenuItem) The MenuItem object to make.
Deducts the required ingredients from the resources.

MoneyMachine Class
Methods:
- report()
Prints the current profit
e.g.
Money: $0
- make_payment(cost)
Parameter cost: (float) The cost of the drink.
Returns True when payment is accepted, or False if insufficient.
"""

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turnoff=True

while turnoff:
    options=menu.get_items()
    order=input(f"What would you like({options}): ").lower()
    if order=='report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        turnoff = False

    else:
        drink = menu.find_drink(order)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)