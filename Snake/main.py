from collision import body_collision, wall_collision
from screen import GameScreen
from turtle import Screen
import snake
import score
import food


game_over = False

new_screen = GameScreen(600, 600)
new_snake = snake.Snake()
score_board = score.ScoreBoard()
food = food.Food()

while not game_over:
    new_snake.move()
    new_snake.change_direction()
    if new_snake.snakes[0].distance(food) < 15:
        food.refresh()
        score_board.update()
        new_snake.grow()
    if body_collision(new_snake.snakes) or wall_collision(new_snake.snakes) is True:
        new_snake.reset_snake()
        score_board.reset_score()

Screen().exitonclick()
