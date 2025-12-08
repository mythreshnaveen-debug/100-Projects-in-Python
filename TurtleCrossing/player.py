from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])
        self.shape("turtle")
        self.setheading(90)
    def move(self):
        self.goto(self.xcor(), self.ycor() + 10)
    def strafeLeft(self):
        self.goto(self.xcor() - 10, self.ycor())
    def strafeRight(self):
        self.goto(self.xcor() + 10, self.ycor())