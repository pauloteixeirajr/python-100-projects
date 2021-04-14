# Object Oriented Programming (OOP)
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ").lower()

    if order == "off":
        is_on = False
    elif order == "report":
        coffe_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        is_enough_ing = coffe_machine.is_resource_sufficient(drink)
        accepted_payment = money_machine.make_payment(drink.cost)
        if drink and is_enough_ing and accepted_payment:
            coffe_machine.make_coffee(drink)
