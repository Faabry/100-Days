# ----------------------------- TODO 5:Create a scoreboard -----------------------------

from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGMENT, font=FONT)
# --------------------------------------------------------------------------------------