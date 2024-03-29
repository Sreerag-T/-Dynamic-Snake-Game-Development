from turtle import Turtle
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 262)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=("Courior", 21, "normal"))
    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=("Courior", 21, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

