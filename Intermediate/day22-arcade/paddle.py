from turtle import Turtle


class Paddle(Turtle):


    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.up()
        self.goto(position)


    def move_up(self):
        if self.ycor()<220:
            self.goto(self.xcor(), self.ycor() + 20)


    def move_down(self):
        if self.ycor()> -220:
            self.goto(self.xcor(), self.ycor() - 20)