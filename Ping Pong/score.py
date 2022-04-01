from turtle import Turtle


class ScoreBoard:
    you = 0
    ai = 0

    def __init__(self):
        self.scoreboard = Turtle(visible=False)
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.goto(0, 320)
        self.scoreboard.pendown()
        self.scoreboard.write(f"You:{self.you}            AI:{self.ai}",
                              align="center", font=("Courier", 20, "normal"))

    def update_score(self, user):
        if user.ycor() < 0:
            self.you += 1
        else:
            self.ai += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"You:{self.you}            AI{self.ai}",
                              align="center", font=("Courier", 20, "normal"))
