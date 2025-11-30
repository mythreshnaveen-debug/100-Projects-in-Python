# Day/Project 13 -- The Pizzeria
# For some reason, we just didn't have a project for today... So, I just made my own!

logo = """
  ________            ____  _                     _      
 /_  __/ /_  ___     / __ \(_)_______  ___  _____(_)___ _
  / / / __ \/ _ \   / /_/ / /_  /_  / / _ \/ ___/ / __ `/
 / / / / / /  __/  / ____/ / / /_/ /_/  __/ /  / / /_/ / 
/_/ /_/ /_/\___/  /_/   /_/ /___/___/\___/_/  /_/\__,_/                                                           
"""

print(logo)

TOPPINGS = {
    "Sasuage": 0.5,
    "Pineapple": 0.75,
    "Pepperoni": 1,
    "Chicken": 1,
    "Black Olive": 0.5
}
CRUST_PRICES = {
    "Gluten": 5,
    "Regular": 4,
    "Stuffed Crust": 7
}

SIZES = {
    "Light": 0.75,
    "Regular": 1,
    "Large": 1.25
}

def askInList(prompt, Dic):
    print(prompt)
    conv = {}
    num = 1
    for key in Dic:
        print(f"{num}) {key}")
        conv[num] = key
        num += 1
    choice = int(input(">"))
    return Dic[conv[num - 1]]

# Create a list of toppings, and give the ability to add/edit your pizza.
print("Welcome to The Pizzeria")
while True:
    total = 0
    ask = input("Would you like to build a Pizza? (y/n)")
    crust = 0
    sizeModifier = 0
    if ask == "n":
        print("See you soon!")
    crust = askInList("What crust would you like?", CRUST_PRICES)
    sizeModifier = askInList("What size would you like?", SIZES)
    total += crust * sizeModifier
    print(f"Your total is now: ${total}.")
    while True:
        topping = askInList("What toppings would you like?", TOPPINGS)
        total += topping * sizeModifier
        print(f"Your total is now: ${total}.")
        con = input("Would you like to add more toppings? (y/n)")
        if con == 'n':
            break
    print(f"Your total comes out to ${total}.")
