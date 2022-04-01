from turtle import Turtle


class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super(ScoreBoard, self).__init__()
        with open("score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 280)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Ariel", 12, "normal"))

    def update(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                highest_score = str(self.high_score)
                file.write(highest_score)
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Ariel", 12, "normal"))

    def reset_score(self):
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Ariel", 12, "normal"))
