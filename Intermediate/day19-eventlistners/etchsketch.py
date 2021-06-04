from turtle import Turtle, Screen

boi = Turtle()

screen = Screen()

def move_forward():
    boi.forward(10)


def move_backward():
    boi.backward(10)

def clockwise():
    boi.right(10)

def counterclockwise():
    boi.left(10)

def clear():
    boi.home()
    boi.clear()


screen.listen()

screen.onkey(
    key="w",
    fun=move_forward
)

screen.onkey(
    key="s",
    fun=move_backward
)

screen.onkey(
    key="a",
    fun=counterclockwise
)

screen.onkey(
    key="d",
    fun=clockwise
)

screen.onkey(
    key="c",
    fun=clear
)


screen.exitonclick()