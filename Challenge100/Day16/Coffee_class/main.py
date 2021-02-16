from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_menu = Menu()
barista = CoffeeMaker()
cashier = MoneyMachine()

while True:
    order = input(f"What is your order from the {machine_menu.get_items()} ")

    if order == "report":
        barista.report()
        cashier.report()
    elif order == "off":
        break
    else:
        order = machine_menu.find_drink(order)
        money_ok = cashier.make_payment(order.cost)
        ingredient_ok = barista.is_resource_sufficient(order)
        if money_ok and ingredient_ok:
            barista.make_coffee(order)
