from menu import Menu as m
from coffee_maker import CoffeeMaker as c
from money_machine import MoneyMachine as mM
# Project 16 - Coffee Machine 2.0
# This is basically the same as Coffee Machine 1.0, but uses some libraries.
print("Coffee Machine for Python&CO.")
print("Enter pwroff to Power off the machine.\n\n")

# This wierd formatting of the Menu, CoffeeMaker, and the MoneyMachine, is due to me not
# realizing that they are Objects, and that I had to make them first...
Menu = m()
CoffeeMaker = c()
MoneyMachine = mM()

def get_key_from_value(my_dict, value_to_find):
    for key, value in my_dict.items():
        if value == value_to_find:
            return key
            break
    return None

while True:
    coffee = input(f"What coffee would you like? ({Menu.get_items()}): ").lower()
    if coffee == "pwroff":
        print("Shutting off")
        break
    elif coffee == "resources":
        CoffeeMaker.report()
        MoneyMachine.report()
    elif Menu.find_drink(coffee):
        coffeeName = coffee
        coffee = Menu.find_drink(coffeeName)
        print(f"That will be: {coffee.cost}")
        if MoneyMachine.make_payment(coffee.cost):
            if CoffeeMaker.is_resource_sufficient(coffee):
                CoffeeMaker.make_coffee(coffee)
    else:
        print("Invalid Input.")