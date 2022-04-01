from turtle import Screen
from score import Score
from player import Player
from car import CarManager
import time


bg_screen = Screen()
bg_screen.title("Turtle Crossing Game")
bg_screen.setup(width=600, height=600)
bg_screen.tracer(0)
game_on = True
level = Score()
player = Player()
count = 0
difficulty = 10
car_speed = 0.1
cars = []

bg_screen.listen()
bg_screen.onkey(player.move, "Up")

while game_on:
    time.sleep(car_speed)
    bg_screen.update()
    if count % difficulty == 0:
        cars.append(CarManager())
    for car in cars:
        car.move_car()
    if player.ycor() > 300:
        level.update_level()
        player.next_level()
        difficulty -= 1
        car_speed *= 0.8
        if difficulty == 0:
            game_on = False
            level.you_win()
        for car in cars:
            car.hideturtle()
    count += 1
    for car in cars:
        if car.distance(player) < 10:
            game_on = False
            level.game_over()
bg_screen.exitonclick()
