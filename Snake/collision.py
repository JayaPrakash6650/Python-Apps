def body_collision(snakes):
    position = []
    for i in range(1, len(snakes)):
        position.append(snakes[i].pos())
    if snakes[0].pos() in position:
        return True
    else:
        return False


def wall_collision(snakes):
    if snakes[0].xcor() < -240 or snakes[0].xcor() > 240 or snakes[0].ycor() < -240 or snakes[0].ycor() > 240:
        return True
    else:
        return False
