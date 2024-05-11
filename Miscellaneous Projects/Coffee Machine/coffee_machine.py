"""Coffee Machine"""

from data import MENU
from data import resources

turn_off = True

while turn_off:
    coffee_type = input(" What would you like to have? (espresso/latte/cappuccino):")

    if coffee_type == "report":
        print(resources)
    elif coffee_type == "end":
        turn_off = False
    else:
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        collected_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

        if coffee_type == "espresso":
            if resources['water'] >= MENU['espresso']['ingredients']['water']:
