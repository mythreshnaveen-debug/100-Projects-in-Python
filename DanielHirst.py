# Project 18 - Daniel Hirst Panting
# Firs ttime trying out turtle, and as we aren't using that much modules (in the same project) anymore, I thought it would've been better to just let this one act as a file.

import random
import turtle as t

colors = [ (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), (68, 105, 90), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53), (134, 42, 38), (47, 66, 61), (0, 122, 125)]



turtle = t.Turtle()
screen = t.Screen()

t.colormode(255)

turtle.speed('fastest')

turtle.penup()
turtle.right(90)
turtle.backward(450)
turtle.left(90)
turtle.backward(325)
turtle.pendown()

pastLeft = True

for h in range(10):
    for w in range(10):
        newColor = random.choice(colors)
        turtle.fillcolor(newColor)
        turtle.pencolor(newColor)
        with turtle.fill():
            turtle.circle(20)
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    turtle.penup()
    turtle.backward(50)
    if pastLeft:
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    else:
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    pastLeft = not pastLeft
    turtle.pendown()

turtle.screen = screen
screen.exitonclick()
