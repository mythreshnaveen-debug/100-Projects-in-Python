# Project 4 - Rock Paper Scissors Game
# I wasn't sure if I actually had done it correctly the first time, but after testing it over a 100 times, I realized that I did, and was pretty proud of myself!

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


mList = [rock, paper, scissors]

playerChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if playerChoice < 0 or playerChoice > 2:
    print("Invalid choice. Please restart the program.")
else:
    print(mList[playerChoice])
    computerChoice = int(random.randint(0, 2))
    
    print(f"The computer chose: \n{mList[computerChoice]}")
    
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice > computerChoice and not (playerChoice == 2 and computerChoice == 0):
        print("You won!")
    else:
        print("You lose!")
