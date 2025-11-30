# Project 11 (CAPSTONE PROJECT) - Blackjack
# Probably one of the most fun parts was learning how to play, and after some crazy plays, I think im quite a pro. 😎
# Definetly one of the most fun projects to make, espicially when you get to test it out.

import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


player_deck = []
computer_deck = []

player_total = 0
comp_total = 0



def draw_card(p):
    card = random.choice(cards)
    if p == 'c':
        computer_deck.append(card)
    elif p == 'p':
        player_deck.append(card)
    return card

while True:
    player_deck = []
    computer_deck = []

    player_total = 0
    comp_total = 0

    ask = input("Do you want to play BlackJack? (y/n)")
    if ask == 'y':
        print("LETS PLAY!")
    elif ask == 'n':
        print("Thank you for playing!")
        break
    else:
        print("Invalid answer. Auto-changing to 'y'.")

    #Player draws two cards.
    for i in range(2):
        player_total += draw_card('p')
    print(f"Your deck: {player_deck} -- Total: {player_total}")
    # Computer draws 2 cards. 1 card is not shown to the player.
    comp_total += draw_card('c')
    computer_deck.append("?")
    print(f"Computer deck: {computer_deck} -- Total: {comp_total} (not including the mystery card)")
    computer_deck.remove('?')
    while True:
        choice = input("Would you like another card, (y) or pass? (n)")
        if choice == 'y':
            player_total = player_total + draw_card('p')
            print(f"Your deck: {player_deck} -- Total: {player_total}")
            if player_total == 21:
                print("That was good intuition! You won!")
                break
        else:
            if choice != 'n':
                print("Invalid Syntax for answer. Assuming user meant 'n'.")
            while comp_total < player_total:
                comp_total = comp_total + draw_card('c')
            print(f"Computer deck: {computer_deck} -- Total: {comp_total}")
            if comp_total > 21:
                print("Bust for Computer! You win!")
            elif comp_total == player_total:
                print("Woah! A TIE! Who could've seen that coming?")
            else:
                print("Ruh, roh! You LOST.")
            break
