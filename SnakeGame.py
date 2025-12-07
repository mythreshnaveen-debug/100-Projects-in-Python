#Proj. 20 -The Snake Game

import random
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(600, 400)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.listen()

positions = [(0, 0), [-20, 0], (-40, 0),(-60, 0), (-80, 0), (-100, 0)]
segments = []

food = Turtle("circle")
food.fillcolor("blue")
food.pencolor("blue")
food.penup()


food.goto(random.randint(-15, 15) * 20, random.randint(-10, 10) * 20)

def createNewSegment(position):
    segment = Turtle("square")
    segment.speed("fastest")
    segment.penup()
    segment.color("white")
    segment.goto(position)
    segment.screen = screen
    segments.append(segment)



for position in positions:
    createNewSegment(position)

screen.update()

def turnLeft():
    segments[0].setheading(180)

def turnRight():
    segments[0].setheading(0)

def turnDown():
    segments[0].setheading(270)

def turnUp():
    segments[0].setheading(90)

screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.onkey(turnDown, "Down")
screen.onkey(turnUp, "Up")

eatingFood = False

gameOn = True
while gameOn:
    eatingFood = True
    #Snake Moving Animation
    for segNum in range(len(segments) - 1, 0, -1):
        segment = segments[segNum]
        segment.goto(segments[segNum - 1].xcor(), segments[segNum - 1].ycor())

    #The Snake acutally moving
    segments[0].forward(20)

    #Food Eating Logic
    if segments[0].distance(food) < 15:
        eatingFood = True
        pos = (segments[-2].xcor() + 20, segments[-2].ycor())
        createNewSegment(pos)
        food.goto(random.randint(-300, 300), random.randint(-200, 200))

    #Ending game when snake hits border
    x = float(segments[0].xcor())
    y = float(segments[0].ycor())
    if x > 300 or x < -300 or y > 200 or y < -200:
        gameOn = False

    #Ending the game when snake intersects

    #PART 1 - Grab all Position
    positions = []
    for segment in segments:
        xPoint = int(segment.xcor())
        yPoint = int(segment.ycor())
        positions.append((xPoint, yPoint))

    #PART 2 - Check if 1 position appears 2+ times, and break while loop if it does.
    for segment in segments:
        for segment2 in segments:
            if segment != segment2:
                print(segment.distance(segment2))
            if segment.distance(segment2) < 20 and segment2 != segment and not eatingFood:
                gameOn = False

    #Updating the screen
    time.sleep(0.1)
    screen.update()
screen.textinput("Game Over.", "You Lost.")
