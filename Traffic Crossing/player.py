from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setposition(0, -275)

    def move(self):
        self.forward(20)

    def next_level(self):
        self.goto(0, -275)
