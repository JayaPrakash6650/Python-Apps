from turtle import Turtle
import random


class Border(Turtle):
    def __init__(self):
        super(Border, self).__init__()
        self.hideturtle()
        self.pencolor("white")
        self.fillcolor("white")
        self.draw_border()

    def draw_border(self):
        self.penup()
        self.goto(x=590, y=300)
        self.pendown()
        self.goto(x=590, y=-300)
        self.penup()
        self.goto(x=-590, y=-300)
        self.pendown()
        self.goto(x=-590, y=300)

    def draw_block(self):
        self.penup()
        self.shape("square")
        self.goto(x=random.randint(-540, 540), y=random.randint(-250, 250))
        self.shapesize(stretch_wid=1, stretch_len=5)

