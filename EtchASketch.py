# Project 21 - EtchASketch
# This was purposely really easy, and that was because Day 20's project (Snake) Took way too long.

from turtle import Screen, Turtle
turtle = Turtle()
screen = Screen()
turtle.screen = screen
screen.listen()

def forward():
    turtle.forward(10)
def turnRight():
    turtle.right(10)
def turnLeft():
    turtle.left(10)

screen.onkey(forward, "Up")
screen.onkey(turnRight, "Right")
screen.onkey(turnLeft, "Left")

screen.exitonclick()
