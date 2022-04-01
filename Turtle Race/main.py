import turtle
import random

screen = turtle.Screen()
n = int(screen.textinput("Number of Participants", "Choose 1 through 7 to set the number of participants: "))
guess = screen.textinput("Who will Win?", "Guess which colour will win? (Choose from the colours of the rainbow):\n")
participant_list = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]


def game_start(j):
    screen.setup(width=j*100, height=j*80)
    refree = turtle.Turtle()
    refree.penup()
    refree.setposition(-j*100/2+50, -j*80/2)
    refree.setheading(90)
    refree.pendown()
    refree.forward(j*80)
    refree.penup()
    refree.setposition(j*100/2-50, j*80/2)
    refree.setheading(270)
    refree.pendown()
    refree.forward(j*80)
    refree.hideturtle()

def create_turtle(colour):
    turtle_name = turtle.Turtle()
    turtle_name.color(colour)
    turtle_name.shape("turtle")
    return turtle_name


def race_participants(number):
    i = 0
    turtle_list = []
    while i < number:
        name = participant_list[i]
        name = create_turtle(name)
        turtle_list.append(name)
        name.penup()
        name.setposition(-number*100/2+50, -number*80/2+80*i+40)
        name.pendown()
        i += 1
    return turtle_list


def race_start():
    end = False
    while not end:
        for names in participants:
            names.forward(random.randrange(1, 11))
            if names.xcor() >= n*100/2-50:
                for x in range(0, len(participants)):
                    if participants[x] == names:
                        winner_name = participant_list[x]
                        return winner_name


game_start(n)
participants = race_participants(n)
winner = race_start()

if winner == guess:
    print(f"{guess} has won the race, you win!")
else:
    print(f"{winner} has won the race, you lose!")

screen.exitonclick()
