from turtle import Turtle
import random


class Food(Turtle):
    random_x = random.randrange(-245, 245, 20)
    random_y = random.randrange(-245, 245, 20)

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(self.random_x, self.random_y)

    def refresh(self):
        self.goto(random.randrange(-245, 245, 20), random.randrange(-245, 245, 20))
