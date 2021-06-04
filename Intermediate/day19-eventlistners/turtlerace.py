from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the colour: ").lower()
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

y_pos = [-70,-40,-10, 20, 50, 80]
all_turts = []

for turtle_idx in range(6):
    boi = Turtle(shape="turtle")
    boi.penup()
    boi.color(colours[turtle_idx])
    boi.goto(x=-230, y=y_pos[turtle_idx])
    all_turts.append(boi)
if user_bet:
    is_race_on = True

winner = None

while is_race_on:
    for turt in all_turts:
        if turt.xcor()>230:
            winner = turt.pencolor()
            is_race_on=False
            break
        random_dist = random.randint(0, 10)
        turt.forward(random_dist)

if (user_bet == winner):
    print(f"You won and {winner} won")
else:
    print(f"You lost and {winner} won")

screen.exitonclick()