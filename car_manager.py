import turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):
    def __init__(self,pos_y,level):
        super().__init__()
        self.shape('square')
        self.shapesize(1,2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(270,pos_y)
        self.speed = STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * level)

    def move(self):
        self.goto(self.xcor() - self.speed,self.ycor())




