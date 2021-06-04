from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 24, "normal")


class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.up()
        self.color("white")
        self.hideturtle()
        self.goto(0,265)
        self.score = 0
        self.update()


    def increase_score(self):
        self.score += 1
        self.update()


    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)