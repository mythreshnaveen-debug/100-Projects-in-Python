# Project 19 - Turtle Race
# I really enjoyed making this one, since testing this was super fun.

import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

winning_color = ""

i = 1
for color in colors:
    newTurtle = Turtle("turtle")
    newTurtle.penup()
    newTurtle.color(color)
    newTurtle.goto(-230, 200 - (25 + (300 / len(colors) * i)))
    turtles.append(newTurtle)
    newTurtle.screen = screen
    if user_bet == color:
        newTurtle.pendown()
    i += 1

while True:
    gameOver = False
    for turtle in turtles:
        rand_distance = random.randint(0, 100)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            gameOver = True
            winning_color = turtle.pencolor()
            break
    if gameOver:
        break

if user_bet == winning_color:
    screen.textinput("You Won!", f"The turtle that won's color is: {winning_color}!\n\n(There was no information box in Turtle, so excuse the random text box below)")
else:
    screen.textinput("You Lost.", f"The turtle that won's color is: {winning_color}.\n\n(There was no information box in Turtle, so excuse the random text box below)")
