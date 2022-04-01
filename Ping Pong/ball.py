from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.fillcolor("white")
        self.penup()
        self.i = random.choice([-1, 1])
        self.j = random.choice([-1, 1])

    def move(self):
        self.goto(self.xcor()+self.i, self.ycor()+self.j)

    def wall_bounce(self):
        if self.xcor() >= 580 or self.xcor() <= -580:
            self.i *= -1

    def paddle_bounce(self, user):
        if self.distance(user) < 50 and self.ycor() == 280:
            self.j *= -1
        elif self.distance(user) < 50 and self.ycor() == -280:
            self.j *= -1

    def restart(self):
        self.i = random.choice([-1, 1])
        self.j = random.choice([-1, 1])
        self.goto(0, 0)
