from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(["red", "orange", "green", "black", "blue", "purple"]))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setposition(300, random.randrange(-250, 300, 20))
        self.setheading(180)

    def move_car(self):
        if self.xcor() > -320:
            self.forward(20)
        else:
            self.hideturtle()
