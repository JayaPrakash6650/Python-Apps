from score import ScoreBoard
from turtle import Screen
from paddle import Paddle
from ball import Ball
from background import Border
import time


def ai_move(paddle, ball):
    if paddle.xcor() < ball.xcor() and paddle.xcor() + 100 <= 540:
        paddle.goto(paddle.xcor()+1, paddle.ycor())
    elif paddle.xcor() > ball.xcor() and paddle.xcor() - 100 >= -540:
        paddle.goto(paddle.xcor()-1, paddle.ycor())


bg_screen = Screen()
bg_screen.setup(width=1280, height=700)
bg_screen.bgcolor("black")
bg_screen.title("Impossible Pong Game")
bg_screen.tracer(0)
game_on = True

new_border = Border()
scoreboard = ScoreBoard()
you_paddle = Paddle(0, -300)
ai_paddle = Paddle(0, 300)
pong = Ball()

while game_on:
    bg_screen.update()
    bg_screen.listen()
    bg_screen.onkeypress(you_paddle.move_left, "Left")
    bg_screen.onkeypress(you_paddle.move_right, "Right")
    pong.move()
    pong.wall_bounce()
    pong.paddle_bounce(ai_paddle)
    pong.paddle_bounce(you_paddle)
    ai_move(ai_paddle, pong)
    if pong.ycor() > 350:
        pong.restart()
        scoreboard.update_score(you_paddle)
    elif pong.ycor() < -350:
        pong.restart()
        scoreboard.update_score(ai_paddle)

bg_screen.exitonclick()
