# Day/Project 22 - Pong!
# This actually was one of the first projects where I coded without any bugs!

import time
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()


class Paddle:
    def __init__(self, xCor, yCor):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(xCor, yCor)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.score = 0
    def move(self):
        screen.update()
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
    def bounce_y(self):
        self.y_move *= -1
        self.x_move *= 1.25
        self.y_move *= 1.25
    def bounce_x(self):
        self.x_move *= -1
        self.x_move *= 1.25
        self.y_move *= 1.25
        self.score += 1
        
        print(f"The new score is now: {self.score}")
paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
screen.tracer(1)
screen.update()

screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

loser = ""
gameOn = True
while gameOn:
    time.sleep(0.1)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle1.paddle) < 45 and ball.xcor() < 355:
        ball.bounce_x()
    elif ball.distance(paddle2.paddle) < 45 and ball.xcor > -355:
        ball.bounce_x()
    if ball.xcor() > 400:
        loser = "Right Paddle"
        break
    elif ball.xcor() < -400:
        loser = "Left Paddle"
        break

screen.textinput("Game Over", f"The ball has left the confines of this lands, due to the user playing {loser}..")
