from turtle import Turtle, Screen


def border(width, height):
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.color("white")
    line.setposition(-width / 2 + 25, -height / 2 + 25)
    line.pendown()
    i = 1
    for direction in [0, 90, 180, 270]:
        line.setheading(direction)
        line.forward((width*(1+i)+height*(1-i))/2-50)
        i *= -1


class GameScreen:

    def __init__(self, width, height):
        self.screen = Screen()
        self.screen.setup(width, height)
        self.screen.bgcolor("black")
        self.screen.title("My Python Game")
        self.screen.delay(0)
        border(width, height)
