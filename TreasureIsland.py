#Day 3 - Treasure Island
#This is a small 'choose your adventure' inspired game, which takes you to TREASURE ISLAND

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
c1 = input("   Type left or right").lower()
if c1 == "left":
    print("""You\'ve come to a lake. 
    There is an island in the middle of the lake. 
    Type "wait" to wait for a boat. 
    Type "swim" to swim across.\n""")
    c2 = input("What do you choose? ").lower()
    if c2 == "wait":
        print("""You arrive at the island unharmed. 
        There is house with 3 doors. One red, 
        one yellow and one blue. """)
        c3 = input("Which color do you choose?").lower()
        if c3 == "red":
            print("It's a room full of fire. Game Over")
        elif c3 == "yellow":
            print("You found the treasure. You Win!")
        elif c3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You enter a door that does not exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell in to a hole. Game Over.")
