from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cord, y_cord):
        super(Paddle, self).__init__()
        self.fillcolor("white")
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setposition(x_cord, y_cord)

    def move_right(self):
        if self.xcor() + 20 <= 540:
            self.goto(self.xcor()+20, self.ycor())

    def move_left(self):
        if self.xcor() - 20 >= -540:
            self.goto(self.xcor()-20, self.ycor())
