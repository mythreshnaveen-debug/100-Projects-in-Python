# Project 5 -- The Password Generator
# This project was a bit difficult to do, (First ever code project that errored when I ran it for the first time) so I decided to turn it into 2 steps
# 1) Get the random letters, numbers, symbols and merge it as a table
# 3) Randomize the table -> Turn into a string.
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

lns = [letters, numbers, symbols]
gLNS = [nr_letters, nr_numbers, nr_symbols]

fancyList = [lns, gLNS]

passwordList = []
# This piece of code took me way too long to debug.
# Finally, after getting a piece of paper and writing my thoughts out, was I actually able to figure it out.
for i in range(0, len(gLNS)):
    for i2 in range(0, gLNS[i]):
        passwordList.append(random.choice(lns[i]))
print(passwordList)
random.shuffle(passwordList)
print(passwordList)
password = ""
for i in passwordList:
    password += i
print("Your password is: " + password)
