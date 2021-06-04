from turtle import Turtle, Screen
from random import randint,choice
import turtle as t
boi = Turtle()

# boi.circle(100, steps=4)

# for _ in range(4):
#     boi.forward(100)
#     boi.left(90)

# boi.right(180)

# for _ in range(3):
#     boi.forward(100)
#     boi.right(90)

# boi.left(180)
# for i in range(10):
#     boi.forward(15)
#     boi.penup()
#     boi.forward(5)
#     boi.pendown()
# colours = ["cyan", "purple", "white", "blue"]
Screen().colormode(255)
# Screen().bgcolor("blue")
boi.width(2)


# for i in range(3, 12):
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0,255)
#     boi.color((r,g,b))
#     for _ in range(i):
#         boi.forward(100)
#         boi.left(360 / i)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0,255)
    return (r,g,b)


boi.speed("fastest")
# while True:
#     boi.forward(20)
#     boi.setheading(choice([0, 90, 180, 270, 360]))
#     boi.color(random_color())

# while start!=boi.heading():
for _ in range(int(360/10)):
    boi.color(random_color())
    boi.circle(100)
    boi.seth((boi.heading()+10)%360)