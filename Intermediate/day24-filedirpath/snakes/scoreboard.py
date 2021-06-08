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
        with open("highscore.txt") as data:
            self.highscore = int(data.read())
        self.update()


    def increase_score(self):
        self.score += 1
        self.update()


    def update(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.score = 0
            self.save_highscore()
            self.update()
    
    def save_highscore(self):
        with open("highscore.txt",mode="w") as data:
            data.write(str(self.highscore))