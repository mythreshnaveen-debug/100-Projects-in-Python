# Project 13 - Guess the Number
# A lot easier than the other projects that I've made...

import random

logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
print("Welcome to the Number Guessing Game!")
diff = input("Choose a DIFFICULTY:\n1) Easy\n2) HARD\n\n>")
attempts = 10
number = random.randint(1,100)
userGuessed = False
if diff == '2':
    attempts -= 5
else:
    if diff != "1":
        print("Invalid Answer, assuming user meant Easy.")
while attempts > 0:
    print(f"\n\nYou have {attempts} attempts to guess the number that I am thinking of.")
    guess = float(input(">"))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    elif guess == number:
        print(f"You did it! The answer was {number}")
        userGuessed = True
        break
    attempts -= 1
