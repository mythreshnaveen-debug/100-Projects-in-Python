import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

speed = 5

class CarManager:
    def __init__(self, carsInt):
        self.cars = []
        for carNum in range(carsInt):
            for i in range(random.randint(1,5)):
                newCar = Turtle()
                newCar.penup()
                newCar.fillcolor(random.choice(COLORS))
                newCar.goto(random.randint(-250, 250), (250 - ((carNum / carsInt) * 250 + (10 * carNum))))
                self.cars.append(newCar)
    def move(self):
        for car in self.cars:
            car.forward(random.randint(0,speed))
            if car.xcor() > 300:
                car.goto(-300, car.ycor())