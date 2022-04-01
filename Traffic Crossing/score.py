from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.hideturtle()
        self.pencolor("black")
        self.penup()
        self.setposition(-300, 275)
        self.level = 0
        self.pendown()
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=("Courier", 18, "normal"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"GAME OVER", align="center", font=("Courier", 40, "normal"))

    def you_win(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(f"YOU WIN", align="center", font=("Courier", 40, "normal"))
