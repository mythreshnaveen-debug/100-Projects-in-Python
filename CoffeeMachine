# Project 15 - Coffee Machine
# This is meant to be the code that runs inside of a coffee machine. 
# Since I didn't have an actual coffee machine to program, 
# I just used print statements for dispensing the coffee, 
# and there is no part which makes the coffee.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25
print("Coffee Machine for Python&CO.")
print("Enter pwroff to Power off the machine.\n\n")

def get_key_from_value(my_dict, value_to_find):
    for key, value in my_dict.items():
        if value == value_to_find:
            return key
            break
    return None

def checkSupplies(coffee):
    for ingredient in coffee['ingredients']:
        if resources[ingredient] < coffee['ingredients'][ingredient]:
            return False
    for ingredient in coffee['ingredients']:
        resources[ingredient] -= coffee['ingredients'][ingredient]
    resources["money"] += coffee['cost']
    return True

while True:
    coffee = input("What coffee would you like? (espresso/latte/cappuccino): ")
    if coffee == "pwroff":
        print("Shutting off")
        break
    elif coffee == "resources":
        print("Your resources is:")
        for key in resources:
            print(f"{key}: {resources[key]}")
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        coffee = MENU[coffee]
        p = int(input("Insert pennies: "))
        n = int(input("Insert nickels: "))
        d = int(input("Insert dimes: "))
        q = int(input("Insert quarters: "))
        total = (p * penny) + (n * nickel) + (d * dime) + (q * quarter)
        if total >= coffee["cost"]:
            if checkSupplies(coffee):
                print(f"Thank you! Here is your ${total - coffee['cost']} back.")
                print(f"Here is your {get_key_from_value(MENU, coffee)}! 🍵")
            else:
                print("Sorry, there is not enough supplies in the machine to make your coffee. Money refunded.")
        else:
            print("Sorry, that is not enough. Money refunded.")
    else:
        print("Invalid Input.")
