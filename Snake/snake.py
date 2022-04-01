from turtle import Turtle, Screen
import time


class Snake(Turtle):
    screen = Screen()

    def __init__(self):
        super(Snake, self).__init__()
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for n in range(0, 3):
            new_segment = Turtle(shape="square")
            new_segment.color("green")
            new_segment.penup()
            new_segment.setposition(-n * 20, 0)
            self.snakes.append(new_segment)

    def move(self):
        i = len(self.snakes) - 1
        while i > 0:
            position = self.snakes[i - 1].pos()
            self.snakes[i].goto(position)
            i -= 1
        self.snakes[0].forward(20)
        time.sleep(0.1)

    def change_direction(self):
        self.screen.listen()
        self.screen.onkey(self.move_up, "Up")
        self.screen.onkey(self.move_down, "Down")
        self.screen.onkey(self.move_left, "Left")
        self.screen.onkey(self.move_right, "Right")

    def move_up(self):
        if self.snakes[0].heading() != 270:
            self.snakes[0].setheading(90)

    def move_down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)

    def move_left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)

    def move_right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)

    def grow(self):
        grow_segment = Turtle()
        grow_segment.shape("square")
        grow_segment.color("green")
        grow_segment.penup()
        self.snakes.append(grow_segment)

    def reset_snake(self):
        for snake in self.snakes:
            snake.hideturtle()
        self.snakes.clear()
        self.create_snake()
