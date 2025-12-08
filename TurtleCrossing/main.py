# Project 23 - Turtle Crossing
# It's really difficult past Level 3, but really fun!

import time
from turtle import Screen
import car_manager
from player import Player
from car_manager import CarManager

level = 1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

Turtle = Player()

screen.onkey(Turtle.move, "Up")
screen.onkey(Turtle.strafeLeft, "Left")
screen.onkey(Turtle.strafeRight, "Right")

cars = CarManager(25)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.move()
    screen.update()
    if Turtle.ycor() > 300:
        Turtle.goto(0, -280)
        car_manager.speed += 5
        level += 1
        screen.textinput(f"Level {level}", f"You have now reached level {level}. You got this!")
        screen.listen()
    for car in cars.cars:
        if Turtle.distance(car) < 3:
            game_is_on = False
            break
screen.textinput("You just killed a turtle!", "The turtle got run over by the car. How dare you, kill that poor turtle!")